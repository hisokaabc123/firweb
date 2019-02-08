from django.db import models
from django.contrib.auth.models import User



class movie_type(models.Model):
     type_name=models.CharField(max_length=20)

     def __str__(self):
          return self.type_name


class movie(models.Model):
     title = models.CharField(max_length=20)
     type_name = models.ForeignKey(movie_type,on_delete=models.DO_NOTHING)
     content = models.TextField()
     author = models.ForeignKey(User,on_delete = models.DO_NOTHING)
     screen_time = models.DateField(auto_now_add=True)
     exceed_time = models.DateField(auto_now = True)

     def __str__(self):
          return "<Movie: %s>" % self.title

     class Meta:
          ordering = ['screen_time']
