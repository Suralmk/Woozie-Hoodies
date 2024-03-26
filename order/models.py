from django.db import models
from shop.models import Product
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid

User = get_user_model()
class Order(models.Model):
    id = models.SlugField(primary_key=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=13)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    tx_ref = models.SlugField(max_length=100, blank=True)

    class Meta:
        ordering = ['-created']
        indexes = [
        models.Index(fields=['-created']),
        ]

    def __str__(self):
            return f'Order {self.id}'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_slug_id()
        super().save(*args, **kwargs)

    def generate_slug_id(self):
        id = uuid.uuid4().hex[:6]
        return id
        
    def get_total_cost(self):
            return sum(item.get_cost() for item in self.items.all())
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity