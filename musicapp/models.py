from django.contrib.auth.models import AbstractUser
from django.db import models

# Enum, характерирузующий состояние трека/плейлиста
class Status(models.IntegerChoices):
    UNRELEASED = 0, 'НЕОПУБЛИКОВАННЫЙ'
    PUBLISHED = 1, 'ОПУБЛИКОВАННЫЙ'

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_logo', blank=True, null=True)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=MusicTrack.STATUS.PUBLISHED)

class MusicTrack(models.Model):

    # Enum, характерирузующий состояния
    class Status(models.IntegerChoices):
        UNRELEASED = 0, 'НЕОПУБЛИКОВАННЫЙ'
        PUBLISHED = 1, 'ОПУБЛИКОВАННЫЙ'

    name = models.CharField(max_length=255) # название трека
    author = models.CharField(max_length=255) # автор трека
    genre = models.CharField(max_length=255) # foreing key на таблицу с жанрами
    time_created = models.DateTimeField(auto_now_add=True) # время создания трека
    time_updated = models.DateTimeField(auto_now=True) # релизное время - время изменения трека
    logo = models.ImageField(upload_to='media/',blank=False, null=True)
    mp3 = models.FileField(upload_to='media/', blank=True, null=True)
    mp3_link = models.CharField(max_length=255,blank=True,null=True)
    lyrics = models.TextField(blank=True,null=True)
    duration = models.CharField(default=0, max_length=32)
    is_published = models.BooleanField(choices=Status.choices, default=Status.UNRELEASED) # status публикации трека
    paginate_by = 2

    # Менеджеры моделей
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created']), # сортировка по новизне публикации
        ]


class Genre(models.Model):
    genre = models.CharField(max_length=127, unique=True, db_index=True)
    slug = models.SlugField(max_length=127, unique=True, db_index=True, default='default-musictrackslug')

    def __str__(self):
        return self.genre

class Playlist(models.Model):
    name = models.CharField(max_length=255) # название плейлиста
    author = models.CharField(max_length=255) # автор плейлиста
    genre = models.CharField(max_length=255)
    tracks = models.ManyToManyField(MusicTrack, related_name='playlists', blank=True) # треки, хранящиеся в плейлисте
    time_created = models.DateTimeField(auto_now_add=True)  # время создания плейлиста
    time_updated = models.DateTimeField(auto_now=True)  # релизное время - время изменения плейлиста
    logo = models.ImageField(upload_to='playlists/', blank=False, null=True)
    lyrics = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.UNRELEASED)  # status публикации альбома
    paginate_by = 3

    def __str__(self):
        return f'{self.name} - {self.author}'

    class Meta:
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created']),  # Индекс по дате создания
        ]