from django.shortcuts import render
from django.utils import timezone
from .models import Ingredient

def post_list(request):

    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient/post_list.html', {'ingredients': ingredients})
