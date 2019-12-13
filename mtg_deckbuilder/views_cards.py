from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed

# View that gets all the possible cards and returns a response using a template 
def card_list(request):
    cards = [{'name': 'cat'}, {'name': 'dog'}, {'name': 'bird'} ]  # Todo get actual data
    deck_id = 42  # Figure out what this is 
    return render(request, 'mtg_deckbuilder/card_list.html', {'cards': cards, 'deck_id': deck_id})
    

# JSON API type view. JavaScript will make requests to this view
def save_user_card_list(request):
    if request.method == 'POST':
        user_choices = json.loads(request.body)
        deck_id = user_choices.get('deck_id')
        #  user_choice = { 'cards': ["bird", "dog"] }
        # user choice is a python object send by client-side javascript
        # TODO save that to your database 
        print(user_choices)
        print(deck_id)
        return JsonResponse({ 'message': 'ok!' })
    else:
        return HttpResponseNotAllowed('no')
        # Return HTTPForbidden 
        # Not a vali(d type of request
        # Only POST requests should modify databases on serve.
