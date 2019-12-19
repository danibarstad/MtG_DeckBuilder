from mtgsdk import Card, Set
import random
from django.http import JsonResponse


"""
Card List
"""
def get_card_list():
    cards = card_list()
    listOfCards = object_to_list(cards)
    return listOfCards

def card_list():
    """
    FOR TESTING PURPOSES
    cards = Card.where(page=1) \
                .where(pageSize=5) \
                .all()
    """
    # Returns a list of cards from the set named "Khans of Tarkir"
    return Card.where(setName='Khans of Tarkir') \
                .all()

def object_to_list(cardList):
    # Creates a list of only the names from provided Card objects
    cards = []
    for card in cardList:
        cards.append((card.name, card.name))
    return cards



"""
Random Card Flavor Text
"""
def flava(request):
    flavor = get_data()
    return JsonResponse({'flavor': flavor})  
  
def get_data():
    end = False
    while end == False:             # keeps searching until flavor text is not None
        setName = get_set()
        card = get_random_card(setName)
        flava_flav = get_flavor_text(card)
        if is_not_null(flava_flav) == True:
            end = True              # ends the loop when valid flavor text is provided
    return flava_flav

def get_set():
    sets = Set.all()                # Gets a list of all Sets
    return random.choice(sets)      # returns a random Set object

def get_random_card(s):
    # gets a random Card object
    cards = Card.where(set=s.code) \
                .where(types='creature') \
                .all()              # Only 'creature' type cards from the provided Set are searched
    return random.choice(cards)

# TODO: redo so it always return a card with flavor text
#       and retries if there is none
def get_flavor_text(card):
    return card.flavor              # returns the flavor text from the Card object

def is_not_null(flavor):
    if flavor != None:              # returns True if the supplied text is not None
        return True
    else:
        return False