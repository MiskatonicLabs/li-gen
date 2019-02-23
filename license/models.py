from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<License: {str(self)}>'


class License(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    text = models.TextField()
    details = models.URLField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.category.name}-{self.title}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category.name} {self.title}'

    def __repr__(self):
        return f'<License: {str(self)}>'
