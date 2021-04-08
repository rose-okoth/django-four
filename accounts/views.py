from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, logout, login 
# Create your views here.
def signup(request):

    '''User signup function'''

    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            name = request.POST["username"]
            email = request.POST["email"]
            send_welcome_email(name,email)
            # signin(request, user)

            return redirect("accounts:login")

    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:

                login(request, user)
                return redirect('main:home')
            else:
                return render(request, 'login.html', {"error": "Your account id is not active"})

        else:
            return render(request, 'login.html', {"error": "Invalid username or password"})

    return render(request, 'login.html')

    
def user_logout(request):

    '''User logout function'''

    logout(request)
    return redirect('accounts:login')
