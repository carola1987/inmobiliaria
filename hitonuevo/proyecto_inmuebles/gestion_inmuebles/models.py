from django.db import models

# Create your models here.


class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario'),
    ]

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.tipo_usuario})"


class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=50)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class RelacionUsuarioInmueble(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Aceptada', 'Aceptada'),
        ('Rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='relaciones')
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE, related_name='relaciones')
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.inmueble} ({self.estado})"
