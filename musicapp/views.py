import json

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q

from core import settings

from musicapp.models import MusicTrack, Playlist
from django.core.paginator import Paginator
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request, template_name='404.html', status=404)

def home(request):
    paginator = Paginator(MusicTrack.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    genres_for_playlists = ['Russian Rap', 'Rap']
    playlists_by_genre = {genre: Playlist.objects.filter(genre=genre, is_published=MusicTrack.Status.PUBLISHED) for genre in genres_for_playlists}

    genres = ['Russian Rap', 'Rap', 'Russian Rock', 'Rock']
    tracks_by_genre = {genre: MusicTrack.objects.filter(genre=genre, is_published=MusicTrack.Status.PUBLISHED) for genre in genres}

    context = {
        'page_obj': page_obj,
        'tracks_by_genre': tracks_by_genre,
        'playlists_by_genre': playlists_by_genre,
        'marker': 'playlists'
    }

    return render(request, "player.html", context)

def show_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    tracks = playlist.tracks.all()

    paginator = Paginator(tracks, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'playlist': playlist,
        'tracks': tracks,
        'marker': 'playlist_page',
        'page_obj': page_obj,
    }
    return render(request, 'player.html', context)

def open_search_page(request):
    context = {
        'marker': 'search_page',
    }
    return render(request, 'player.html', context)

def search(request):
    query = request.GET.get('query', '').strip()

    tracks = MusicTrack.objects.filter(name__icontains=query) | MusicTrack.objects.filter(author__icontains=query)

    paginator = Paginator(tracks, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print(f"tracks: {tracks}")

    context = {
        'tracks': tracks,
        'marker': 'search_page',
        'page_obj': page_obj,
    }

    return render(request, 'player.html', context)

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile_page.html'
    extra_context = {
        'default_photo': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

def logout_view(request):
    logout(request)
    return redirect('/')