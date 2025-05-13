# py
# django
from django.db import models
from django.core.exceptions import ValidationError
# third
# own

# Create your models here.

class CategoriesProduct(models.Model):
    name = models.CharField('Name', max_length=100, blank=False, null=False, unique=True)
    condition = models.BooleanField('Active/Deactivated', default=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    update_date = models.DateTimeField('Update Date', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def clean(self):
        super().clean()
        # Buscar si ya existe otra categoría con el mismo nombre, sin importar mayúsculas o minusculas.
        if CategoriesProduct.objects.filter(name__iexact=self.name).exclude(id=self.id).exists():
            raise ValidationError({
                'name': "Ya existe una categoría con ese nombre (sin importar mayúsculas, minúsculas y espacios al inicio o al final)."
            })
    
    def seve(self, *args, **kwargs):
        self.name = self.name.strip() # normaliza el valor -> quita espacios al inicio y al final.
        self.full_clean() # Ejecuta clean() antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField('Name', max_length=100, blank=False, null=False, unique=True)
    category = models.ForeignKey(CategoriesProduct, on_delete=models.CASCADE)
    price = models.FloatField('Price')
    available = models.BooleanField('Available', default=True)
    amount = models.IntegerField('Amount')
    img = models.ImageField(upload_to='products/', blank=True, null=True)
    condition = models.BooleanField('Active/Deactivated', default=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    update_date = models.DateTimeField('Update Date', auto_now=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
    
    def clean(self):
        super().clean()
        # Buscar si ya existe otro product con el mismo nombre, sin importar mayúsculas o minusculas.
        if Products.objects.filter(name__iexact=self.name).exclude(id=self.id).exists():
            raise ValidationError({
                'name': "Ya existe un product con ese nombre (sin importar mayúsculas, minúsculas y espacios al inicio o al final)."
            })
    
    def seve(self, *args, **kwargs):
        self.name = self.name.strip() # normaliza el valor -> quita espacios al inicio y al final.
        self.full_clean() # Ejecuta clean() antes de guardar
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name