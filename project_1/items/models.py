from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from project_1.core.my_enums import Categories, Conditions
from project_1.core.my_validators import validate_location, validate_phone

# ITEMS MODELS
UserModel = get_user_model()


class Item(models.Model):
    MAX_LEN_TITLE = 40
    MIN_LEN_TITLE = 2
    MAX_LEN_LOCATION = 60
    MIN_LEN_LOCATION = 2

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        validators=[MinLengthValidator(MIN_LEN_TITLE)],
        blank=False,
    )
    category = models.CharField(
        choices=Categories.choices(),
        max_length=Categories.max_len(),
        blank=False,
    )
    image_main = models.ImageField(upload_to='items_photos_mains', default='defaults/no-img.png')
    description = models.TextField()
    is_new = models.BooleanField(default=False, )
    price = models.IntegerField()
    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        validators=[
            MinLengthValidator(MIN_LEN_LOCATION),
            validate_location],
        blank=True,
    )
    phone = models.CharField(
        max_length=10,
        validators=[validate_phone, ],
        blank=True,
    )
    email = models.EmailField(blank=True, )  # no need to be unique
    date_added = models.DateField(auto_now=True, )

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        ordering = ['pk']


class ItemImage(models.Model):
    image = models.FileField(upload_to='items_photos')
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['pk']
