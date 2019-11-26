from django.shortcuts import render


def homepage(request):
    return render(request, 'mtg_deckbuilder/home.html')