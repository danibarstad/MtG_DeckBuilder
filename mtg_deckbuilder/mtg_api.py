from mtgsdk import Card, Set
import random, requests
from django.http import JsonResponse


def flava(requests):
    # get_data()
    flavor = random.choice(['pizza', 'pumpkin spice', 'pomegranate'])  # idk
    return JsonResponse({'flavor': flavor})  
  
def get_data():
    setName = get_set()
    card = get_random_card(setName)
    flava_flav = get_flavor_text(card)
    # print(flava_flav)
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
        return 'sorry'


def is_not_null(card):
    if card.flavor != None:
        return True
    else:
        return False


if __name__ == "__main__":
    flava(requests)