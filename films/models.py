from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='films/')
    background_image = models.ImageField(upload_to='films/', blank=True, null=True)  # Фон
    trailer_url = models.URLField()
    movie_url = models.URLField()

    def __str__(self):
        return self.title
