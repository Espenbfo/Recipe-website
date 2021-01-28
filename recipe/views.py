from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import IngredientForm

def index(request):
    return render(request, "core\\recipes.html")


def create_ingredient(request):

    if request.method == "POST":
        form = IngredientForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("create")
    else:
        form = IngredientForm()

    return render(request, "core\\createingredient.html", {"form": form})


def create_recipe(request):
    return render(request, "core\\createrecipe.html")