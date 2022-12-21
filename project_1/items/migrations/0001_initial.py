# Generated by Django 4.1.3 on 2022-12-21 03:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import project_1.core.my_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2)])),
                ('is_favourite', models.BooleanField(default=False)),
                ('image_main', models.ImageField(default='defaults/no-img.png', upload_to='items_photos_mains')),
                ('description', models.TextField()),
                ('is_new', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=60, validators=[django.core.validators.MinLengthValidator(2), project_1.core.my_validators.validate_location])),
                ('phone', models.CharField(blank=True, max_length=10, validators=[project_1.core.my_validators.validate_phone])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.category')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='items_photos')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
