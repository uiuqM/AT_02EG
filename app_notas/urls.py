from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios', views.usuario, name='listagem_usuarios'),
    path('index', views.index, name='index'),
    path('<int:nota_id>', views.detail, name='detail'),
    path('delete_nota/<int:id>', views.delete_nota, name="delete_nota"),
    path('mod_nota/<int:id>', views.mod_nota, name="mod_nota"),
    path('save_modnota/<id>', views.save_modnota, name='save_modnota'),
    #path('save_nota', views.save_nota, name='save_nota'),
]