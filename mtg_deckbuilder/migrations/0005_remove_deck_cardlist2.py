# Generated by Django 3.0 on 2019-12-19 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_deckbuilder', '0004_auto_20191219_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='cardList2',
        ),
    ]