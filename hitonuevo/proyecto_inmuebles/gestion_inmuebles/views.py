from django.shortcuts import render, get_list_or_404, redirect
from gestion_inmuebles.models import Usuario, Inmueble, RelacionUsuarioInmueble
from .models import Inmueble
from django.views import View
from .forms import InmuebleForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


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
    
class InmuebleCreateView(CreateView):  # Esta vista es para crear un inmueble, solo para arrendadores
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'gestion_inmuebles/inmueble_form.html'
    success_url = reverse_lazy('gestion_inmuebles:inmueble_list')   # Redirige a la lista de inmuebles

    def form_valid(self, form):
        # Aquí puedes agregar lógica adicional si es necesario
        return super().form_valid(form)