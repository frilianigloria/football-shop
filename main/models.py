from django.db import models
import uuid

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('clothing', 'Clothing'),
        ('gears', 'Gears'),
        ('bags', 'Bags'),
        ('accessories', 'Accessories'),
        ('balls', 'Balls'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='clothing')
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 50
    
    def increment_views(self):
        self.product_views += 1
        self.save()