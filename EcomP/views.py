
from django.shortcuts import render

from products.models import Prod


def home(request):
    product = Prod.objects
    return render(request, 'home.html', {'prod' : product})
