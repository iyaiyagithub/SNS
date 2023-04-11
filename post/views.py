from django.shortcuts import render

# Create your views here.



def post_views(request):
    """전체 게시글을 보여주는 함수"""
    return render(request, 'post/main.html')


def post_detail(request):
    """게시글 상세보기"""
    pass


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