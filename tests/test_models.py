from django.test import TestCase
from store.models import Product, Category

class TestProductModel(TestCase):

    def setUp(self):
        # Create a category
        self.category = Category.objects.create(name='Test Category')

    def test_create_product(self):
        # Create a product with a category
        product = Product.objects.create(name='Test Product', price=10, category=self.category)

        # Assert that the product was created successfully
        self.assertIsNotNone(product)
