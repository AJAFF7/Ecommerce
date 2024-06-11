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
        self.assertEqual(response.status_code, 200)  # Assuming home page returns HTTP 200 OK
        self.assertTrue('home.html' in [t.name for t in response.templates])  # Check if 'home.html' is used
        self.assertTrue('base.html' in [t.name for t in response.templates])  # Check if 'base.html' is used
        self.assertTrue('navbar.html' in [t.name for t in response.templates])  # Check if 'navbar.html' is used
