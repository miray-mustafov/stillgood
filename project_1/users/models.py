from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from project_1.core.my_validators import validate_personal_names, validate_location, validate_phone
from project_1.core.my_enums import Genders


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_LOCATION = 45
    MIN_LEN_LOCATION = 3

    personal_photo = models.ImageField(
        upload_to='users_photos',
        blank=False,
        default='defaults/no-user-photo.png',
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_personal_names,
        ),
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_personal_names,
        ),
        blank=True,
    )

    gender = models.CharField(
        choices=Genders.choices(),
        max_length=Genders.max_len(),
        blank=True,
    )

    phone = models.CharField(
        max_length=10,
        validators=(validate_phone,),
        blank=True,
    )
    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LOCATION),
            validate_location),
        blank=True,
    )

    email = models.EmailField(unique=True, blank=False, )

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ['pk']
