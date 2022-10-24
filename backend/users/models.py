from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models



class User(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
    )
    username = models.CharField(
        'Никнайм',
        max_length=150,
        unique=True,
        validators=(
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
            ),
        )
    )
    first_name = models.CharField(
        'Фамилия',
        max_length=150,
    )
    last_name = models.CharField(
        'Имя',
        max_length=150,
    )

    def __str__(self):
        return self.username

class Follower(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор рецепта',
    )
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author',),
                name='unique_subscribe'
            ),
        )

    def __str__(self):
        return (f'{self.user} following {self.author}')