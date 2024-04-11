from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer, ArtistUpdateSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArtistUpdateSerializer(artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'delete': f'등록 번호 {artist_pk} 번의 {artist.name}을 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def artist_condition_list(request):
    query_param = request.query_params.get('is_group', False)
    if query_param:
        if query_param == 'True' or query_param == 'true':
            artists = Artist.objects.filter(is_group=True)
        else:
            artists = Artist.objects.filter(is_group=False)
    else:
        artists = Artist.objects.all()
    
    serializer = ArtistSerializer(artists, many=True)


    return Response(serializer.data, status=status.HTTP_200_OK)