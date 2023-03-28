from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nota_id>', views.detail, name='detail'),
    path('delete_nota/<int:id>', views.delete_nota, name="delete_nota"),
    path('mod_nota/<int:id>', views.mod_nota, name="mod_nota")
    #path('save_nota', views.save_nota, name='save_nota'),
]