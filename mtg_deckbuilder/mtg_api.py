from mtgsdk import Card, Set
import random
from django.http import JsonResponse


# Card List
def get_card_list(request):
    cards = Card.where(page=1) \
                .where(pageSize=50) \
                .all()
    return JsonResponse({'cards': cards})
    # for card in cards:
    #     print(card.name)


# RandomCard
def flava(request):
    flavor =  get_data()
    # flavor = random.choice(['pizza', 'pumpkin spice', 'pomegranate'])  # idk
    return JsonResponse({'flavor': flavor})  

  
def get_data():
    setName = get_set()
    card = get_random_card(setName)
    flava_flav = get_flavor_text(card)
    return flava_flav

def get_set():
    sets = Set.all()
    return random.choice(sets)

def get_random_card(s):
    cards = Card.where(set=s.code) \
                .where(types='creature') \
                .all()
    return random.choice(cards)

# TODO: redo so it always return a card with flavor text, and retries if there is none
def get_flavor_text(card):
    if is_not_null(card):
        return card.flavor
    else:
        return 'sorry, no flavor text'

def is_not_null(card):
    if card.flavor != None:
        return True
    else:
        return False