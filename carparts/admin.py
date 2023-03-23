from django.contrib import admin

# Register your models here.
from .models import Product,Vehicle,Order,Order_detail,Customer

admin.site.register(Product)
admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Customer)