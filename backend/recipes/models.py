from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from foodgram.settings import MIN_TIME, MIN_AMOUNT
from users.models import User

def validation_time_cooking(value):
    if value < MIN_TIME:
        raise ValidationError(
            f'Время приготовления не меньше {MIN_TIME} минуты'
        )
    return value

def validation_amount(value):
    if value < MIN_AMOUNT:
        raise ValidationError(
            f'Как минимум {MIN_AMOUNT} ингредиент'
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
        validators=(validation_time_cooking,),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Тег',
    )
    color = ColorField(
        unique=True,
        max_length=7,
        verbose_name='Цветовой код',
        validators=(
            RegexValidator(
                regex=r'^#[\w]{1,8}$',
            ),
        ),
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
        related_name='ingredient_amount',
        verbose_name='Ингрединты',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=(validation_amount,),
    )

    def __str__(self):
        return f'{self.name} - {self.amount}'

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='added_to_favorite',
        verbose_name='Подписчик',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='added_to_favorite',
        verbose_name='Рецепт',
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe',), name='unique_favorite'),)

    def __str__(self):
        return f'{self.user} - {self.recipe}'

class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_added_to_cart',
        verbose_name='Покупатель',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_added_to_cart',
        verbose_name='Рецепт',
    )
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe',), name='unique_shopping_cart')),

    def __str__(self):
        return f'{self.user} - {self.recipe}'
