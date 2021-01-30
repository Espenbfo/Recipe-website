"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, create_ingredient, create_recipe, ingredients, \
    recipe, recipe_page, create_category, category_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipe/<int:recipe_id>', recipe,
                       name="recipe"),
    path('createingredient', create_ingredient, name="create_ingredient"),
    path('createcategory', create_category, name="create_category"),
    path('create', create_recipe, name="create_recipe"),
    path('ingredients', ingredients, name="ingredients"),
    path('categories/<int:page>', category_page, name="category_page"),
    path('<int:page>', recipe_page, name="index"),
    path('', index, name="index"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#if DEBUG:
#    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)