from django.shortcuts import render
from . models import local, transporte
from django.views import generic

#importando para los formularios

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

# Create your views here.

def index(request):
    num_Locales = local.objects.all().count()
    nom_Local  = local.objects.filter(tipoEmpresa__exact='Salud').count()

    return render(
        request,
        'index.html',
        context={'numero_locales': num_Locales, 'Nombre_local': nom_Local},
    )

def registro(request):

    num_registros = local.objects.all().count()

    return render(
        request,
        'Registro.html',
        context={'numero_registros': num_registros},
    )
def sobrenosotros(request):

    return render(
        request,
        'Sobrenosotros.html',
    )

#formulario


class LocalCreate(CreateView):
    model = local
    fields = '__all__'

class LocalUpdate(UpdateView):
    model = local
    fields = {'correo', 'telefono', 'direccion'}

class LocalDelete(DeleteView):
    model  = local
    success_url = reverse_lazy('index')

class LocalDetailView(generic.DetailView):
    model = local


#Listas detalladas

class LocalListView(generic.ListView):
    model  = local
    paginate_by = 10

#Transporte


class transporteCreate(CreateView):
    model = transporte
    fields = '__all__'

class transporteUpdate(UpdateView):
    model = transporte
    fields = {'nombre', 'telefono', 'correo'}

class transporteDelete(DeleteView):
    model = transporte
    success_url = reverse_lazy('index')

#Vista de detalle
class transporteDetailView(generic.DetailView):
    model = transporte

#Lista de transporte

class transporteListView(generic.ListView):
    model  = transporte
    paginate_by = 10


