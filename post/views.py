from django.shortcuts import render, get_object_or_404
from .models import Post
from user.models import User as user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post



# Create your views here.


def post_views(request):
    user = request.user.is_authenticated
    if user:
        post_list = Post.objects.order_by('caption')
        return render(request, 'post/main.html', {'posts': post_list})


def post_detail(request, id):
    user = get_object_or_404(user_model, id=request.user.id)
    my_post = Post.objects.get(id=user.id)
    return render(request, 'post/post-detail.html', {'posts': my_post})


@login_required(login_url='')
def write_post(request):
    """게시글을 작성하는 함수"""
    if request.method == 'GET':
        post_form = PostForm()
        return render(request, 'post/write-post.html', {'posts': post_form})

    elif request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            write_post = post_form.save(commit=False)
            write_post.author = request.user
            write_post.save()
            # 어디로 이동해야 하는지 모르겠음
            return HttpResponseRedirect(reverse('post:postMain'))


def edit_post(request):
    """게시글을 수정하는 함수"""
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass


def delete_post(request):
    """게시글을 삭제하는 함수"""
    pass


def post_list(request):
    user = request.user.is_authenticated
    if user:
        post_list = Post.objects
        return render(request, 'post/main.html', {'posts': post_list})


"""피드 페이지 """
def user_feed(request):
    user = request.user.is_authenticated
    if request.method == 'GET':
        if user:
            post_list = Post.objects.all().order_by('-created_at')
            return render(request, 'feed-page.html', {'posts': post_list})
        else:
            return redirect('user/signup.html')


"""마이페이지를 보여주는 함수 이름,프로필,프사,이메일"""
def mypage_view(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            user_infoes = user_model.objects.get(id=id)
            return render(request,'user/profile',{"user_infoes": user_infoes})
        else:
            return redirect('user/signup.html')
        
    