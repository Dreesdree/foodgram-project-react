# Generated by Django 3.2.15 on 2022-10-19 20:16

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[users.models.validation_color], verbose_name='Никнайм'),
        ),
    ]