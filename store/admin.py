from django.contrib import admin
from .models import Category, Product, ProductImage, ProductCategory, categoryImage

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name', 'price', 'description']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(categoryImage)


