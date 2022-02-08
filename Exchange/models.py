from django.db import models
from django.urls import reverse

# Create your models here.


class Exchange(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/Exchange_img')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exchange_detail', args=[self.slug],)





from django.db import models

# Create your models here.
