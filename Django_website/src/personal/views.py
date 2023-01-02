from django.shortcuts import render
from .models import *

from .filter import DriversFilter

# Create your views here.

def home_screen_view(request):
    
    context = {}
    context['some_string'] = "This is a string that I m passing to the view"
    context['some_number'] = 0
    
    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("Second entry")
    list_of_values.append("Third entry")
    list_of_values.append("Fourth entry")
    
    context['list_of_values'] = list_of_values
    
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request,"personal/home.html",context)


def explorer_screen(request) :
    context = {}
    drivers = Drivers.objects.all()
    
    context['drivers'] = drivers 
    
    myFilter = DriversFilter()
    
    context['myFilter'] = myFilter
    
    return render(request,"personal/explorer.html",context)

def contact_screen(request) :
    nom_pilote = request.GET['nom_pilote']
    context = {'nom_pilote' : nom_pilote}
    return render(request,'personal/contact.html',context)




