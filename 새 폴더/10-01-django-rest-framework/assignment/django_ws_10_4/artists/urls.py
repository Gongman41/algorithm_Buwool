from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.artist_list_or_create),
    path('artists/<int:artist_pk>/', views.artist_detail),
]
