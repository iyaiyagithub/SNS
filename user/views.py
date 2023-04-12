from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import User as user_model


def main(request):
    if request.method == 'GET':
        return render(request, 'user/main.html')

    elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('post:postMain'))

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
                return HttpResponseRedirect(reverse('post:postMain'))


        return render(request, 'user/main.html')
    
    
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:login'))


@login_required
def profile(request, id):
    user = get_object_or_404(user_model, id=request.user.id)
    return render(request, 'user/profile_detail.html', {'user': user})



# 1. 본인 프로필
# 2. post 작성한 프로필