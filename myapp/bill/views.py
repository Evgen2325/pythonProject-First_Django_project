from django.shortcuts import render
from .models import Bills
from .forms import BillsForm


def index(request):
    return render(request, 'bill/index.html')


def bills(request):
    bill = Bills.objects.all()
    return render(request, 'bill/bills.html', {'bill': bill})


def create(request):
    error = ''
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('bill/bills') not work
        else:
            error = 'Некорректные данные'

    form = BillsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'bill/create.html', data)
