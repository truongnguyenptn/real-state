from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('blog',views.blog,name ='blog'),
    path('about',views.about,name ='about'),
    path('', views.blog, name='blog page'),

]
