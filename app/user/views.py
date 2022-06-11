from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from .forms import SignupForm


# Create your views here.
def user_create(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.signup()
            login(request, user)
            return redirect('main.html')
    else:
        form = SignupForm()

        context = {
            'form': form
        }
        return render(request,'', context)

def user_login(request, user):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passoword']

        user = authenticate(request, username=user, password=password)

        if user is not None:
            login(request, user)
            return redirect('main.html')

        else:
            return redirect('login.html')
    else:
        return render(request, 'login.html')