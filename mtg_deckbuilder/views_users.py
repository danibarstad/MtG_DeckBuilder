from django.shortcuts import render, redirect

from .models import Deck
from .forms import UserRegistrationForm, EditProfileForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# User Profile
def user_profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    userdecks = Deck.objects.filter(user=user.pk)

    editable = False
    if request.user.is_authenticated and request.user == user:
        editable = True     # Only allow a user to edit their own profiles

    return render(request, 'mtg_deckbuilder/users/user_profile.html', {'user' : user , 'decks' : userdecks })


@login_required
def my_user_profile(request):
    return redirect('user_profile', user_pk=request.user_pk)


# Users can edit their own profile
@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_pk=request.user.pk)
        else:
            message = 'Please check the changes you entered'
            args = {'form': form, 'message': message}
            return render(request, 'mtg_deckbuilder/users/edit_user_profile.html', args)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'mtg_deckbuilder/users/edit_user_profile.html', args)


# Users can edit their password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed!')
            return redirect('user_profile', user_pk=request.user.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        args = { 'form' : form }
        return render(request, 'mtg_deckbuilder/users/change_password.html', args)


# Register new user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('my_user_profile')
        else:
            message = 'Please check the data you entered'
            args = { 'form' : form , 'message' : message }
            return render(request, 'registration/register.html', args)
    else:
        form = UserRegistrationForm()
        args = { 'form' : form }
        return render(request, 'registration/register.html', args)