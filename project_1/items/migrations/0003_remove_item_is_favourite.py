# Generated by Django 4.1.3 on 2022-12-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_favourite',
        ),
    ]