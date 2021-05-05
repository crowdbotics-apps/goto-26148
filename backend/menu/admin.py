from django.contrib import admin
from .models import ItemVariant, Country, Item, Category, Review

admin.site.register(ItemVariant)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Review)

# Register your models here.
