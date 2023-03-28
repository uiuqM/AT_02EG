from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nota_id>', views.detail, name='detail'),
    #path('save_nota', views.save_nota, name='save_nota'),
]