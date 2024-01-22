# carousel/admin.py

from django.contrib import admin
from .models import CarouselItem

class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image_url', 'description')
    search_fields = ('title', 'description')

admin.site.register(CarouselItem, CarouselItemAdmin)
