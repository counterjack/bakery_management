from django.urls import include, path
from rest_framework import routers

from bakery.views import (CustomerProductListView, IngredientModelViewSet,
                          ProductModelViewSet)

router = routers.SimpleRouter()
router.register(r'vendor/product', ProductModelViewSet)
router.register(r'vendor/ingredient', IngredientModelViewSet)


urlpatterns = [
    path('customer/product', CustomerProductListView.as_view()),
]

urlpatterns += router.urls
