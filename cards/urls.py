from django.urls import path
from .views import *    

urlpatterns = [
    path('get-all-cards/', get_all_cards_api, name='get-all-cards_api'),
    path('get-card/<int:row_id>', get_card_api, name="get-card_api"),
    path('add-card/', add_card_api, name="add-card_api"),
    path('delete-card/', delete_card_api, name="delete-card_api"),
    path('update-card/', update_card_api, name="update-card_api"),
]
