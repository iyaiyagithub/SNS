from django.shortcuts import render, get_object_or_404
from .models import Post
from user.models import User as user_model

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


def write_post(request):
    """게시글을 작성하는 함수"""
    pass


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