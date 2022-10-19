# Generated by Django 3.2.15 on 2022-10-19 09:06

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_shopingcart_shoppingcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientsamount',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[recipes.models.validation_amount], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[recipes.models.validation_time_cooking], verbose_name='Время приготовления, минуты'),
        ),
        migrations.AddConstraint(
            model_name='favoriterecipe',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_favorite'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_shopping_cart'),
        ),
    ]
