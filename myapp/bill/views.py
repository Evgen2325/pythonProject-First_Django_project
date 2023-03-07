from django.shortcuts import render, redirect
from .models import Bills
from .forms import BillsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from datetime import datetime, timedelta
from gtts import gTTS
from playsound import playsound


def sound(request):
    text_val = 'Добро пожаловать в приложение которое поможет вам контролировать ваши расходы'
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('test.mp3')
    playsound('test.mp3')
    return render(request, 'bill/index.html', {'playsound': playsound})


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


def total_price(request):
    items = Bills.objects.all()
    total = sum(items.values_list('price', flat=True))
    return render(request, 'bill/bills.html', {'total': total})


def bills_filter(request, pk):
    bill = Bills.objects.all()
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)
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
