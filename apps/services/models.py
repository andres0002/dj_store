from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    img = models.ImageField(upload_to='services/', max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['name']
    
    def __str__(self):
        return self.name