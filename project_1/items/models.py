from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.utils.safestring import mark_safe

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from project_1.core.my_validators import validate_location, validate_phone

# ITEMS MODELS
UserModel = get_user_model()


class Category(MPTTModel):
    title = models.CharField(unique=True, max_length=20)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    # def __str__(self):
    #     return self.title

    def __str__(self):
        full_path = [self.title]
        current_parent = self.parent
        while current_parent is not None:
            full_path.append(current_parent.title)
            current_parent = current_parent.parent
        return '/'.join(full_path[::-1])


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    date_added = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

    # to display image in administration with fake tag
    def get_image(self):
        return mark_safe(f'<img src="{self.image_main.url}" height="60"/>')

    # TODO: SlUG
    # slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.slug:  # change on update or not
    #         self.slug = slugify(f'{self.title}-{self.pk}')
    #     return super().save(*args, **kwargs)


class ItemImage(models.Model):
    image = models.FileField(upload_to='items_photos')
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['pk']
