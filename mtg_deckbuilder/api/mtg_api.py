from mtgsdk import Card, Set
import random

def main():
    while True:
        setName = get_set()
        card = get_random_card(setName)
        is_not_null(card)
        flava_flav = get_flavor_text(card)


def get_set():
    sets = Set.all()
    return random.choice(sets)


def get_random_card(s):
    cards = Card.where(types='creature') \
                .where(set=s.name) \
                .all()
    return random.choice(cards)


def get_flavor_text(card):
    return card.flavor


def is_not_null(card):
    if card.flavor != None:
        return True


main()