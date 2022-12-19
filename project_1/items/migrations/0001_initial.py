# Generated by Django 4.1.3 on 2022-12-16 02:01

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
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2)])),
                ('category', models.CharField(choices=[('animals', 'Animals'), ('real_estate', 'Real Estate'), ('babies', 'Babies'), ('house_garden', 'House and garden'), ('vehicles', 'Vehicles'), ('electronics', 'Electronics')], max_length=12)),
                ('description', models.TextField(max_length=200, validators=[django.core.validators.MinLengthValidator(15)])),
                ('condition', models.CharField(default='used', max_length=4)),
                ('location', models.CharField(blank=True, max_length=45, validators=[django.core.validators.MinLengthValidator(3), project_1.core.my_validators.validate_location])),
                ('phone', models.CharField(blank=True, max_length=10, validators=[project_1.core.my_validators.validate_phone])),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items_photos')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='items.item')),
            ],
        ),
    ]
