from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title',)


class ArtistSerializer(serializers.ModelSerializer):

    musics = MusicListSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='musics.count', read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics', 'music_count',)

      
class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title', 'artist',)
        read_only_fields = ('artist',)