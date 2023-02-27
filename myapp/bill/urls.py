from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('bills', views.bills, name='about'),
    path('create', views.create, name='create')
]
