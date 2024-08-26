from django.urls import path, include
from . import views
from . views import MovieDetailsViewSet, MovieComedyViewSet, MoviePsychologicalDramaViewSet, MovieActionViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('all_movies', MovieDetailsViewSet, basename = 'all_movies')
router.register('comedy_movies',MovieComedyViewSet, basename = 'comedy_movies')
router.register('psychological_drama_movies', MoviePsychologicalDramaViewSet, basename = 'psychological_drama')
router.register('action_movies', MovieActionViewSet, basename = 'action_movies')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls))
]