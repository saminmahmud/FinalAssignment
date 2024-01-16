from django.shortcuts import render,redirect
from train.models import Train
from station.models import Station

# def home(request):
#     return render(request, 'home.html')


def home(request, category_slug = None):
    train = Train.objects.all()
    if category_slug is not None:
        category = Station.objects.get(slug = category_slug)
        train = Train.objects.filter(start_station  = category)
    categories = Station.objects.all()
    return render(request, 'home.html', {'trains' : train, 'category' : categories})
