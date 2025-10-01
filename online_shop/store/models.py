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

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    subcategory_name = models.CharField(max_length=64, unique=True)

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    prodict_name = models.CharField(max_length=64)
    price = models.PositiveSmallIntegerField()
    article_number = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)

class ProductImage(models.Model):
    product = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.CharField(choices=[(i, str(i)) for i in range (1, 6)])
    created_data = models.DateField(auto_now_add=True)

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

