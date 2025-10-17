from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Home, Testimonial, Product_details,About

admin.site.register(Home)
admin.site.register(Testimonial)
admin.site.register(Product_details)
admin.site.register(About)
