from django.contrib import admin

from inventory.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('bar_code','name','stock','unit_measure','cost',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

