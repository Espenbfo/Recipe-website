from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import IngredientForm, IngredientType

def index(request):
    return render(request, "core\\recipes.html")


def ingredients(request):
    ingredients = IngredientType.objects.all()
    return render(request, "core\\ingredients.html", {"ingredients": ingredients})


def create_ingredient(request):

    if request.method == "POST":
        form = IngredientForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            unit_type = form.cleaned_data["unit_type"]
            IngredientType.objects.create(name=name,unit_type=unit_type)
            return HttpResponseRedirect("create")
    else:
        form = IngredientForm()

    return render(request, "core\\createingredient.html", {"form": form})


def create_recipe(request):
    return render(request, "core\\createrecipe.html")