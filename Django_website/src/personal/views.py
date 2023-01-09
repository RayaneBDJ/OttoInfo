from django.shortcuts import render
from .models import *
from django.db.models import Count, Q

from .filter import DriversFilter

# Create your views here.

def merge_dicts(a, b):
    m = a.copy()
    m.update(b)
    return m

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
    
    drivers = Drivers.objects.all()
    drivers_count = drivers.count
    
    races = Races.objects.all()
    races_count = races.count()
    
    circuits = Circuits.objects.all()
    circuits_count = circuits.count()
    
    constructors = Constructor.objects.all()
    constructos_count = constructors.count()
    
    results = Results.objects.all()
    results_count = results.count()
    # gorup by drivers_nbrRaces = results.g

    return render(request,"personal/home.html",context)


def explorer_screen(request) :
    
    
    forename = request.GET.get('Forename')
    
    surname = request.GET.get('Surname')
   
    nationality = request.GET.get('nationality')

    dob = request.GET.get('Dob')
    
    
  
    if forename != None and surname != None and nationality != None :
        drivers_filt = Drivers.objects.filter(Q(surname__in = surname) |
                                                Q(forename__in=forename) |
                                                 Q(nationality__in=nationality))
    elif forename != None and surname != None and nationality == None :
        drivers_filt = Drivers.objects.filter(Q(surname__in = surname) |
                                                Q(forename__in=forename) )
    elif forename == None and surname != None and nationality != None :
        drivers_filt = Drivers.objects.filter(Q(surname__in= surname) |
                                                Q(nationality__in=nationality) )
    elif forename != None and surname == None and nationality != None :
        drivers_filt = Drivers.objects.filter(Q(forename__icontains = forename) |
                                                Q(nationality__in=nationality) )
    elif forename != None and surname == None and nationality == None :
         drivers_filt = Drivers.objects.filter(Q(forename__in = forename))
    elif forename == None and surname != None and nationality == None :
         drivers_filt = Drivers.objects.filter(Q(surename_in = surname))
    elif forename == None and surname == None and nationality != None :
        drivers_filt = Drivers.objects.filter(Q(nationality__in = nationality))
    
    else :
        drivers_filt = "Nothing to show yet"
    
    
    drivers = Drivers.objects.all()
    drivers_filter = DriversFilter(request.GET,queryset = drivers)
        
    
    context = {}
    context['filter'] = drivers_filter
    context['drivers'] = drivers_filt
   
        
 
    return render(request,"personal/explorer.html",context)

def contact_screen(request) :

    return render(request,'personal/contact.html',{})

def vizu_screen(request):
    context = {}
    
    
    labels =[]
    data = []
    
    labels_col = []
    labels_col_names=[]
    data_col = []
   
    
    drivers = Drivers.objects.values('nationality').annotate(total = Count('nationality')).order_by('-total')
    results_ranking = Results.objects.values('driverid').annotate(total = Count('rank',filter=Q(rank =1))).order_by('-total')[:5]
    
   
    
    for result in results_ranking:
        labels_col.append(result['driverid'])
        data_col.append(result["total"])
        
        
    best_drivers = Drivers.objects.all().filter(driverid__in = labels_col)
    
    for driver in best_drivers:
        labels_col_names.append(driver.surname + ' ' +driver.forename)
        
    

    for driver in drivers:
        labels.append(driver['nationality'])
        data.append(driver['total'])
        
    

        
    
    
        
    
    context['labels'] = labels
    context['data'] = data
    
    data_labels = [ [labels[index],data[index]] for index in range(len(data))]
    context['drivers'] = drivers
    context['data_labels'] = data_labels
    
    data_labels_col = [ [labels_col_names[index],data_col[index]] for index in range(len(data_col))]
    context['data_col'] = data_col
    context['labels_col'] = labels_col
    context['data_labels_col'] = data_labels_col
    
    
    
    return render(request,'personal/vizualisation.html',context)





