from django.db import models

from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length= 100, unique= True )
    price = models.DecimalField( max_digits= 10, decimal_places= 2 )
    image = models.URLField()
    release_date = models.DateField(auto_now_add=True )
    lte_exists = models.BooleanField(default= True)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

