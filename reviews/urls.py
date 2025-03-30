from django.urls import path
from reviews.views import ReviewsCreateListView, ReviewsRetrieveUpdateDestroyView

urlpatterns = [
    path('reviews/', ReviewsCreateListView.as_view(), name='movie-create-list'),
    path('reviews/<int:pk>/', ReviewsRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy'),
]