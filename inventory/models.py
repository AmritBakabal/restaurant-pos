# Create your models here.

from django.db import models


class Ingredient(models.Model):

    class Unit(models.TextChoices):
        GRAM = "g", "Gram"
        MILLILITER = "ml", "Milliliter"
        PIECE = "piece", "Piece"

    name = models.CharField(max_length=150)

    unit = models.CharField(
        max_length=10,
        choices=Unit.choices,
    )

    current_stock = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
    )

    low_stock_threshold = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.unit})"

    class Meta:
        ordering = ["name"]


# Connect menu products to their ingredients

class RecipeIngredient(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="recipe_ingredients",
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        related_name="used_in_recipes",
    )

    quantity_required = models.DecimalField(
        max_digits=12,
        decimal_places=3,
    )

    def __str__(self):
        return (
            f"{self.quantity_required} {self.ingredient.unit} "
            f"{self.ingredient.name} for {self.product.name}"
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "ingredient"],
                name="unique_product_ingredient",
            ),
            models.CheckConstraint(
                check=models.Q(quantity_required__gt=0),
                name="recipe_quantity_positive",
            ),
        ]

