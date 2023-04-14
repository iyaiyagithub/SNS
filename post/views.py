from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment
from user.models import User as user_model
from . import serializers

from django.http import JsonResponse

# Create your views here.



# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     context = {
#         'post': post,
#     }
#     return render(request, 'post/post-detail.html', context)


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
        edit_form = PostForm(instance=edit_post)
        context = {
            'form': edit_form,
            'edit': '수정하기',
        }
        return render(request, 'post/write-post.html', context)

    elif request.method == 'POST':
        user = get_object_or_404(user_model, pk=request.user.id)
        edit_form = PostForm(request.POST, request.FILES, instance=edit_post)
        if edit_form.is_valid():
            edit_post = edit_form.save(commit=False)
            edit_post.author = user
            edit_post.id = current_edit_post
            edit_post.save()
            return redirect(reverse('post:feed')+ "#post-" + str(edit_post.id))


@login_required(login_url='')
def delete_post(request, id):
    """게시글을 삭제하는 함수"""
    delete_post = Post.objects.get(id=id)
    # current_delete_post = delete_post.id
    delete_post.delete()
    # return redirect('/delete-post/'+str(current_delete_post))
    return redirect('post:feed')


"""피드 페이지 """


@login_required(login_url='')
def user_feed(request):
    if request.method == 'GET':
        comment_form = CommentForm()
        post_list = Post.objects.all().order_by('-id')

        serializer = serializers.PostSerializer(post_list, many=True)
        
        return render(request, 'post/posts.html', {'posts': serializer.data, 'comment_form': comment_form})


"""마이페이지를 보여주는 함수 이름,프로필,프사,이메일"""


def mypage_view(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            user_infoes = user_model.objects.get(id=id)
            return render(request, 'user/profile', {"user_infoes": user_infoes})
        else:
            return redirect('user/signup.html')


@login_required(login_url='')
def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            search_keyword = request.GET.get("q", "")
            comment_form = CommentForm()

            posts = Post.objects.filter(caption__contains=search_keyword)

            serializer = serializers.PostSerializer(posts, many=True)
            return render(request, 'post/posts.html', {'posts': serializer.data, 'comment_form': comment_form})


@login_required(login_url='')
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.posts = post
        comment.save()

        return redirect(reverse('post:feed') + "#comment-" + str(comment.id))
    
    else :
        post_list = Post.objects.all().order_by('-id')
        comment_form = CommentForm()

        return render(request, 'post/posts.html', {'posts': post_list, 'comment_form': comment_form})
        

@login_required(login_url='')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        comment.delete()
    
    return redirect(reverse('post:feed'))


@login_required(login_url='')
def post_like(request, post_id):
    response_body = {"result": ""}

    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        like_user = post.post_likes.filter(pk=request.user.id).exists()
        if like_user:
            post.post_likes.remove(request.user)
            response_body['result'] = 'dislike'
        else:
            post.post_likes.add(request.user)
            response_body['result'] = 'like'

        post.save()
        return JsonResponse(status=200, data=response_body) # https://developer.mozilla.org/ko/docs/Web/HTTP/Status
