from django.contrib import admin
from ajanthaapp.models import Product , Category

# Register your models here.

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     # exclude = ('name', 'code')      # (Exclude these fields from admin panel)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     fields = ('name', 'code')         # (Only show these fields in admin panel)


admin.site.register(Product)
admin.site.register(Category)