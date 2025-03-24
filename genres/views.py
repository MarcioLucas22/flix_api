from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
import json


@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data['name']
        genre = Genre(name=name)
        genre.save()

        return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)
        