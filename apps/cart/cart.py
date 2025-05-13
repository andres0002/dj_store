# py
# django
# third
# own

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get('cart', {})
        if not self.cart:
            self.__save_cart()
    
    def __save_cart(self, clean_cart=False):
        if clean_cart:
            self.session['cart'] = {}
        else:
            self.session['cart'] = self.cart
        self.session.modified = True
    
    def add(self, product):
        if str(product.pk) not in self.cart.keys():
            self.cart[str(product.pk)] = {
                'pk': product.pk,
                'name': product.name,
                'price': str(product.price),
                'amount': 1,
                'img': product.img.url,
                'total': str(product.price)
            }
            self.__save_cart()
        else:
            self.cart[str(product.pk)]['amount'] += 1
            self.cart[str(product.pk)]['total'] = float(self.cart[str(product.pk)]['price']) * self.cart[str(product.pk)]['amount']
            self.__save_cart()
    
    def delete(self, product):
        if str(product.pk) in self.cart.keys():
            del self.cart[str(product.pk)]
            self.__save_cart()
    
    def subtract(self, product):
        if str(product.pk) in self.cart.keys():
            self.cart[str(product.pk)]['amount'] -= 1
            self.cart[str(product.pk)]['total'] = float(self.cart[str(product.pk)]['price']) * self.cart[str(product.pk)]['amount']
            if self.cart[str(product.pk)]['amount'] < 1:
                self.delete(product)
            self.__save_cart()
    
    def clean(self):
        self.__save_cart(True)