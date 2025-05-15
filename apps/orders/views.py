# py
import logging
# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
# third
# own
from apps.orders.models import Orders, OrdersLine
from apps.cart.cart import Cart
from apps.store.models import Products
from apps.base.utils.emails import send_email_gmail_with_email_message_for_order

# Create your views here.

logger = logging.getLogger(__name__)

@login_required(login_url='user:login')
def process_order(request, *args, **kwargs):
    cart = Cart(request)
    if not cart.cart:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:home')
    user = request.user
    full_name = f'{request.user.name.strip()} {request.user.lastname.strip()}'
    try:
        # para que no persista data en la DB si hay error ya sea en la creación de la order o de las ordes lines.
        with transaction.atomic():
            # create order
            order = Orders.objects.create(user=request.user)
            
            # Crear líneas de la orden
            product_ids = [item['pk'] for item in cart.cart.values()]
            products = Products.objects.in_bulk(product_ids)
            
            list_orders_line = []
            for key, product in cart.cart.items():
                # get product.
                product_object = products.get(product['pk'])
                if not product_object:
                    raise ValueError(f"Product with ID {product['pk']} not found.")
                
                list_orders_line.append(
                    OrdersLine(
                        user=user,
                        product=product_object,
                        order=order,
                        amount=product['amount'],
                        price=product['price'], # esta linea la puse por que el bulk_create no ejecuta el save del model.
                        total=product['total'] # esta linea la puse por que el bulk_create no ejecuta el save del model.
                    )
                )
            # create orders line.
            created_objects = OrdersLine.objects.bulk_create(list_orders_line)
            if not created_objects:
                raise ValueError("No order lines were created.")
        
        # Enviar correo (fuera de la transacción)
        list_orders_line = created_objects
        if len(created_objects) > 0:
            # send email
            ok, error = send_email_gmail_with_email_message_for_order(
                subject=f'Order User -> {full_name}',
                body={
                    'template_name':'order_email.html',
                    'order':order,
                    'orders_line':list_orders_line,
                    'email':user.email,
                    'full_name':full_name
                },
                to=[user.email],
                reply_to=[user.email]
            )
            # email ok.
            if ok:
                logger.info(f'Mail send successfully -> Username: {user.username.strip()}, Full Name: {full_name}, email: {user.email}.')
                request.session['cart'] = {}
                request.session.modified = True
                messages.success(request, 'SuccessFully Order creation.')
                return redirect('store:home')
            # email NO ok.
            else:
                logger.error(f'Mail send errorfully -> Username: {user.username.strip()}, Full Name: {full_name}, email: {user.email}, error: {error}.')
                messages.error(request, 'Errorful Order creation.')
                return redirect('cart:home')
    # si se presenta aogún error en el flujo normal.
    except Exception as error:
        logger.error(f'Error while processing order for user {user.username}, error:  {error}.')
        messages.error(request, 'Errorful Order creation.')
        return redirect('cart:home')