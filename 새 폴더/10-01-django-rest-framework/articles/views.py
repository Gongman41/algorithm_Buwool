from rest_framework.response import Response
from rest_framework.decorators import api_view
from  .models import Article
from .Serializers import ArticleListSerializer,ArticleSerializer
from rest_framework import status
@api_view(['GET','POST'])
# DRF 규칙
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        # 직렬화안하면 다른 플랫폼에서 사용 불가
        # serialize 대상이 queryset인 경우 입력
        return Response(serializer.data)
        # 실제 데이터 추출
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            # 모델폼에서 썻던 거랑 이름만 똑같음
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
    
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # partial 넣으면 부분적으로 수정가능
        if serializer.is_valid():
            # raise_exception 유효성 검사 못하면 예외바ㅓㄹ생. 막줄 필요없어짐.
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
# postman ㅜpost 보낼 때 body에서
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
