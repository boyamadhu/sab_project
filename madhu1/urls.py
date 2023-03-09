from django.urls import path
from madhu1.views import *
add_name='nnn'

urlpatterns={
    path('jersey/',jersey,name='jersey'),
}