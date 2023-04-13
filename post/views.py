from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from user.models import User as user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.


def post_views(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            posts = Post.objects.order_by('-id')
            return render(request, 'post/main.html', {'posts': posts})


def post_detail(request, id):
    user = get_object_or_404(user_model, id=request.user.id)
    my_post = Post.objects.get(id=user.id)
    return render(request, 'post/post-detail.html', {'posts': my_post})


@login_required(login_url='')
def write_post(request):
    """게시글을 작성하는 함수"""
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'post/write-post.html', {'form': form})

    elif request.method == 'POST':
        user = get_object_or_404(user_model, pk=request.user.id)
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            write_post = post_form.save(commit=False)
            write_post.author = user
            write_post.save()
            return redirect('post:feed')
        else:
            return redirect('user:signup')


@login_required(login_url='')
def edit_post(request, id):
    """게시글을 수정하는 함수"""
    edit_post = Post.objects.get(id=id)
    current_edit_post = edit_post.id

    if request.method == 'GET':
        return render(request, 'post/write-post.html', {'edit-post': edit_post})

    elif request.method == 'POST':
        edit_post.caption = request.POST.get("edit_post_caption", "")
        edit_post.image = request.POST.get("edit_post_image", "")
        edit_post.save()
        return redirect('/edit-post/'+str(current_edit_post))


@login_required(login_url='')
def delete_post(request, id):
    """게시글을 삭제하는 함수"""
    delete_post = Post.objects.get(id=id)
    current_delete_post = delete_post.id
    delete_post.delete()
    return redirect('/delete-post/'+str(current_delete_post))


"""피드 페이지 """


def user_feed(request):
    user = request.user.is_authenticated
    if request.method == 'GET':
        if user:
            post_list = Post.objects.all().order_by('-id')
            return render(request, 'post/main.html', {'posts': post_list})
        else:
            return redirect('user/signup.html')
        # d


"""마이페이지를 보여주는 함수 이름,프로필,프사,이메일"""


def mypage_view(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            user_infoes = user_model.objects.get(id=id)
            return render(request, 'user/profile', {"user_infoes": user_infoes})
        else:
            return redirect('user/signup.html')


def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            search_keyword = request.GET.get("q", "")
            posts = Post.objects.filter(caption__contains=search_keyword)

            return render(request, 'post/main.html', {'posts': posts})