from django.contrib import admin
from .models import Usuario, Inmueble, RelacionUsuarioInmueble
# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'rut', 'tipo_usuario')
    search_fields = ('nombres', 'apellidos', 'rut')


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'estacionamientos',
                    'habitaciones', 'banos', 'direccion', 'comuna', 'tipo_inmueble', 'precio_mensual')
    list_filter = ('precio_mensual', 'tipo_inmueble', 'comuna')
    search_fields = ('nombre', 'direccion', 'comuna')


@admin.register(RelacionUsuarioInmueble)
class RelacionUsuarioInmuebleAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'inmueble', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('usuario__nombres', 'inmueble__nombre')
