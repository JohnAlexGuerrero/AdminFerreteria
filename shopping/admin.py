from django.contrib import admin
from datetime import datetime

from shopping.models import Providers, Invoice, ProductInvoice

# admin invoices
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('number','provider','created_at','expiration_at','total','days')
    
    ordering = ('created_at',)
    
    def days(self, obj):
        now = datetime.now()
        days = (datetime.strptime(str(obj.expiration_at), "%Y-%m-%d") - now).days
        return days

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('invoice','product','quantity','price')
    


admin.site.register(Providers) 
admin.site.register(Invoice, InvoicesAdmin) 
admin.site.register(ProductInvoice, InventoryAdmin) 
