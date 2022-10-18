# Generated by Django 2.2.19 on 2022-10-14 18:50

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import recipes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ингредиент')),
                ('measurement_unit', models.CharField(max_length=200, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientsAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название рецепта')),
                ('image', models.ImageField(upload_to='recipes/image', verbose_name='Фото рецепта')),
                ('text', models.TextField(verbose_name='Описание рецепта')),
                ('cooking_time', models.IntegerField(validators=[recipes.models.validation_time_cooking], verbose_name='Время приготовления, минуты')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тег')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=7, samples=None, verbose_name='Цветовой код')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Слаг тега')),
            ],
        ),
        migrations.CreateModel(
            name='ShopingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_cart', to='recipes.Recipe', verbose_name='Рецепт')),
            ],
        ),
    ]
