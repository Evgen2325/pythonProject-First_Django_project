from django.shortcuts import render, redirect
from .models import Bills
from .forms import BillsForm
from django.views.generic import DetailView, UpdateView, DeleteView


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


class BillsDeleteView(DetailView):
    model = Bills
    template_name = 'bill/bills-delete.html'


def bills(request):
    bill = Bills.objects.order_by('date')
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
