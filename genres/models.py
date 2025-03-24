from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return the string representation of the Genre, which is its name."""
        return self.name