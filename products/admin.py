from django.contrib import admin
from products.models import Product, Offer

# Admin class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)

# Admin class for Offer
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')  # Fields to display in the list view
    list_filter = ('code','description')

# Registering both models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)


