from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies') # models.PROTECT significa que não é possível apagar o gênero se houver filmes relacionados a ele
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies') # models.ManyToManyField significa que um filme pode ter vários atores e um ator pode atuar em vários filmes
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
