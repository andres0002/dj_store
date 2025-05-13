def sum_total_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, product in request.session.get('cart', {}).items():
            total += float(product['total'])
    return {'sum_total_cart':total}