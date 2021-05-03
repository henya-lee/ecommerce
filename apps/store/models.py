from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories' # instead of showing Categorys

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  #can get all the products when inside the category #and when delete category, also delete the product
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True) # 可以空白
    price = models.FloatField()


    def __str__(self):
        return self.title