from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    message = 'A avaliação deve ser entre 0 e 5'

    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, message), 
            MaxValueValidator(5, message)
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title