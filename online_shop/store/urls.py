from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productimages', ProductImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
