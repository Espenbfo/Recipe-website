from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from random import randint
from io import BytesIO

from PIL import Image
from .models import IngredientForm, IngredientType, Ingredient, Recipe, \
    RecipeForm, CategoryForm, Category


def resize_image(img):
    im = Image.open(img)
    print(im.verify())
    im = Image.open(img)
    width, height = im.size

    max_size = 300
    print(im.size)
    width_greater = width >= height
    print(width_greater)
    if width_greater:
        print(width, max_size)
        if width > max_size:
            im = im.resize((max_size, int(height * max_size / width)))
    else:
        if height > max_size:
            im = im.resize((int(width * max_size / height), max_size))
    print(im.size)
    buffer = BytesIO()
    im.save(fp=buffer, format="JPEG")
    return ContentFile(buffer.getvalue())


def recipe_page(request, page):
    recipes = Recipe.objects.all()
    page_number = page
    print(page_number)
    recipes = Paginator(recipes, 12).get_page(page_number)

    return render(request, "core\\recipes.html", {"recipes": recipes})

def category_page(request, page):
    categories = Category.objects.order_by("category_name")
    page_number = page
    print(page_number)
    categories = Paginator(categories, 12).get_page(page_number)
    print(categories)
    return render(request, "core\\categories.html", {"categories": categories})


def recipes_category_page(request, category_id, page):
    recipes = Recipe.objects.all().filter(category=category_id)
    page_number = page
    print(page_number)
    categories = Paginator(recipes, 12).get_page(page_number)
    print(categories)
    return render(request, "core\\recipes.html", {"recipes": recipes})



def index(request):
    recipes = Recipe.objects.all()
    page_number = 1
    recipes = Paginator(recipes, 12).get_page(page_number)

    return render(request, "core\\recipes.html", {"recipes": recipes})


def recipe(request, recipe_id):
    chosen_recipe = Recipe.objects.get(id=recipe_id)
    chosen_ingredients = Ingredient.objects.all().filter(recipe_id=recipe_id)
    ingredient_names = [IngredientType.objects.get(id=ing.ingredient_type_id)
                        for ing in chosen_ingredients]

    print(chosen_recipe.recipe_name)
    print(chosen_ingredients)
    return render(request, "core/recipe.html", {"recipe": chosen_recipe,
                                                "ingredients": chosen_ingredients,
                                                "ingredient_names": ingredient_names})



def ingredients(request):
    ingredients = IngredientType.objects.all()
    return render(request, "core\\ingredients.html",
                  {"ingredients": ingredients})


@staff_member_required
def create_ingredient(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["ingredient_name"].lower()
            unit_type = form.cleaned_data["unit_type"].lower()
            IngredientType.objects.create(ingredient_name=name,
                                          unit_type=unit_type)
            return HttpResponseRedirect("createingredient")
    else:
        form = IngredientForm()

    return render(request, "core\\createingredient.html", {"form": form})

@staff_member_required
def create_category(request):
    if request.method == "POST":
        form = request.POST
        print("hello")
        name = form["category_name"].lower()
        image = request.FILES["category_image"]
        image = resize_image(image)
        Category.objects.create(category_name=name,
                                category_image=InMemoryUploadedFile(
                                    image,
                                    None,
                                    str(randint(0,
                                                1000000000000)) + ".jpg",
                                    "image/jpeg",
                                    image.tell,
                                    None
                                ))
        return HttpResponseRedirect("createcategory")
    else:
        form = CategoryForm()

    return render(request, "core\\createcategory.html", {"form": form})


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@staff_member_required
def create_recipe(request):
    if request.method == "POST":
        form = request.POST

        name = form["recipe_name"]
        category = Category.objects.get(category_name=form["category"])
        description = form["recipe_description"]
        print(request.FILES)
        image = request.FILES["image"]
        try:
            im = Image.open(image)
            print(im.verify())
            im = Image.open(image)
            width, height = im.size

            max_size = 300
            print(im.size)
            width_greater = width >= height
            print(width_greater)
            if width_greater:
                print(width, max_size)
                if width > max_size:
                    im = im.resize((max_size, int(height * max_size / width)))
            else:
                if height > max_size:
                    im = im.resize((int(width * max_size / height), max_size))
            print(im.size)
            buffer = BytesIO()
            im.save(fp=buffer, format="JPEG")
            content_im = ContentFile(buffer.getvalue())
        except Exception as e:
            print(e)
            return HttpResponseRedirect("YOUCANTTRICKMEEEE")
        print(image)
        r = Recipe.objects.create(recipe_name=name,
                                  recipe_description=description,
                                  category=category,
                                  image=InMemoryUploadedFile(
                                      content_im,
                                      None,
                                      str(randint(0, 1000000000000)) + ".jpg",
                                      "image/jpeg",
                                      content_im.tell,
                                      None
                                  ))
        # with open("image.jpg", "w") as f:
        #    for chunk in image.chunks():
        #        f.write(image)
        print(r)
        ingredient_list = []
        number_of_ingredients = form["number-of-ingredients"]

        for i in range(1, int(number_of_ingredients) + 1):
            name = form[str(i) + "name"]
            value = form[str(i) + "number"]
            ingredient_type = IngredientType.objects.get(ingredient_name=name)
            ingredient_list.append \
                (Ingredient.objects.create(value=float(value),
                                           ingredient_type=ingredient_type,
                                           recipe=r))
        return HttpResponseRedirect("")
    else:
        form = RecipeForm()

    ingredients = IngredientType.objects.order_by("ingredient_name")
    categories = Category.objects.order_by("category_name")
    return render(request, "core\\createrecipe.html",
                  {"form": form,
                   "ingredients": ingredients,
                   "categories": categories})
