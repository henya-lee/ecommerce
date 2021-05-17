from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories' # instead of showing Categorys
        ordering = ('ordering',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  #can get all the products when inside the category #and when delete category, also delete the product
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True) # 可以空白
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)

    image = models.ImageField(blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)   # editable=False

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print('Save', self.image.name)
        # self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0

# class ProductImage(models.Model):   #  part13
#     product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
#
#     image = models.ImageField(blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#         print('Save', self.image.name)
#         # self.thumbnail = self.make_thumbnail(self.image)
#
#         super().save(*args, **kwargs)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)