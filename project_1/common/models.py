from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# class Category(MPTTModel)


class Message(models.Model):  # refresh when new message arrives
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_of_publication = models.DateField(auto_now=True)

# class Comment():
# class Favorite()
