# py
# django
from django.db import models
# from django.db.models import F, Sum, FloatField
from django.db.models import Sum, FloatField
# third
# own
from apps.store.models import Products
from apps.user.models import Users

# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['pk']
    
    def __str__(self):
        return f'Order -> {self.pk}'
    
    @property
    def total(self):
        # en tiempo real hacer el calculo. mas consumo de recursos.
        # return self.ordersline_set.aggregate(
        #     total = Sum(F('price') * F('amount'), output_field = FloatField())
        # )['total'] or 0.00
        # suma directa si ya se tiene el campo caulcualdo anteriormente en ordersline. menos consumo de recursos.
        return self.ordersline_set.aggregate(
            total = Sum('total', output_field=FloatField())
        )['total'] or 0.00

class OrdersLine(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    amount = models.IntegerField(default=1)
    total = models.FloatField(default=0.00)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Order Line'
        verbose_name_plural = 'Orders Line'
        ordering = ['pk']
    
    def __str__(self):
        return f'{self.amount} units of {self.product.name}'
    
    def save(self, *args, **kwargs):
        if self.product and self.amount:
            self.price = self.product.price
            self.total = self.price * self.amount
        return super().save(*args, **kwargs)