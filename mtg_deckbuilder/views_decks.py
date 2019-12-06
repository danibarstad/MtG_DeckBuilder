from django.shortcuts import render, redirect
from .models import Deck
from .forms import NewDeckForm

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