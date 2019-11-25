from django.urls import path
from . import views, views_decks, views_users

urlpatterns = [

    path('', views.homepage, name='homepage'),

    # Decks
    path('', views_decks.deck_list, name='deck_list'),

    # Users
    path('user/profile/<int:user_pk>/', views_users.user_profile, name='user_profile'),
    path('user/profile/', views_users.my_user_profile, name='my_user_profile'),
    path('user/profile/edit', views_users.edit_user_profile, name='edit_user_profile'),
    path('user/password/', views_users.change_password, name='change_password')
]