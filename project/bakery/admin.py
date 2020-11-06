from django.contrib import admin
from bakery.models import Bakery, ProductIngredient, Product, Ingredient
# Register your models here.

@admin.register(Bakery)
class BakeryAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "is_active", "created")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "bakery", "is_vegetarian", "cost", "selling_price", "is_active")


@admin.register(ProductIngredient)
class ProductIngredientAdmin(admin.ModelAdmin):
    list_display = ("product", "ingredient", "percentage", "quantity")


@admin.register(Ingredient)
class ProductIngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "bakery")