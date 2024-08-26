from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
from rest_framework import viewsets
from . serializers import MovieDetailsSerializer

def index(request):
    movies_data = Movies.objects.all().order_by('id')

    movie_name = request.GET.get('movie_name')

    if movie_name:
        movies_data = movies_data.filter(name__icontains=movie_name)

    paginator = Paginator(movies_data, 3)
    page_number = request.GET.get('page')
    movies_paginator = paginator.get_page(page_number)

    return render(request, 'index.html', {'movies_paginator': movies_paginator})


class MovieDetailsViewSet(viewsets.ModelViewSet):
    queryset =Movies.objects.all()
    serializer_class = MovieDetailsSerializer

class MovieComedyViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.filter(genere = 'Comedy')
    serializer_class = MovieDetailsSerializer

class MoviePsychologicalDramaViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.filter(genere = 'Psychological Drama')
    serializer_class = MovieDetailsSerializer

class MovieActionViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.filter(genere = 'Action')
    serializer_class = MovieDetailsSerializer