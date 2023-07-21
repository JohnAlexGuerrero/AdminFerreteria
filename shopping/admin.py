from django.contrib import admin

from shopping.models import Providers, Invoice, ProductInvoice

class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('number','provider','created_at','expiration_at','total')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('invoice','product','quantity','price')

admin.site.register(Providers) 
admin.site.register(Invoice, InvoicesAdmin) 
admin.site.register(ProductInvoice, InventoryAdmin) 
