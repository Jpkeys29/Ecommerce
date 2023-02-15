from django.contrib import admin

# Register your models here.
from . models import Category, Product

# Creating a Class (so that we can use a prepopulated field):
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


#slug is a specific field and we are routing it to a specific product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


