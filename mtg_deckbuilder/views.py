from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck


def homepage(request):
    decks = Deck.objects.all()
    return render(request, 'mtg_deckbuilder/home.html', {'decks': decks})


def deck_detail(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    return render(request, 'decks/deck_detail.html' , {'deck' : deck })