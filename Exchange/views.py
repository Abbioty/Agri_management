from django.shortcuts import render
from django.shortcuts import render
from .models import Exchange
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.


def home_index(request):
    exchanges = Exchange.objects.all()
    context = {'exchanges': exchanges}
    return render(request, 'exchange_index.html', context)
