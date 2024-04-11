from rest_framework.response import Response
from rest_framework.decorators import api_view
from  .models import Book
from .serializers import ArticleListSerializer,ArticleSerializer

@api_view(['GET'])
# DRF 규칙
def libraries_list(request):
    libraries = Book.objects.all()
    serializer = ArticleListSerializer(libraries, many=True)
    # 직렬화안하면 다른 플랫폼에서 사용 불가
    # serialize 대상이 queryset인 경우 입력
    return Response(serializer.data)
    # 실제 데이터 추출
  

@api_view(['GET'])
def libraries_detail(request, libraries_pk):
    libraries = Book.objects.get(pk=libraries_pk)
    serializer = ArticleSerializer(libraries)
    return Response(serializer.data)
     