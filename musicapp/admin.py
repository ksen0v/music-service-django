from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MusicTrack, Playlist

admin.site.register(User, UserAdmin)
admin.site.register(MusicTrack)
admin.site.register(Playlist)