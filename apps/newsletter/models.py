from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.email