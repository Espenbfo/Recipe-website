from django.db import models
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _


class IngredientType(models.Model):
    ingredient_name = models.CharField(max_length=127, unique=True)
    unit_type = models.CharField(max_length=32)


class Category(models.Model):
    category_name = models.CharField(max_length=127, unique=True)
    category_image = models.ImageField(upload_to='static/img/')


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='static/img/')
    recipe_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    portions = models.IntegerField()


class Ingredient(models.Model):
    ingredient_type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.FloatField()


class IngredientForm(ModelForm):
    ingredient_name = forms.CharField(label="", max_length=127,
                                         required=True, widget=forms.TextInput(
            attrs={'placeholder': 'name'}))
    unit_type = forms.CharField(label="", max_length=32,
                                         required=True, widget=forms.TextInput(
            attrs={'placeholder': 'unit'}))
    class Meta:
        model = IngredientType
        fields = ['ingredient_name', 'unit_type']


class RecipeForm(ModelForm):
    recipe_name = forms.CharField(label="", max_length=127,
                                         required=True, widget=forms.TextInput(
            attrs={'placeholder': 'title'}))
    portions = forms.IntegerField(label="",
                                         required=True, widget=forms.NumberInput(
            attrs={'placeholder': 'portions'}))
    recipe_description = forms.CharField(label="", widget=forms.Textarea(
        attrs={"placeholder": "recipe"}
    ))

    class Meta:
        model = Recipe
        fields = ['recipe_name', "portions", "recipe_description", 'image']


class CategoryForm(ModelForm):
    category_name = forms.CharField(label="", max_length=127,
                                         required=True, widget=forms.TextInput(
            attrs={'placeholder': 'title'}))
    class Meta:
        model = Category
        fields = ['category_name', 'category_image']