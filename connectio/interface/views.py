from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)


def create(request):
    context = {}
    return render(request, 'create.html', context)


def date(request, date):
    context = {}
    return render(request, 'date.html', context)


def events(request, event):
    context = {}
    return render(request, 'events.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)
