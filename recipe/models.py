from django.db import models
from django.forms import ModelForm

class Ingredient(models.Model):
    name = models.CharField(max_length=127)
    value = models.FloatField()
    unit_type = models.CharField(max_length=32)


class Recipe(models.Model):
    name = models.CharField(max_length=127)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField()


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'value', 'unit_type']
