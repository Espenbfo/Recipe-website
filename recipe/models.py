from django.db import models
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _

class IngredientType(models.Model):
    ingredient_name = models.CharField(max_length=127, unique=True)
    unit_type = models.CharField(max_length=32)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='static/img/')
    recipe_description = models.TextField()

class Ingredient(models.Model):
    ingredient_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.FloatField()

class IngredientForm(ModelForm):
    class Meta:
        model = IngredientType
        fields = ['ingredient_name', 'unit_type']

class RecipeForm(ModelForm):
    recipe_name = forms.CharField(label="", max_length=127,
                                         required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Tittel'}))
    recipe_description = forms.CharField(label="", widget=forms.Textarea(
        attrs={"placeholder": "beskrivelse"}
    ))
    class Meta:
        model = Recipe
        fields = ['recipe_name', "recipe_description", 'image']
        widgets = {
            "recipe_description": forms.Textarea(attrs={"cols": 30, "rows": 20}),
        }