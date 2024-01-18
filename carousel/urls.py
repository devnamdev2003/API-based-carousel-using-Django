# carousel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.carousel_view, name='carousel'),
    path('form/', views.carousel_Form_view, name='carousel'),
    path('api/', views.CarouselItemList.as_view(), name='carousel-item-list'),
]
