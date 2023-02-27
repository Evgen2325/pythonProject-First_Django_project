from django.shortcuts import render
from .models import Bills


def index(request):
    return render(request, 'bill/index.html')


def bills(request):
    bill = Bills.objects.all()
    return render(request, 'bill/bills.html', {'bill': bill})


def create(request):
    return render(request, 'bill/create.html')
