from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm


def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index')) # 메인 화면으로

        else:
            return render(request, 'users/main.html')


def signup(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:index')) # 메인화면으로
        return render(request, 'users/login.html')
