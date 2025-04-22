from store.models import Product, Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def db_add(self, product, quantity):
        """
        Add product by ID and quantity to cart, typically from saved JSON.
        """
        try:
            product_obj = Product.objects.get(id=product)
            product_id = str(product_obj.id)
            product_qty = int(quantity)

            if product_id not in self.cart:
                self.cart[product_id] = product_qty

            self.session.modified = True

            if self.request.user.is_authenticated:
                current_user = Profile.objects.filter(user__id=self.request.user.id)
                cart_str = str(self.cart).replace("'", "\"")
                current_user.update(old_cart=cart_str)

        except Product.DoesNotExist:
            pass  # Ignore invalid product IDs silently (or log it)

    def add(self, product, quantity):
        """
        Add product instance to the cart with quantity.
        """
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            cart_str = str(self.cart).replace("'", "\"")
            current_user.update(old_cart=cart_str)

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart

       
       
       
    def update(self, product_id, quantity):
        """
        Update the quantity of an existing product in the cart.
        """
        product_id = str(product_id)
        product_qty = int(quantity)

        # Update the product quantity in the cart
        self.cart[product_id] = product_qty
        self.session.modified = True

        # If the user is authenticated, update the saved cart in the database
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            cart_str = str(self.cart).replace("'", "\"")
            current_user.update(old_cart=cart_str)

        return self.cart



    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            cart_str = str(self.cart).replace("'", "\"")
            current_user.update(old_cart=cart_str)

