from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

UserModel = get_user_model()


class Category(MPTTModel):
    title = models.CharField(unique=True, max_length=20)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Message(models.Model):  # refresh when new message arrives
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_of_publication = models.DateField(auto_now=True)

# class Favorite()
#    pass

# class Comment():
