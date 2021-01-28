from django.db import models
from django.forms import ModelForm



class IngredientType(models.Model):
    ingredient_name = models.CharField(max_length=127)
    unit_type = models.CharField(max_length=32)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=127)
    image = models.ImageField()

class Ingredient(models.Model):
    ingredient_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.FloatField()

class IngredientForm(ModelForm):
    class Meta:
        model = IngredientType
        fields = ['ingredient_name', 'unit_type']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'image']