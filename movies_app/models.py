from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DecimalField(max_digits=3, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to="movie_images")
    genere = models.CharField(max_length=100)


    def __str__(self):
        return self.name