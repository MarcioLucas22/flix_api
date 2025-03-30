from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality')

    class Meta:
        model = Actor
        fields = '__all__'