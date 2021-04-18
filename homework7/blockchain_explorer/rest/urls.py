from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('txs', views.get_txes, name='get_txes'),
    path('blocks', views.get_blocks, name='get_blocks'),
]