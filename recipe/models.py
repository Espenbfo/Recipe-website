from django.db import models


class Ingredient(models.Model):
    name = models.TextField()
    value = models.FloatField()
    unit_type = models.TextField()


class Recipe(models.Model):
    name = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField()