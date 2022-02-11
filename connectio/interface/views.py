from django.shortcuts import render

# Create your views here.


def create(request):
    return render('create.html')


def date(request, date):
    return render('date.html')


def events(request, event):
    return render('events.html')


def about(request):
    return render('about.html')
