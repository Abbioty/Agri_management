# Generated by Django 3.2 on 2021-12-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agric_store', '0004_auto_20211226_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/product_img'),
        ),
    ]