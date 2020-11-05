from rest_framework.exceptions import APIException
from rest_framework import status

class IngredientAlreadyExistsException(APIException):

    default_code  = "BAKERY_0001_INGREDIENT_ALREADY_EXISTS"
    default_detail = "INGREDIENT_ALREADY_EXISTS"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)