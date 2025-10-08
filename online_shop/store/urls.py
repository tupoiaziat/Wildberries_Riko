from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'productimages', ProductImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('sub_category', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='sub_category_detail'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail')
]
