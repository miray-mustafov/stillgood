# Generated by Django 4.1.3 on 2022-12-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='condition',
        ),
        migrations.AddField(
            model_name='item',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
