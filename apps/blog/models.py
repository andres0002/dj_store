# django
from django.db import models
from django.core.exceptions import ValidationError
# third
from ckeditor.fields import RichTextField
# own

# Create your models here.

class Categories(models.Model):
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
        if Categories.objects.filter(name__iexact=self.name).exclude(id=self.id).exists():
            raise ValidationError({
                'name': "Ya existe una categoría con ese nombre (sin importar mayúsculas, minúsculas y espacios al inicio o al final)."
            })
    
    def seve(self, *args, **kwargs):
        self.name = self.name.strip() # normaliza el valor -> quita espacios al inicio y al final.
        self.full_clean() # Ejecuta clean() antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Authors(models.Model):
    name = models.CharField('Name', max_length=150, null=False, blank=False)
    lastname = models.CharField('Lastname', max_length=150, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    email = models.EmailField('Email', null=False, blank=False, unique=True)
    condition = models.BooleanField('Active/Deactivated', default=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    update_date = models.DateTimeField('Update Date', auto_now=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        unique_together = ('name', 'lastname')  # para que al author sea unico
        ordering = ['name']

    def __str__(self):
        return f'{self.lastname} {self.name}'

class Posts(models.Model):
    title = models.CharField('Title', max_length=100, null=False, blank=False, unique=True)
    slug = models.CharField('Slug', max_length=150, null=False, blank=False, unique=True)
    description = models.CharField('Description', max_length=200, null=False, blank=False)
    content = RichTextField('Content')
    image = models.URLField('URL of Image', max_length=300, null=False, blank=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories)
    condition = models.BooleanField('Publicationed/Not Publicationed', default=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    update_date = models.DateTimeField('Update Date', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title']

    def save(self, *args, **kwargs):
        # Reemplazar espacios en slug por "_"
        if self.slug:
            self.slug = self.slug.strip().replace(' ', '_')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_categories(self):
        return ", ".join([str(c) for c in self.categories.all()])