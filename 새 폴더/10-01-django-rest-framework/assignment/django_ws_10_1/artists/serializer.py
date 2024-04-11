# 재구성할 수 있는 포맷으로 변환하는 과정
from rest_framework import serializers
from .models import Artist

class ArtistListSerializer(serializers.ModelSerializer):
    # 장고의 모델과 연관없으면 일반 serializer 사용
    class Meta:
        model = Artist
        fields = '__all__'

