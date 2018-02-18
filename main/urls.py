from django.conf.urls import url

from . import views



movie_views = views.MovieViewSet.as_view({
    'get': 'list',
})


urlpatterns = [
    url(r'^movies/$', movie_views),
]
