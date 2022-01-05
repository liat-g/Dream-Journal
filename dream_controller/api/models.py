from django.db import models
import string
import random
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings

User = settings.AUTH_USER_MODEL
# added the code above bc I was getting errors with the fk 'user'

# this is not my coce


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
# put most of your info on the models
# add a picture url field for users model so they can have a random pixel icon
# is_dreamer, is_star_gazer, is_romantic as custom fields based on the number of journals a user has


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

# this is not my code


# is_draft to determined whether the post is posted or is a draft


class Journal(models.Model):
    title = models.CharField(
        max_length=100, default="Icing toffee soufflé fruitcake sweet. Cupcake cupcake tootsie roll sweet tootsie roll chocolate.")
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)

    class JournalRating(models.TextChoices):
        FANTASY = 'FA', _('Fantasy')
        DAYDREAM = 'DA', _('Daydream')
        VISION = 'VI', _('Vision')
        ILLUSION = 'IL', _('Illusion')
        NIGHTMARE = 'NM', _('Nightmare')

    journal_rating = models.CharField(
        max_length=2,
        choices=JournalRating.choices,
        default=JournalRating.VISION,
        blank=False
    )

    def _str_(self):
        return self.title

# is_approved so comments must be approved before they are public or something idk, this would be something for machine learning to handle as well


class User(AbstractUser):
    is_dreamer = models.BooleanField(default=True)
    # journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def _str_(self):
        return self.username


class Comment(models.Model):
    # commented_on = models.ForeignKey(Journal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def _str_(self):
        return self.created_at
