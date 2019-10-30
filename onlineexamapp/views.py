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
