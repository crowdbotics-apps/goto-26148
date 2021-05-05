from django.contrib import admin
from .models import Order, PaymentMethod, Bill

admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(PaymentMethod)

# Register your models here.
