from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from artista_api.models import Cancion, Artista

from artista_api.serializers import CancionSerializer, ArtistaSerializer

from artista_api.forms import CancionForm, ArtistaForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
# Create your views here.


def get_all_artista():
    artistas = Artista.objects.all().order_by('name')
    artistas_serializers = ArtistaSerializer(artistas, many=True)
    return artistas_serializers.data

def artista_rest(request):
    artistas = get_all_artista()
    return JsonResponse(artistas, safe=False)

def index_artista(request):
    artistas = get_all_artista()
    return render(request, 'index_artista.html', {'artistas': artistas})

class ArtistaListView(ListView):
    model = Artista
    template_name = 'artista_list.html'  # Nombre del nuevo template
    context_object_name = 'artistas'

    def get_queryset(self):
        return Artista.objects.prefetch_related('canciones')
    
def add_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artistas:index_artista')  # Ajusta esto a la vista que muestra la lista de autores
    else:
        form = ArtistaForm()
    return render(request, 'artistas/form_artista.html', {'form': form})    


class NewArtistaView(CreateView):
    form_class = ArtistaForm
    template_name = 'form_artista.html'
    success_url = '/index_artista/'








def get_all_canciones():
    canciones = Cancion.objects.all().order_by('Nombre')
    canciones_serializers = CancionSerializer(canciones, many=True)
    return canciones_serializers.data

def home_canciones(request):
    canciones = get_all_canciones()
    return render(request, 'home_canciones.html', {'canciones': canciones})



def cancion_rest(request):
    canciones = get_all_canciones()
    return JsonResponse(canciones, safe=False)


class NewCancionView(CreateView):
    form_class = CancionForm
    template_name = 'form_cancion.html'
    success_url = '/home_canciones/'



