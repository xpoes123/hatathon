from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'interface/home.html', context)


def create(request):
    context = {}
    return render(request, 'interface/create.html', context)


def date(request, date):
    context = {}
    return render(request, 'interface/date.html', context)


def events(request, event):
    context = {}
    return render(request, 'interface/events.html', context)


def about(request):
    context = {}
    return render(request, 'interface/about.html', context)
