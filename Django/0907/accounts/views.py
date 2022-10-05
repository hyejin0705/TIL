from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
@require_http_methods(['POST', 'GET'])
def login(request):
    if request.user.is_authenticated:   # 인증된 사용자라면,
        return redirect('articles:index')   # 그냥 기본 페이지로... 

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())     # 로그인

            # 단축평가 : next가 존재하면, next로 없으면 index로
            return redirect(request.GET.get('next') or 'articles:index')

    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    # 로그아웃
    auth_logout(request)
    
    return redirect('articles:index')


@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()

            # 회원가입 후 로그인
            auth_login(request, user)

            return redirect('articles:index')
    
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)    # 세션에서도 나가기(로그아웃)
    return redirect('articles:index')


@login_required
@require_http_methods(['POST', 'GET'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['POST', 'GET'])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)  # 선택인자, 데이터
        if form.is_valid():
            form.save()
            
            # 유저정보 가져오는 2가지 방법
            # 1. 변수설정
            # 2. form.user
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')

    else:
        form = PasswordChangeForm(request.user)

    context={
        'form':form,
    }

    return render(request, 'accounts/change_password.html', context)
