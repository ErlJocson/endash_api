from django.urls import path
from .views import *

urlpatterns = [
    path('get-all-cards/', get_all_cards, name='get-all-cards'),
    path('get-card/', get_card, name="get-card"),
    path('add-card/', add_card, name="add-card"),
    path('delete-card/', delete_card, name="delete-card"),
    path('update-card/', update_card, name="update-card"),
]
