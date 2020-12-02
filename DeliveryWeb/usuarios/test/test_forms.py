from django.test import TestCase
from django.urls import reverse
from usuarios.models import local, transporte

def test_get_template_reverse(self):
        
        local = local.objects.create(nombre=sushi, direccion="esmeralda")
        response = self.client.get(reverse('local_detail', kwargs={'pk':local.pk}))
        self.assertEqual(response.status_code, 404)