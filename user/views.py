from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import User as models_user
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdateForm

from post import models


def main(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return HttpResponseRedirect(reverse('post:feed'))
        else:
            return render(request, 'user/main.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('post:feed'))

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
                return HttpResponseRedirect(reverse('post:feed'))

        return render(request, 'user/main.html')


@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'user/main.html')


@login_required
def profile_detail(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            user = get_object_or_404(models_user, pk=request.user.id)
            posts = models.Post.objects.filter(author=user)
            return render(request, 'user/profile_detail.html', {'user': user, "posts": posts})


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필 업데이트 완료')
            return redirect('user:profile_detail')
    return render(request, 'user/profile_update.html')
