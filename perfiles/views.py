from django.shortcuts import redirect, render

from perfiles.models import Perfil

# Create your views here.
def lista_perfiles(request):
    # 1. Consultar los perfiles de la base de datos
    perfiles = Perfil.objects.all()
    # 2. Pasar los perfiles a la plantilla
    return render(request, 'perfiles/lista.html', {'perfiles':perfiles})


def detalle_perfil(request, perfil_id):
    # 1. Obtener el perfil indicado de la base de datos
    perfil = Perfil.objects.get(pk=perfil_id)
    # 2. Renderizar la plantilla con el perfil
    return render(request, 'perfiles/detalle.html', {'perfil':perfil})

def home(request):
    return redirect('perfiles/')