from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import home, login_user, logout_user, register_user, product, about, category, search

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, about)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_user)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_user)

    def test_product_url_resolves(self):
        url = reverse('product', args=[1])  # Assuming 'product' URL expects an argument
        self.assertEqual(resolve(url).func, product)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_category_url_resolves(self):
        url = reverse('category', args=['some-category'])  # Assuming 'category' URL expects a string argument
        self.assertEqual(resolve(url).func, category)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)
