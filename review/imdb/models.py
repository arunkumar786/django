from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Movie(models.Model):
    movieName = models.CharField(max_length=200)
    movieRating = models.FloatField()
    movieReview = models.TextField()
    comments = models.TextField()
    def __str__(self):
        return self.movieName

class Review(models.Model):
    review = models.ForeignKey(Movie)

class Rating(models.Model):
    rating = models.ForeignKey(Movie)
    
class createSuperUser(BaseUserManager):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    