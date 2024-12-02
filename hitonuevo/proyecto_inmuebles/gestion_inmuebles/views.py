from django.shortcuts import render, get_list_or_404
from gestion_inmuebles.models import Usuario, Inmueble, RelacionUsuarioInmueble
from .models import Inmueble
from django.views import View
from .forms import InmuebleForm

# Create your views here.


def listar_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'listar_inmuebles.html', {'inmuebles': inmuebles})


def crear_usuario(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        rut = request.POST.get('rut')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo_electronico')
        tipo_usuario = request.POST.get('tipo_usuario')

        nuevo_usuario = Usuario.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            rut=rut,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo,
            tipo_usuario=tipo_usuario
        )
        return render(request, 'usuario_creado.html', {'usuario': nuevo_usuario})

class InmuebleListView(View): #esta vista es para listar los inmuebles
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        return render(request, 'gestion_inmuebles/inmueble_list.html', {'inmuebles': inmuebles})
    
class InmuebleDetailView(View): #esta vista es para mostrar los detalles de los inmuebles
    def get(self, request, inmueble_id):
        inmueble = get_list_or_404(Inmueble, pk=inmueble_id)
        return render(request, 'gestion_inmuebles/inmueble_detail.html', {'inmueble':inmueble})
    
class InmuebleCreateView(View): #esta vista es para crear un inmueble, solo para arrendadores
    def get(self, request):
        form = InmuebleForm
        return render(request, 'gestion_inmuebles/inmueble_form.html', {'form':form})
    
    def post(self, request):
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save() #este comando guarda el inmueble que se acaba de crear
            return redirect('gestion_inmuebles: inmueble_list') #este comando redirige a la lista de inmuebles
        return render(request, 'gestion_inmuebles/inmueble_form.html', {'form':form})
    
    
