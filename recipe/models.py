from django.db import models
from django.forms import ModelForm



class IngredientType(models.Model):
    name = models.CharField(max_length=127)
    unit_type = models.CharField(max_length=32)

class Ingredient(models.Model):
    ingredient_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)
    value = models.FloatField()

class Recipe(models.Model):
    name = models.CharField(max_length=127)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField()


class IngredientForm(ModelForm):
    class Meta:
        model = IngredientType
        fields = ['name', 'unit_type']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'image']