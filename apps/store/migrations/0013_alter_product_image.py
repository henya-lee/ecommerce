# Generated by Django 3.2 on 2021-05-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
