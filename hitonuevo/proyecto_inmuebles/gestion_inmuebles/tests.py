from django.test import TestCase
from gestion_inmuebles.models import Usuario, Inmueble, RelacionUsuarioInmueble
# Create your tests here.


class ModeloInmuebleTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombres='Carolina Andrea',
            apellidos='Olivares Diaz',
            rut='16503192-K',
            direccion='Carrera Pinto 142',
            telefono='931935025',
            correo_electronico='carolivares1987@outlook.com',
            tipo_usuario='Arrendador'
        )

        self.inmueble = Inmueble.objects.create(
            nombre='Casa de Campo',
            descripcion='Hermosa y acogedora casa en el campo, especial para una vida tranquila y relajada',
            m2_construidos=120,
            m2_totales=180,
            habitaciones=4,
            banos=2,
            direccion='Calle Pomaire 4541',
            comuna='Lampa',
            tipo_inmueble='Casa',
            precio_mensual=750000,
            estacionamientos=2
        )

    def test_inmueble_creado(self):
        self.assertEqual(self.inmueble.nombre, 'Casa de Campo')


class RelacionUsuarioInmuebleTestCase(TestCase):
    def setUp(self):  # este codigo crea un usuario
        self.usuario = Usuario.objects.create(
            nombres='Richard Patricio',
            apellidos='Salas Ortega',
            rut='12789341-1',
            direccion='Calle Palguim 555',
            telefono='554774851',
            correo_electronico='rsalas@gmail.com',
            tipo_usuario='Arrendatario',
        )

        # este codigo crea un inmueble
        self.inmueble = Inmueble.objects.create(
            nombre='Centrico Departamento',
            descripcion='Moderno y recien estrenado departamento en el centro de Santiago',
            m2_construidos=60,
            m2_totales=80,
            estacionamientos=1,
            habitaciones=2,
            banos=1,
            direccion='Alonso de Ovalle 1650, depto 55',
            comuna='Santiago Centro',
            tipo_inmueble='Departamento',
            precio_mensual=530000
        )

        # este codigo crea la relacion entre usuario e inmueble
        self.relacion = RelacionUsuarioInmueble.objects.create(
            usuario=self.usuario,
            inmueble=self.inmueble,
            estado='Pendiente'
        )

    # este codigo verifica que la relacion se haya creado de forma correcta
    def test_relacion_usuario_inmueble(self):
        relacion = RelacionUsuarioInmueble.objects.get(
            usuario=self.usuario, inmueble=self.inmueble)
        self.assertEqual(relacion.usuario, self.usuario)
        self.assertEqual(relacion.inmueble, self.inmueble)
        self.assertEqual(relacion.estado, 'Pendiente')

    # este codigo verifica que un usuario pueda ingresar a los inmuebles relacionados
    def test_relaciones_usuario(self):
        inmuebles = self.usuario.relaciones.all()
        self.assertIn(self.inmueble, [
                      relacion.inmueble for relacion in inmuebles])

    # este codigo verifica que un inmueble puede acceder a los usuarios relacionados
    def test_relaciones_inmueble(self):
        usuarios = self.inmueble.relaciones.all()
        self.assertIn(
            self.usuario, [relacion.usuario for relacion in usuarios])
