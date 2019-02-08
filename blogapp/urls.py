from django.urls import path
from .import views

urlpatterns = [
    
    #http://localhost:8000/blogqpp/1
    path('',views.movies_list,name='blogapp_home'),
    path('<int:movie_pk>',views.movie_detail,name = 'movie_detail'),
    path('type/<int:movie_type_pk>',views.movie_type_list,name = 'movie_type_list'),
    

]