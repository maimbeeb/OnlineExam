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
