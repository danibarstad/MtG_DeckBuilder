from django.shortcuts import render, redirect, get_object_or_404
import mtg_api


def card_list(request):
    if request.method == 'POST':
        card_list = mtg_api.get_card_list

        pass