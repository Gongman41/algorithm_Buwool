from django.urls import path
from . import views


urlpatterns = [
    path('libraries/',views.libraries_list),
    path('libraries/<int:libraries_pk>/',views.libraries_detail)
]