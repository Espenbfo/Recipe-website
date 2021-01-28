from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import IngredientForm, IngredientType, Ingredient, Recipe, RecipeForm

def index(request):
    recipes = Recipe.objects.all()
    return render(request, "core\\recipes.html", {"recipes": recipes})


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

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def create_recipe(request):
    if request.method == "POST":
        form = request.POST

        name = form["recipe_name"]
        print(request.FILES)
        image = request.FILES["image"]
        print(image)
        r = Recipe.objects.create(recipe_name=name,image=image)
        #with open("image.jpg", "w") as f:
        #    for chunk in image.chunks():
        #        f.write(image)
        print(r)
        ingredient_list = []
        number_of_ingredients = form["number-of-ingredients"]

        for i in range(1,int(number_of_ingredients)+1):
            name = form[str(i) + "name"]
            value = form[str(i) + "number"]
            ingredient_type = IngredientType.objects.get(ingredient_name=name)
            ingredient_list.append(Ingredient.objects.create(value=float(value), ingredient_type=ingredient_type, recipe=r))
        return HttpResponseRedirect("")
    else:
        form = RecipeForm()

    ingredients = IngredientType.objects.all()
    return render(request, "core\\createrecipe.html", {"form": form, "ingredients": ingredients})