from django.contrib import admin
from .models import Product, Person
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'main_price', 'wheight', 'supplier', 'unit_qnt', 'retail_qnt', 'group', 'observation']
    def view_name(self, obj):
        return obj.name

class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'doc_type', 'doc_id1', 'doc_id2', 'extern_code', 'since']

    def view_name(self, obj):
        return obj.name

admin.site.register(Product, ProductAdmin)
admin.site.register(Person, PersonAdmin)
