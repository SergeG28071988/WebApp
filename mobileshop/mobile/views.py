from django.shortcuts import render

from .forms import RateForm
from .models import Rate

def index(request):
    rates = Rate.objects.order_by('-id')
    return render(request, 'mobile/index.html', {'title': 'Главная страница сайта', 'rates': rates})


def about(request):
    return render(request, 'mobile/about.html')


def create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
    form = RateForm()
    context ={
        'form': form
    }
    return render(request, 'mobile/create.html', context)
