from django.contrib.auth import get_user_model
from django.db import models

from project_1.items.models import Item

UserModel = get_user_model()


class Favourite(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Favourite of {self.user} to {self.item}'
