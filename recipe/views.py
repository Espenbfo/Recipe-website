from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "core\\recipes.html")


def create_ingredient(request):
    return render(request, "core\\createingredient.html")


def create_recipe(request):
    return render(request, "core\\createrecipe.html")