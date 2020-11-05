from bakery.models import Ingredient
from django.db.models.signals import pre_save
from django.dispatch import receiver
from bakery.exceptions import IngredientAlreadyExistsException


@receiver(pre_save, sender=Ingredient)
def check_ingredient_already_exists(sender, instance, raw: bool, **kwargs) -> None:

    if raw:
        return

    new_ingredient_name = instance.name
    ingredient_exists = Ingredient.is_ingredient_exists(new_ingredient_name)
    if (ingredient_exists):
        raise IngredientAlreadyExistsException
