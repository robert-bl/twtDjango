from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDo, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDo.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})



def home(response):
    return render(response, "main/home.html", {"name": "test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDo(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:    
        form = CreateNewList
    return render(response,"main/create.html", {"form": form})