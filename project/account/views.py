from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from account.forms import UserAdminCreationForm

# Create your views here.

@login_required
def dashboard(request):
    # here will get all events user create and participant in
    context = {}
    return render(request, 'account/dashboard.html', context)

@login_required
def profile(request):
    # here will get all events user create and participant in

    context = {}
    return render(request, 'account/dashboard.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('events:events_list')
                else:
                    form = LoginForm()
                    message = "your accound has been disabled by the admin"
                    context = {'form': form, 'message':message}
                    return render(request, 'registration/login.html', context)
            else:
                form = LoginForm()
                message = "the email or password is wrong, if you didn't make an account before please signup"
                context = {'form': form, 'message':message}
                return render(request, 'registration/login.html', context)
        else:
            form = LoginForm()
            message = "thers's error in the form, try again:"
            context = {'form': form, 'message':message}
            return render(request, 'registration/login.html', context)
    else:
        form = LoginForm()
        message = "Please, use the following form to log-in:"
        context = {'form': form, 'message':message}
        return render(request, 'registration/login.html', context)
           
def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message = "successfully signup please log in "
            context = {'form': form, 'message':message}
            return render(request, 'registration/register.html', context)
        else:
            message = "ther's error in the form, try again "
            context = {'form': form, 'message':message}
            return render(request, 'registration/register.html', context)
    else:
        message = "Please, sign up using the following form:"
        form = UserAdminCreationForm(request.POST)
        context = {'form': form, 'message':message}
        return render(request, 'registration/register.html', context)


    #  message = "Please, use the following form to log-in:"
    #             form = LoginForm()
    #             context = {'message':message, 'form':form}
    #     return render(request, 'registration/login.html', context)

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # testing
#             email = user_form.cleaned_data['email']
#             split = email.split('@')
#             username = split[0]
#             #print(f'the email is {email} and the split is {split} and username is {username}')
#             # end testing
#             new_user.username = username
#             # Save the User object
#             new_user.save()
#             return render(request,'registration/register_done.html',{'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#         return render(request,'registration/register.html',{'user_form': user_form})