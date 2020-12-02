from django.test import TestCase
from django.urls import reverse
from usuarios.models import local, transporte

def test_get_template_reverse_local(self):
        
        local = local.objects.create(nombre="sushi", direccion="esmeralda")
        response = self.client.get(reverse('local_detail', kwargs={'pk':local.pk}))
        self.assertEqual(response.status_code, 200)

def test_get_template_reverse_transporte(self):
        transporte = transporte.objects.create(nombre="didi", telefono="975525786")
        response = self.client.get(reverse('transporte_detail', kwars={'pk':transporte.pk}))
        self.assertEqual(response.status_code, 200)