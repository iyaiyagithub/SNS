from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


# Create your views here.


def post_views(request):
    """전체 게시글을 보여주는 함수"""
    return render(request, 'post/main.html')


def post_detail(request):
    """게시글 상세보기"""
    pass


@login_required(login_url='')
def write_post(request):
    """게시글을 작성하는 함수"""
    if request.method == 'GET':
        post_form = PostForm()
        return render(request, 'post/write-post.html', {'posts': post_form})

    elif request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            write_post = post_form.save(commit=False)
            write_post.author = request.user
            write_post.save()
            return HttpResponseRedirect(reverse('post:postMain'))


def edit_post(request):
    """게시글을 수정하는 함수"""
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass


def delete_post(request):
    """게시글을 삭제하는 함수"""
