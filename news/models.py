from django.urls import reverse
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_page_view", args=[self.name])


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)  # Added unique and db_index
    body = models.TextField()
    img = models.ImageField(upload_to="news/images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_article_view", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email
