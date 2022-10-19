from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models

from foodgram.settings import min_time, min_amount
from users.models import User

def validation_time_cooking(value):
    if value < min_time:
        raise ValidationError(
            f'Время приготовления не меньше {min_time} минуты'
        )
    return value

def validation_amount(value):
    if value < min_amount:
        raise ValidationError(
            f'Как минимум {min_amount} ингредиент'
        )
    return value

class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта'
    )
    image = models.ImageField(
        upload_to='recipes/image',
        verbose_name='Фото рецепта',
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    ingredients = models.ManyToManyField(
        'IngredientsAmount',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='recipes',
        verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления, минуты',
        validators=[validation_time_cooking],
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Тег',
    )
    color = ColorField(
        max_length=7,
        verbose_name='Цветовой код',
    )
    slug = models.SlugField(
        unique=True,
        max_length=200,
        verbose_name='Слаг тега',
    )

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Ингредиент',
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единица измерения',
    )

    def __str__(self):
        return self.name

class IngredientsAmount(models.Model):
    name = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name='Ингрединты',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[validation_amount],
    )

    def __str__(self):
        return f'{self.name} - {self.amount}'

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Подписчик',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Рецепт',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe',), name='unique_favorite')]

    def __str__(self):
        return f'{self.user} - {self.recipe}'

class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_cart',
        verbose_name='Покупатель',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_cart',
        verbose_name='Рецепт',
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe',), name='unique_shopping_cart')]

    def __str__(self):
        return f'{self.user} - {self.recipe}'
