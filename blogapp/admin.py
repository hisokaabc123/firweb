from django.contrib import admin
from .models import movie,movie_type
# Register your models here.

@admin.register(movie_type)
class movie_typeAdmin(admin.ModelAdmin):
	list_display = ('id','type_name')

@admin.register(movie)
class movieadmin(admin.ModelAdmin):
	list_display = ('title','type_name','content','author','screen_time','exceed_time')