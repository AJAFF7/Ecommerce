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
        self.assertTemplateUsed(response, 'store/templates/home.html')  # Assuming the home view renders 'store/home.html'

    # Add more test cases for other views as needed
