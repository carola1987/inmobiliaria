from django import forms
from .models import Inmueble, Usuario

class InmuebleForm(forms.ModelForm): #este es el formulario para crear el inmueble
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'estacionamientos',
                  'habitaciones', 'banos', 'direccion', 'comuna', 'tipo_inmueble', 'precio_mensual']
        
class UsuarioForm(forms.ModelForm): #este es el formulario para registrar un usuario
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']

        