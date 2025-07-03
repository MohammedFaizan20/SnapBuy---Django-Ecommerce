from decimal import Decimal
from store.models import Product

class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def update(self, product, qty):
        product_id = str(product)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty

        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        # ✅ Remove orphaned items
        existing_ids = set(str(product.id) for product in products)

        for product_id in list(cart.keys()):
            if product_id not in existing_ids:
                del self.cart[product_id]
                self.session.modified = True

        # ✅ Add product objects
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item

    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def clear(self):
        # Clear the cart completely
        if 'cart' in self.session:
            del self.session['cart']
            self.session.modified = True
