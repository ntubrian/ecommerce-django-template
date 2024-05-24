from django.db import models

# Create your models here.
class BusinessUser(models.Model):
    ROLES = [
        ('admin', 'Admin'),
        ('store_manager', 'Store Manager'),
        ('product_manager', 'Product Manager'),
        ('order_manager', 'Order Manager'),
        ('customer_support', 'Customer Support'),
        ('finance_manager', 'Finance Manager'),
        ('marketing_specialist', 'Marketing Specialist'),
    ]

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'business_users'  # 指定表名