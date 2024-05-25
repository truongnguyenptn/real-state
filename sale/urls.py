from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('sale', views.create_sale, name='create_sale'),
    path('sale_success', views.sale_send_success, name='sale_success'),
]