from django.urls import path, include
from rest_framework import routers
from bakery.views import CustomerProductListView, ProductModelViewSet

router = routers.SimpleRouter()
router.register(r'vendor/product', ProductModelViewSet)


urlpatterns = [
    path('^customer/product', CustomerProductListView.as_view()),
]

urlpatterns += router.urls