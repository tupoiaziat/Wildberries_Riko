from rest_framework import serializers
from .models import UserProfile, Category, SubCategory, Product, ProductImage, Review, Cart, CartItem

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'status', 'created_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'article_number', 'description', 'image', 'video', 'subcategory']

class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'stars', 'created_data']

class CartSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'user']

class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']
