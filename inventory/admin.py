# Register your models here.

from django.contrib import admin
from .models import Ingredient, RecipeIngredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit",
        "current_stock",
        "low_stock_threshold",
    )

    search_fields = ("name",)
    list_filter = ("unit",)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "ingredient",
        "quantity_required",
    )

    list_filter = ("product", "ingredient")
    search_fields = (
        "product__name",
        "ingredient__name",
    )
