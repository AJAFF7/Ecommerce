# In tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from store.models import Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        # Add more setup steps if necessary

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)  # Assuming home page returns HTTP 200 OK
        self.assertTemplateUsed(response, 'store/home.html')  # Assuming the home view renders 'store/home.html'
        self.assertTrue('home.html' in [t.name for t in response.templates])  # Check if 'home.html' is used
        self.assertTrue('base.html' in [t.name for t in response.templates])  # Check if 'base.html' is used
        self.assertTrue('navbar.html' in [t.name for t in response.templates])  # Check if 'navbar.html' is used

    def test_product_view(self):
        product = Product.objects.create(name='Test Product', price=10)  # Assuming a product exists in the database
        response = self.client.get(reverse('product', args=[product.pk]))
        self.assertEquals(response.status_code, 200)  # Assuming product page returns HTTP 200 OK
        self.assertTemplateUsed(response, 'store/product.html')  # Assuming the product view renders 'store/product.html'
        self.assertTrue('product.html' in [t.name for t in response.templates])  # Check if 'product.html' is used
        self.assertTrue('base.html' in [t.name for t in response.templates])  # Check if 'base.html' is used
        self.assertTrue('navbar.html' in [t.name for t in response.templates])  # Check if 'navbar.html' is used







# from django.test import TestCase, Client
# from django.urls import reverse
# from store.models import Product

# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.home_url = reverse('home')
#         # Add more setup steps if necessary

#     def test_home_view(self):
#         response = self.client.get(self.home_url)
#         self.assertEqual(response.status_code, 200)  # Assuming home page returns HTTP 200 OK
#         self.assertTrue('home.html' in [t.name for t in response.templates])  # Check if 'home.html' is used
#         self.assertTrue('base.html' in [t.name for t in response.templates])  # Check if 'base.html' is used
#         self.assertTrue('navbar.html' in [t.name for t in response.templates])  # Check if 'navbar.html' is used
