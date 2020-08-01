from django.urls import path
from . import views, views_decks, views_cards, mtg_api


urlpatterns = [

    path('', views.homepage, name='homepage'),

    # Decks
    path('', views_decks.deck_list, name='deck_list'),
    path('decks/detail/<int:deck_pk>/', views_decks.deck_detail, name='deck_detail'),
    path('decks/add/', views_decks.new_deck, name='new_deck'),

    # API
    path('flavor_text/', mtg_api.flava, name='get_flavor_text'),

    # Cards
    path('card_list/', views_cards.card_list, name='card_list'),
    path('save_card_list/', views_cards.save_user_card_list, name='save_card_list')
]