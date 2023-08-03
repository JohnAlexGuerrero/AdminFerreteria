from django.contrib import admin

from inventory.models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('bar_code','name','stock','unit_measure','cost')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','items')
    
    ordering = ('name',)

    def items(self, obj):
        return Product.objects.filter(category__name=obj.name).count()
