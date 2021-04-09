from django.shortcuts import render
from .models import Neighborhood

def home(request):
    return render(request, 'index.html')

def hood(request):
    '''
    A function for showcasing the list of neighborhoods
    
    '''
    queryset_list = Neighborhood.objects.active().order_by("-timestamp")
    queryset = Neighborhood.objects.all()   

    context = {
            "title":"Neighborhoods",
            "object_list":queryset
        }

    return render(request,"hood.html", context)
