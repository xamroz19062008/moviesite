from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'films/index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'films/movie.html', {'movie': movie})
