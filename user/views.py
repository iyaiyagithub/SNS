from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import User as models_user
from post import models
from post.serializers import PostSerializer
from post.forms import CommentForm
from .forms import SignUpForm
from .forms import UserUpdateForm
from django.contrib import messages


def main(request):
    """로그인 함수"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('post:feed'))

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('post:feed'))

    return render(request, 'user/main.html')


def signup(request):
    """회원가입 함수"""
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
        return render(request, 'user/signup.html', {'form': form})


@login_required
def logout(request):
    """로그아웃 함수"""
    auth.logout(request)
    return render(request, 'user/main.html')


@login_required
def my_posts(request):
    """내가 쓴 글만 보여주는 함수"""
    if request.method == 'GET':
        comment_form = CommentForm()
        user = get_object_or_404(models_user, pk=request.user.id)
        post_list = models.Post.objects.filter(author=user).order_by('-id')
        serializer = PostSerializer(post_list, many=True)

        return render(request, 'post/posts.html', {'posts': serializer.data, 'comment_form': comment_form, 'user': user})


@login_required
def edit_profile(request, user_id):
    """프로필 수정 함수"""
    user = get_object_or_404(models_user, pk=user_id)
    if user:
        # 로그인한 유저가 맞다면
        if request.method == "GET":
            form = UserUpdateForm(instance=user)
            context = {
            'form': form,
            'edit': '수정하기',
        }
            return render(request, 'user/profile_edit.html', context)
        
        elif request.method == "POST":
            forms = UserUpdateForm(request.POST, request.FILES, instance=user)
            if forms.is_valid():
                forms.save()

            return redirect(reverse('post:feed'))

    else:
        # 로그인한 유저와 다르면
        return redirect('post:feed')
