from rest_framework import serializers
from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name', 'debut_date',)

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'

class ArtistUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('agency', 'is_group')