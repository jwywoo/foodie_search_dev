from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm


# Create your views here.
def user_create(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.signup()
            login(request, user)
            return render(request, 'food/main.html', {})
    else:
        form = SignupForm()

        context = {
            'form': form
        }
        return render(request, 'user/user_create.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'food/main.html', {})

        else:
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'food/main.html', {})


# def postsignUp(request):
#     email = request.POST['email']
#     password = request.POST['pass']
#     name = request.POST['name']
#     try:
#         # # creating a user with the given email and password
#         # user = authe.create_user_with_email_and_password(email, password)
#         # uid = user['localId']
#         # idtoken = request.session['uid']
#         # print(uid)
#         pass
#     except:
#         return render(request, "food/main.html")
#     return render(request, "login.html")

