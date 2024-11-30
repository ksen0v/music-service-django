from django.db import models

# Create your models here.
class Account(models.Model):
    login = models.CharField(max_length=127, unique=True, db_index=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    access = models.ForeignKey('AccessLevel', on_delete=models.PROTECT)

class AccessLevel(models.Model):
    level = models.CharField(max_length=127, unique=True, db_index=True)

    def __str__(self):
        return self.level

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=MusicTrack.STATUS.PUBLISHED)

class MusicTrack(models.Model):

    # Enum, характерирузующий состояния треков
    class Status(models.IntegerChoices):
        UNRELEASED = 0, 'НЕОПУБЛИКОВАННЫЙ'
        PUBLISHED = 1, 'Опубликовано'

    name = models.CharField(max_length=255) # название трека
    author = models.CharField(max_length=255) # автор трека
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT) # foreing key на таблицу с жанрами
    time_created = models.DateTimeField(auto_now_add=True) # время создания трека
    time_updated = models.DateTimeField(auto_now=True) # релизное время - время изменения трека
    logo = models.ImageField(upload_to='music-logo', null=True, blank=True)
    mp3 = models.FileField(upload_to='music-mp3', null=True, blank=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.UNRELEASED) # status публикации трека

    # Менеджеры моделей
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f'{self.name} {self.author}'

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']), # сортировка по новизне публикации
        ]


class Genre(models.Model):
    genre = models.CharField(max_length=127, unique=True, db_index=True)
    slug = models.SlugField(max_length=127, unique=True, db_index=True)

    def __str__(self):
        return self.genre