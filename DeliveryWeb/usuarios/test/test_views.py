from django.test import TestCase

# Create your tests here.

from usuarios.models import local, transporte
from django.urls import reverse


class LocalListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_locals = 12
        for local_id in range(number_of_locals):
            local.objects.create(
                nombre=f'sushi {local_id}',
                direccion=f'Esmeralda {local_id}',)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/usuarios/local/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('locales'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('locales'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/local_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('locales'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['local_list']) == 10)

    def test_lists_all_locales(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('locales')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['local_list']) == 2)

class TransporteListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        number_of_transporte = 13

        for transporte_id in range(number_of_transporte):
            transporte.objects.create(
                nombre=f'didi {transporte_id}',
                rut=f'194974493 {transporte_id}',
            )

        def test_view_url_exists_at_desired_location(self):
            response = self.client.get('/usuarios/transporte/')
            self.assertEqual(response.status_code, 200)

        def test_view_url_accessible_by_name(self):
            response = self.client.get(reverse('transportes'))
            self.assertEqual(response.status_code, 200)

        def test_view_uses_correct_template(self):
            response = self.client.get(reverse('transportes'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'usuarios/transporte_list.html')
        
        def test_pagination_is_ten(self):
            response = self.client.get(reverse('transportes'))
            self.assertEqual(response.status_code, 200)
            self.assertTrue('is_paginated' in response.context)
            self.assertTrue(response.context['is_paginated'] == True)
            self.assertTrue(len(response.context['transporte_list']) == 10)

        def test_lists_all_transportes(self):
            # Get second page and confirm it has (exactly) remaining 3 items
            response = self.client.get(reverse('transportes')+'?page=2')
            self.assertEqual(response.status_code, 200)
            self.assertTrue('is_paginated' in response.context)
            self.assertTrue(response.context['is_paginated'] == True)
            self.assertTrue(len(response.context['transporte_list']) == 3)

        def test_display_no_published_post(self):
            #test_user = User.objects.create(nombre="prueba", password="securetestpassword")
            local = local.objects.create(nombre=sushi, direccion="esmeralda")
            response = self.client.get(reverse('local_detail', kwargs={'pk':local.pk}))
            self.assertEqual(response.status_code, 404)