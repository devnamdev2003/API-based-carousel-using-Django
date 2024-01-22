from rest_framework import serializers
from .models import CarouselItem

class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = ['id','title', 'image_url', 'description']
