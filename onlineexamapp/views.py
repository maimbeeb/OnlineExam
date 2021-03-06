import stripe  # for stripe integration
from django.shortcuts import render, redirect
# forms for templates
from onlineexamapp.forms import UserLogin, UserRegister, UserForget, UserChangePwd
from onlineexamapp.models import User, UserExam  # models for DB operations
from django.core import serializers
from django.core.mail import send_mail  # send_mail
from django.conf import settings

# define stripe secret key

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

# login functionality


def login(request):
    template = 'index.html'

    # check user session exists
    if "user_email"in request.session:
        return redirect("/home")
    else:
        if request.method == "POST":
            form = UserLogin(request.POST)
            if form.is_valid():
                user = User.objects.filter(
                    uemail=form.cleaned_data['uemail'], upwd=form.cleaned_data['upwd']).exists()
                if user == True:
                    # A backend authenticated the credentials
                    data = User.objects.get(uemail=form.cleaned_data['uemail'])
                    request.session["user_email"] = data.uemail
                    return redirect("/home")
                else:
                    # No backend authenticated the credentials
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Invalid username or password!'
                    })

        else:
            form = UserLogin()
    return render(request, 'index.html', {'form': form})

# register functionality


def register(request):
    # check user session exists
    if "user_email"in request.session:
        return redirect("/home")
    else:
        template = 'register.html'
        if request.method == "POST":
            form = UserRegister(request.POST)
            if form.is_valid():
                # check email already exists
                if User.objects.filter(uemail=form.cleaned_data['uemail']).exists():
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Email already exists.'
                    })
                elif form.cleaned_data['upwd'] != form.cleaned_data['ucpwd']:
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Passwords do not match.'
                    })
                else:
                    # Create the user:
                    user = User(
                        uname=form.cleaned_data['uname'],
                        uemail=form.cleaned_data['uemail'],
                        upwd=form.cleaned_data['upwd']
                    )
                    user.save()
                    return render(request, template, {
                        'form': form,
                        'success_message': True
                    })
        else:
            form = UserRegister()
        return render(request, 'register.html', {'form': form})

# forget password fuctionality


def forget(request):
    # check user session exists
    if "user_email"in request.session:
        return redirect("/home")
    else:
        template = 'forget-form.html'
        if request.method == "POST":
            form = UserForget(request.POST)
            if form.is_valid():
                # check email already exists
                if User.objects.filter(uemail=form.cleaned_data['uemail']).exists():
                    data = User.objects.get(uemail=form.cleaned_data['uemail'])

                    # send_mail to user email
                    subject = 'Online Exam - Forget Password'
                    message = 'Hi ' + data.uname + '\n\nYour password is ' + data.upwd
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [form.cleaned_data['uemail']]
                    send_mail(subject, message, email_from, recipient_list)
                    form = UserForget()
                    return render(request, template, {
                        'form': form,
                        'success_message': 'Your password is successfully sent to your email.'
                    })
                else:
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Email not exists!'
                    })
        else:
            form = UserForget()
        return render(request, 'forget-form.html', {'form': form})

# logout functionality


def logout(request):

    if 'user_email' in request.session:
        # delete user session
        del request.session['user_email']
    return redirect('/')

# home functionality


def home(request):
    
    # check user session exists
    if "user_email"in request.session:
        exams = [{"eno": 1, "name": "Assessment and Qualifications Alliance (AQA)", "fees": "100", "date": "10-01-2020"}, {"eno": 2, "name": "Oxford, Cambridge and RSA Examinations (OCR)", "fees": "150", "date": "15-01-2020"}, {"eno": 3, "name": "Edexcel (Edexcel Pearson - London Examinations)", "fees": "100", "date": "20-01-2020"}, {
            "eno": 4, "name": "Welsh Joint Education Committee (WJEC)", "fees": "150", "date": "25-01-2020"}, {"eno": 5, "name": "Council for the Curriculum, Examinations & Assessment (CCEA)", "fees": "100", "date": "30-01-2020"}]
        myexams = UserExam.objects.filter(
            uemail=request.session['user_email']).values_list('eno', flat=True)
        not_applied_exams = [e for e in exams if str(e['eno']) not in list(myexams)]

        return render(request, 'home.html', {'exams': not_applied_exams, 'class': True})
    else:
        return redirect("/")

# my profile functionality


def myprofile(request):
    # check user session exists
    if 'user_email' in request.session:
        email = request.session['user_email']
        data = User.objects.get(uemail=email)
        name = data.uname
        return render(request, 'myprofile.html', {'email': email, 'name': name})
    else:
        return redirect("/")


# my applied exams functionality


