from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck
from .forms import NewDeckForm
from django.http import HttpResponseForbidden

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def deck_list(request):

    """If this is a POST request, the user clicked the Add button
    in the form. Check if the new deck is valid, if so, save a 
    new Deck to the database, and redirect to this same page.
    This creates a GET request to this same route

    If not a POST route, or Deck is not valid, display a page with
    a list of decks and a form to add a new deck.
    """

    if request.method =='POST':
        form = NewDeckForm(request.POST)
        deck = form.save()      # Create a new Deck from the form
        if form.is_valid():     # Checks agains DB constraints, for examples, are required fields present?
            deck.save()         # Saves to the database
            return redirect('deck_list')    # redirects to GET view with name deck_list - which is the same view


    # If not a POST, or the form is not valid, render the page
    # with the form to add a new deck, and list of decks
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


# help from Stack Overflow
# https://stackoverflow.com/questions/1854237/django-edit-form-based-on-add-form
@login_required
def edit_deck(request, deck_pk):
    if deck_pk:
        deck = get_object_or_404(Deck, pk=deck_pk)
        if deck.user != request.user:
            return HttpResponseForbidden()
    else:
        deck = Deck(user=request.user)
    
    form = NewDeckForm(request.POST or None, instance=deck)
    if request.POST and form.is_valid():
        form.save()

        return redirect('deck_detail', deck_pk=deck.pk)
    
    return render(request, 'mtg_deckbuilder/decks/edit_deck.html', {'form':form})