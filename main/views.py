from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo, Item

# Create your views here.

def index(response, id):
    ls = ToDo.objects.get(id=id)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(items.text)))

def v1(response):
    return HttpResponse("<h1>view1</h1>")