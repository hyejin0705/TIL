from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm



# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)



@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        if request.user == article.user:    
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)



# from django.http import HttpResponse, HttpResponseForbidden

# @require_POST
# def delete(request, pk):
#     if request.user.is_authenticated:          # 인증되지 않음 (401)
#         article = Article.objects.get(pk=pk)
#         if request.user == article.user:       # 권한이 없음 (403)
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden()
#     return HttpResponse(status=401)



@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
    
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    
    else:
        return redirect('article:index')
    
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk = pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # 저장하지 않고 저장할 인스턴스를 반환.
            # comment = Comment()와 동일한 작업
            comment = comment_form.save(commit=False)
            
            comment.article = article    # 객체 저장.
            comment.user = request.user  # 유저 객체 넣기
            
            comment.save()
            
        return redirect('articles:detail', article.pk)

    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:    
        
        # [1] 첫번째 방법
        # article_pk = comment.article.pk

        # [2] 두번째 방법: 교재 (urls에서 2개의 pk를 동시에 받기)

            comment.delete()
    
    return redirect('articles:detail', article_pk)