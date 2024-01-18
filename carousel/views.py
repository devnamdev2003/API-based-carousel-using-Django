# carousel/views.py

from rest_framework import status
from rest_framework.response import Response
from .serializers import CarouselItemSerializer
from rest_framework import generics
from django.shortcuts import render
from .models import CarouselItem


def carousel_view(request):
    return render(request, 'carousel/index.html')

def carousel_Form_view(request):
    return render(request, 'carousel/form.html')


class CarouselItemList(generics.ListCreateAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
