from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdateForm


def main(request):
    if request.method == 'GET':
        return render(request, 'user/main.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('post:main'))

        else:
            return render(request, 'user/main.html')


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()

        return render(request, 'user/signup.html', {'form': form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('post:main'))

        return render(request, 'user/main.html')


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:login'))


@login_required
def profile_detail(request):
    user = request.user
    return render(request, 'user/profile_detail.html', {'user': user})


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필 업데이트 완료')
            return redirect('user:profile_detail')
    return render(request, 'user/profile_update.html')
