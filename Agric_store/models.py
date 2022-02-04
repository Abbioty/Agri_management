from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='media/product_img')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug],)





