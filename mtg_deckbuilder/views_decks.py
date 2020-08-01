from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck
from .forms import NewDeckForm
from django.http import HttpResponseForbidden


# Create a new deck
def new_deck(request):

    if request.method == 'POST' :

        form = NewDeckForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.save()
            return redirect('deck_detail', deck_pk=deck.pk)

    else :
        form = NewDeckForm()

    return render(request, 'mtg_deckbuilder/decks/new_deck.html' , { 'form' : form })


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