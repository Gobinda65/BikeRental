from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Bike
# from . models import bikerental
# # Register your models here.
# @admin.register(bikerental)
# class bikerentalAdmin(admin.ModelAdmin):
#     list_display=['username','email','password','conpassword']

@admin.register(Brand)
class AdminCate(admin.ModelAdmin):
    list_display=['brand_name', 'about']

@admin.register(Bike)
class AdminBike(admin.ModelAdmin):
    def BImg(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.b_img.url))
    
    list_display=['bike_title', 'bike_model', 'brand', 'overview', 'p_p_day', 'abs', 'ftype', 'b_break', 'reg', 'BImg']
