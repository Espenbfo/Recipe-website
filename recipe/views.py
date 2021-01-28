from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import IngredientForm, IngredientType, Ingredient, Recipe, RecipeForm

def index(request):
    return render(request, "core\\recipes.html")


def ingredients(request):
    ingredients = IngredientType.objects.all()
    return render(request, "core\\ingredients.html", {"ingredients": ingredients})


def create_ingredient(request):

    if request.method == "POST":
        form = IngredientForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["ingredient_name"]
            unit_type = form.cleaned_data["unit_type"]
            IngredientType.objects.create(ingredient_name=name,unit_type=unit_type)
            return HttpResponseRedirect("create")
    else:
        form = IngredientForm()

    return render(request, "core\\createingredient.html", {"form": form})


def create_recipe(request):
    if request.method == "POST":
        form = request.POST

        name = form["name"]
        image = form["image"]
        r = Recipe.objects.create(recipe_name=name,image=image)
        print(r)
        ingredient_list = []
        number_of_ingredients = form["number-of-ingredients"]

        for i in range(1,int(number_of_ingredients)+1):
            name = form[str(i) + "name"]
            value = form[str(i) + "number"]
            ingredient_type = IngredientType.objects.get(name=name)
            ingredient_list.append(Ingredient.objects.create(value=float(value), ingredient_type=ingredient_type, recipe=r))
        return HttpResponseRedirect("")
    else:
        form = RecipeForm()

    ingredients = IngredientType.objects.all()
    return render(request, "core\\createrecipe.html", {"form": form, "ingredients": ingredients})