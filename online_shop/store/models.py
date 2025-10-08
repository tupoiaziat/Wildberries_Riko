from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(14),
                                                  MaxValueValidator(70)],
                                      null=True, blank=True)
    phone_number = PhoneNumberField()
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class Category(models.Model):
    category_image = models.ImageField(upload_to='category_image')
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='sub_categories')
    subcategory_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=64)
    price = models.PositiveSmallIntegerField()
    article_number = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    product_type = models.BooleanField()

    def __str__(self):
        return  f'{self.product_name} - {self.price}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='images/')

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.CharField(max_length=1, choices=[(str(i), str(i)) for i in range(1, 6)])
    created_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.stars

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.product

