# In tests/test_views.py

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


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.username = 'jaff'
        self.password = 'jaff5550140'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)  # Assuming home page returns HTTP 200 OK
        self.assertTrue('home.html' in [t.name for t in response.templates])  # Check if 'home.html' is used
        self.assertTrue('base.html' in [t.name for t in response.templates])  # Check if 'base.html' is used
        self.assertTrue('navbar.html' in [t.name for t in response.templates])  # Check if 'navbar.html' is used

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)  # Check if login page returns HTTP 200 OK
        self.assertTrue('login.html' in [t.name for t in response.templates])  # Check if 'login.html' is used

    def test_login_view_post_correct_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Check if login redirects after successful login
        self.assertRedirects(response, self.home_url)  # Assuming successful login redirects to home page

    def test_login_view_post_incorrect_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Login page should reload on incorrect credentials
        self.assertTrue('login.html' in [t.name for t in response.templates])  # Check if 'login.html' is used
        self.assertTrue('Invalid login' in response.content.decode())  # Assuming an 'Invalid login' message is shown










