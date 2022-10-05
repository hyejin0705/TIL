from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 첫 페이지
def index(request):
    article = Article.objects.all()

    context ={
        'articles': article
    }

    return render(request, 'articles/index.html', context)


# 추가할 데이터 받는 페이지
def new(request):
    return render(request, 'articles/new.html')


# 추가
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title = title, content = content)
    article.save()

    return redirect('articles:detail', article.pk)


# 상세페이지
def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context ={
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


# 수정페이지
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)


# 수정
def update(request, pk):
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content

    article.save()

    return redirect('articles:detail', article.pk)


# 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect('articles:index')
    