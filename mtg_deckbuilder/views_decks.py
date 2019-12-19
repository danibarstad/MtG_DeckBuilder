from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck
from .forms import NewDeckForm
from django.http import HttpResponseForbidden

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create a new deck
@login_required
def new_deck(request):

    if request.method == 'POST' :

        form = NewDeckForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('deck_detail', deck_pk=deck.pk)

    else :
        form = NewDeckForm()

    return render(request, 'mtg_deckbuilder/decks/new_deck.html' , { 'form' : form })


# Users can edit their decks.
@login_required
def edit_deck(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'POST':
        form = NewDeckForm(request.POST, instance=deck)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('deck_detail', deck_pk=deck.pk)
    else:
        form = NewDeckForm(instance=deck)
    return render(request, 'mtg_deckbuilder/decks/edit_deck.html', {'form': form})


# I started these very early on and messed with them when I didn't know what I was doing
# (i still don't) so I'm not sure if any of these actually need to be here.
# They don't seem to be doing any harm so keeping them for now until I solve that mystery
def deck_list(request):
    if request.method =='POST':
        form = NewDeckForm(request.POST)
        deck = form.save()
        if form.is_valid():
            deck.save()
            return redirect('deck_list')

    decks = Deck.objects.order_by('name')
    new_deck_form = NewDeckForm()
    return render(request, 'mtg_deckbuilder/decks.html', { 'decks': decks, 'new_deck_form': new_deck_form })


def latest_decks(request):
    decks = Deck.objects.all()
    return render(request, 'decks/deck_list.html', {'decks': decks})


def deck_detail(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    cards = [{'name': 'cat'}, {'name': 'dog'}, {'name': 'bird'} ]  # Todo get actual data
    return render(request, 'mtg_deckbuilder/decks/deck_detail.html' , {'deck' : deck, 'cards': cards})