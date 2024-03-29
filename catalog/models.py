from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from lbrary2.settings import AUTH_USER_MODEL


class LiteraryFormat(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Author(AbstractUser):
    pseudonym = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return f"{self.username} : {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(LiteraryFormat, on_delete=models.CASCADE, related_name="books")  # MANY TO ONE
    authors = models.ManyToManyField(AUTH_USER_MODEL, related_name="books")

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f"{self.title} , {self.price} , {self.format.name} "

    def get_absolute_url(self):
        return reverse("catalog:book-detail", args=[str(self.id)])
