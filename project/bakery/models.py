from django.db import models
from django.contrib.auth.models import User
from core.models import DateCreatedUpdatedTimeMixin
from bakery.managers import ProductManager
# Create your models here.


class Bakery(DateCreatedUpdatedTimeMixin):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Bakery \"{self.name}\" owned by {self.owner.get_full_name()}"

    @property
    def products(self):
        return Product.objects.select_related("bakery").filter(bakery_id=self.id)

    @property
    def ingredients(self):
        return Ingredient.objects.select_related("bakery").filter(bakery_id=self.id)


class Ingredient(DateCreatedUpdatedTimeMixin):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name="ingredient")
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField()

    class Meta:
        unique_together = ("bakery", "name")

    @staticmethod
    def is_ingredient_exists(name: str) -> bool:
        return Ingredient.objects.filter(name__iexact=name).exists()

    def __str__(self):
        return f"Ingredient {self.name} listed by {self.bakery}"

class Product(DateCreatedUpdatedTimeMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    is_vegetarian = models.BooleanField(default=False)
    # image = models.ImageField(upload_to="")
    cost = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    objects = ProductManager()

    class Meta:
        unique_together = ("name", "bakery")

    @property
    def ingredients(self):
        return ProductIngredient.objects.select_related("product", "ingredient").filter(
            product_id=self.id).values(
                "ingredient__name","ingredient__description", "percentage", "quantity")

    def __str__(self):
        return f"Product {self.name} listed by {self.bakery.name}"

class ProductIngredient(DateCreatedUpdatedTimeMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    percentage = models.FloatField()
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("product", "ingredient")