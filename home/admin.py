from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contact)

admin.site.register(Order)

admin.site.register(ViewCount)
admin.site.register(Category)

admin.site.register(Product)



