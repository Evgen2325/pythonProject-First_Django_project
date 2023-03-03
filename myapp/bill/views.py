from django.shortcuts import render, redirect
from .models import Bills
from .forms import BillsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from datetime import datetime, timedelta


def index(request):
    return render(request, 'bill/index.html')


class BillsDetailView(DetailView):
    model = Bills
    template_name = 'bill/details_view.html'
    context_object_name = 'all_bills'


class BillsUpdateView(UpdateView):
    model = Bills
    template_name = 'bill/create.html'

    form_class = BillsForm


class BillsDeleteView(DeleteView):
    model = Bills
    success_url = '/'
    template_name = 'bill/bills-delete.html'


def bills(request):
    bill = Bills.objects.all()
    return render(request, 'bill/bills.html', {'bill': bill})


'''it is function for get sum(prices)'''
# def get_total_price(request):
#     all_prices = ''
#     total = Bills.objects.filter('price')
#     for i in total:
#         all_prices += i.price
#         return render(request, 'bill/bills.html', {'all_total': all_prices})


def bills_filter(request, pk):
    bill = Bills.objects.all()
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24*7)
        bill = bill.filter(date__gte=now)
    elif pk == 2:
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)
        bill = bill.filter(date__gte=now)
    elif pk == 3:
        bill = bill
    return render(request, 'bill/bills.html', {'bill': bill})


def create(request):
    error = ''
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            error = 'Некорректные данные'

    form = BillsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'bill/create.html', data)
