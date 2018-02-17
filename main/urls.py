from django.conf.urls import url

from . import views




movie_views = views.MovieViewSet.as_view({
    'get': 'list',
})

artist_views = views.ArtistViewSet.as_view({
    'get': 'list',
})




urlpatterns = [
    url(r'^movies/$', movie_views),
    url(r'^artists/$', artist_views),
]