def myexams(request):
    # check user session exists
    if 'user_email' in request.session:
        exams = [{"eno": 1, "name": "Assessment and Qualifications Alliance (AQA)", "fees": "100", "date": "10-01-2020"}, {"eno": 2, "name": "Oxford, Cambridge and RSA Examinations (OCR)", "fees": "150", "date": "15-01-2020"}, {"eno": 3, "name": "Edexcel (Edexcel Pearson - London Examinations)", "fees": "100", "date": "20-01-2020"}, {
            "eno": 4, "name": "Welsh Joint Education Committee (WJEC)", "fees": "150", "date": "25-01-2020"}, {"eno": 5, "name": "Council for the Curriculum, Examinations & Assessment (CCEA)", "fees": "100", "date": "30-01-2020"}]

        myexams = UserExam.objects.filter(
            uemail=request.session['user_email']).values_list('eno', flat=True)
        applied_exams = [e for e in exams if str(e['eno']) in list(myexams)]
        return render(request, 'myexams.html', {'applied_exams': applied_exams})
    else:
        return redirect("/")

# change password functionality


def changepwd(request):
    # check user session exists
    if 'user_email' in request.session:
        template = 'change-pwd.html'
        if request.method == "POST":
            form = UserChangePwd(request.POST)
            if form.is_valid():
                if User.objects.filter(upwd=form.cleaned_data['upwd']).exists():
                    user = User.objects.get(
                        uemail=request.session['user_email'])
                    user.upwd = form.cleaned_data['unpwd']
                    user.save()
                    form = UserChangePwd()
                    return render(request, template, {
                        'form': form,
                        'success_message': 'Your password successfully changed.'
                    })
                else:
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Old password incorrect!'
                    })
        else:
            form = UserChangePwd()
        return render(request, template, {'form': form})
    else:
        return redirect("/")


# apply exam functionality
def apply(request, eno):
    # check user session exists
    if 'user_email' in request.session:
        exams = [{"eno": 1, "name": "Assessment and Qualifications Alliance (AQA)", "fees": "100", "date": "10-01-2020"}, {"eno": 2, "name": "Oxford, Cambridge and RSA Examinations (OCR)", "fees": "150", "date": "15-01-2020"}, {"eno": 3, "name": "Edexcel (Edexcel Pearson - London Examinations)", "fees": "100", "date": "20-01-2020"}, {
            "eno": 4, "name": "Welsh Joint Education Committee (WJEC)", "fees": "150", "date": "25-01-2020"}, {"eno": 5, "name": "Council for the Curriculum, Examinations & Assessment (CCEA)", "fees": "100", "date": "30-01-2020"}]
        for x in exams:
            if eno == x['eno']:
                exam = x
        amount = int(exam['fees'])
        stripeamount = int(exam['fees']) * 100
        examname = exam['name'] + 'charge'
        key = settings.STRIPE_PUBLISHABLE_KEY
        myexams = UserExam.objects.filter(
            uemail=request.session['user_email']).values_list('eno', flat=True)

        if str(eno) in list(myexams):
            message = True
        else:
            message = False
        return render(request, 'apply-exam.html', {'exam': exam, 'key': key, 'amount': amount, 'stripeamount': stripeamount, 'examname': examname, 'message': message})
    else:
        return redirect("/")


# stripe charge functionality
def charge(request, eno):
    # check user session exists
    if 'user_email' in request.session:
        exams = [{"eno": 1, "name": "Assessment and Qualifications Alliance (AQA)", "fees": "100", "date": "10-01-2020"}, {"eno": 2, "name": "Oxford, Cambridge and RSA Examinations (OCR)", "fees": "150", "date": "15-01-2020"}, {"eno": 3, "name": "Edexcel (Edexcel Pearson - London Examinations)", "fees": "100", "date": "20-01-2020"}, {
            "eno": 4, "name": "Welsh Joint Education Committee (WJEC)", "fees": "150", "date": "25-01-2020"}, {"eno": 5, "name": "Council for the Curriculum, Examinations & Assessment (CCEA)", "fees": "100", "date": "30-01-2020"}]
        for x in exams:
            if eno == x['eno']:
                exam = x

        amount = int(exam['fees']) * 100
        examname = exam['name']
        if request.method == 'POST':
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description=examname + "charge",
                source=request.POST['stripeToken']
            )
        key = settings.STRIPE_PUBLISHABLE_KEY
        user_detail = User.objects.get(uemail=request.session['user_email'])
        user_exam = UserExam(
            eno=eno,
            uemail=request.session['user_email'],
            uname=user_detail.uname,
            exname=examname,
            amount=int(exam['fees']),
            currency='usd',
            stripetoken=request.POST['stripeToken'],
            charge_response=charge
        )
        # save user applied exams in db
        user_exam.save()
        subject = 'Online Exam - Applied for ' + examname
        message = 'Hi ' + user_detail.uname + ',\n\nYou have applied for ' + examname + \
            '\n\nFor later, your hall ticket will be send to your email address.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.session['user_email']]

        # send mail to user for exam details
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/exam/' + str(eno))
    else:
        return redirect("/")
