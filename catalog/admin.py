from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin
from catalog.models import Catalog, Product

class CatalogAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

admin.site.register(Catalog, CatalogAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
    # specify pixel amount for this ModelAdmin only:
   #mptt_level_indent = 20

admin.site.register(Product, ProductAdmin)
