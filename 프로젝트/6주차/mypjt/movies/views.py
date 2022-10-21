from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    
    else:
        form = MovieForm()

    context = {
        'form': form,
    }

    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()

    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'movies/detail.html', context)


