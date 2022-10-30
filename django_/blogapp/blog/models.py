from distutils.command.upload import upload
from enum import unique
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True,
                            db_index=True, null=False, editable=False)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    img_url = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
