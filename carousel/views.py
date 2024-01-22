from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from .models import CarouselItem
from .serializers import CarouselItemSerializer


def carousel_view(request):
    return render(request, 'carousel/index.html')


def carousel_Form_view(request):
    return render(request, 'carousel/form.html')


def carousel_update_delete(request):
    return render(request, 'carousel/list.html')


def carousel_update(request, pk):
    return render(request, 'carousel/update.html')


class CarouselItemList(generics.ListCreateAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CarouselItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer
    lookup_field = 'pk'  # Use 'id' as the lookup field
