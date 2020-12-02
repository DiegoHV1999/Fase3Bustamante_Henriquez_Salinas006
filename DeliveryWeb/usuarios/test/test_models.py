from django.test import TestCase
from usuarios.models import local

class LocalModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        local.objects.create(rut='19497449', nombre='jose bustamante', 
        correo='bustamante@gmail.com', telefono='123456789', direccion='pje esmeralda')
    
    def test_rut(self):
        Local = local.objects.get(id=1)
        field_label  =  Local._meta.get_field('rut').verbose_name
        self.assertEquals(field_label, 'rut')
    
    def test_rut_max_length(self):
        Local = local.objects.get(id=1)
        max_length = Local._meta.get_field('rut').max_length
        self.assertEquals(max_length, 12)

    def test_nombre(self):
        Local = local.objects.get(id=1)
        field_label  = Local._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')
    
    def test_nombre_max_length(self):
        Local = local.objects.get(id=1)
        max_length = Local._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 200)
    
    def test_direcciom(self):
        Local = local.objects.get(id=1)
        field_label = Local._meta.get_field('direccion').verbose_name
        self.assertEquals(field_label, 'direccion')

    def test_get_absolute_url(self):
        Local = local.objects.get(id=1)
        self.assertEquals(Local.get_absolute_url(), '/usuarios/local/1')



    


    