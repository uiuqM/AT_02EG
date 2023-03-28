from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import nota
from django.template import loader
from datetime import datetime

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
        dt = data.strftime("%Y/%m/%d %H:%M:%S")
        print(titulo, conteudo, dt)
        en = nota(titulo=titulo, conteudo=conteudo, data=data)
        en.save()
    return HttpResponse('ok')