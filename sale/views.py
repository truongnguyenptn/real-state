# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from sale.models import Sale
from datetime import datetime
from django import forms





from django.shortcuts import render, redirect
from .forms import SaleForm

def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/sale/sale_success')
    else:
        form = SaleForm()
    return render(request, 'sale/sale_form.html', {'form': form})

def sale_success(request):
    return render(request, 'sale_success.html')


def sale_send_success(request):
    return render(request, 'sale/sale_success.html')