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
    product_type = models.BooleanField()
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'{self.product_name} - {self.price}'

    def avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([int(i.stars) for i in ratings]) / ratings.count(), 1)
        return 0

    def count_people(self):
        ratings = self.reviews.all()
        return ratings.count()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='images/')

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.stars


