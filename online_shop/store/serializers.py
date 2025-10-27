from rest_framework import serializers
from .models import UserProfile, Category, SubCategory, Product, ProductImage, Review

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'status', 'created_date']

class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']

class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'sub_categories']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ReviewSimpleSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'stars', 'created_data']

class ProductListSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSimpleSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'product_type', 'product_images', 'reviews', 'avg_rating', 'count_people']

    def avg_rating(self, object):
        return object.avg_rating()

    def count_people(self, object):
        return object.count_people()


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['subcategory_name', 'products']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'stars', 'created_data']

class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    sub_category = SubCategoryListSerializer()
    created_data = serializers.DateTimeField(format='%d-%m-%Y %H:%M',read_only=True, allow_null=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name', 'sub_category', 'price','product_images', 'article_number',
                  'product_type', 'reviews', 'created_data', 'avg_rating', 'count_people']

    def avg_rating(self, object):
        return object.avg_rating()

    def count_people(self, object):
        return object.count_people()



