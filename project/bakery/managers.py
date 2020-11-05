from django.db import models


class ProductManager(models.Manager):

    def only_active_products(self):
        return super().get_queryset().filter(is_active=True)