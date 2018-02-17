from django.contrib.auth.models import User, Group
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'budget', 'length', 'imdb_rating', 'imdb_rating_votes')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name')
