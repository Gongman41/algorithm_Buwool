from django.urls import path
from . import views


urlpatterns = [
    path('articles',views.article_list),
    path('articles/<int:article_pk>',views.article_detail)
]
# 탬플릿을 제공하지 않기때문에 잡다한놈들 필요없
