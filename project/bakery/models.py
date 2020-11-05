from django.db import models
from django.contrib.auth.models import User
from core.models import DateCreatedUpdatedTimeMixin
# Create your models here.


class Bakery(DateCreatedUpdatedTimeMixin):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created",)


class Ingredient(DateCreatedUpdatedTimeMixin):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    @staticmethod
    def is_ingredient_exists(name: str) -> bool:
        return Ingredient.objects.filter(name__iexact=name).exists()


class Product(DateCreatedUpdatedTimeMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    is_vegetarian = models.BooleanField(default=False)
    # image = models.ImageField(upload_to="")
    cost = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("name", "bakery")


class ProductIngredient(DateCreatedUpdatedTimeMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    percentage = models.FloatField()
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("product", "ingredient")