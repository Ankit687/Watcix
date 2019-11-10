from django.db import models


class movies(models.Model):
    Uploader_name = models.CharField(max_length=50)
    Name_of_movie = models.CharField(max_length=50)
    Genre_of_movie = models.TextField()
    Duration_of_movie = models.IntegerField(default=1000)
    Rating = models.IntegerField(default=10)
    Thumbnail = models.ImageField(upload_to='movies/Images')
    Video_clip = models.FileField(upload_to='movies')


class webSeries(models.Model):
    Uploader_name = models.CharField(max_length=50)
    Name_of_webSeries = models.CharField(max_length=50)
    Genre_of_webSeries = models.TextField()
    Number_of_Seasons = models.IntegerField(default=20)
    Number_of_each_season_episode = models.IntegerField(default=20)
    Duration_of_each_episode = models.IntegerField(default=30)
    Rating = models.IntegerField(default=10)
    Thumbnail = models.ImageField(upload_to='webSeries/Images')
    Video_clip = models.FileField(upload_to='webSeries')
