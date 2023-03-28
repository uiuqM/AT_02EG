from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import nota
from django.template import loader
# Create your views here.

def index(request):
    latest_nota = nota.objects.order_by('data')[:5]
    template = loader.get_template('notas/index.html')
    context = {
        'latest_nota': latest_nota,
    }
    return HttpResponse(template.render(context, request))

def detail(request, nota_id):
    notaa = get_object_or_404(nota, pk=nota_id)
    return render(request, 'polls/detail.html', {'nota':notaa})