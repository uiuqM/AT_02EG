from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import nota
from django.template import loader
from datetime import datetime
from django.urls import reverse
from django.shortcuts import render


#from .forms import NotaForm

# Create your views here.

def index(request):
    latest_nota = nota.objects.order_by('data')
    template = loader.get_template('app_notas/index.html')
    context = {
        'latest_nota': latest_nota,
    }
    return HttpResponse(template.render(context, request))

def detail(request, nota_id):
    notaa = get_object_or_404(nota, pk=nota_id)
    return render(request, 'app_notas/detail.html', {'nota':notaa})

def save_nota(request):

    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']
        data = datetime.now()
        en = nota(titulo=titulo, conteudo=conteudo, data=data)
        en.save()
    return HttpResponse('ok')

def delete_nota(request, id):   
    del_nota = nota.objects.get(pk=id)
    del_nota.delete()
    return redirect('index')


def mod_nota(request, id):
    m_nota = nota.objects.get(pk=id)

def Usuario(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.save()
    #exibir todos os usuários cadastrados em uma nova página
    usuarios={
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para as páginas de listagem de usuários
    return render(request, 'usuarios/usuarios.html',usuarios)

