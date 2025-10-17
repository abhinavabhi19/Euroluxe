from django.db import models

class Home(models.Model):
    banner_video = models.FileField(upload_to="banner_video/")

    product1_image = models.ImageField(upload_to='product/')
    product1_video = models.FileField(upload_to='product/')

    product2_image = models.ImageField(upload_to='product/')
    product2_video = models.FileField(upload_to='product/')

    product3_image = models.ImageField(upload_to='product/')
    product3_video = models.FileField(upload_to='product/')

 


class About(models.Model):
    product1_image = models.ImageField(upload_to='product/')
    product1_video = models.FileField(upload_to='product/')

    product2_image = models.ImageField(upload_to='product/')
    product2_video = models.FileField(upload_to='product/')

    product3_image = models.ImageField(upload_to='product/')
    product3_video = models.FileField(upload_to='product/')




class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product_details(models.Model):


    rum70 = models.ImageField(upload_to='products/')
    vodka = models.ImageField(upload_to='products/', blank=True, null=True)
    whisky = models.ImageField(upload_to='products/', blank=True, null=True)
    rum50 = models.ImageField(upload_to='products/', blank=True, null=True)


    class Meta:
        verbose_name = "Product Detail"
        verbose_name_plural = "Product Details"
  
