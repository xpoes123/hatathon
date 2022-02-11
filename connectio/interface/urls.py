from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('date/<str:date>', views.date, name='date'),
    path('events/<str:event>', views.events, name='events'),
    path('about', views.about, name='about'),
]
