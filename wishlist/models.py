from django.db import models
from django.conf import settings

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    group_pw = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class AppUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class WishList(models.Model):
    user = models.ForeignKey('AppUser', on_delete=models.CASCADE)


class WishListItem(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=200)
