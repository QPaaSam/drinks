from django.urls import path
from .views import drink_list, drink_detail

urlpatterns = [
    path('drinks/', drink_list, name='list'),
    path('drinks/<int:id>', drink_detail, name='detail'),
]


