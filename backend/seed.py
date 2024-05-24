# # ecommerce-backend/seed.py
# import os
# import django

# # 設置 Django 環境
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()

# from django.contrib.auth import get_user_model

# User = get_user_model()

# def create_user(username, email, password, role):
#     if not User.objects.filter(username=username).exists():
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )
#         user.role = role
#         user.save()
#         print(f'User {username} created with role {role}.')

# def seed():
#     users = [
#         {'username': 'admin_user', 'email': 'admin_user@example.com', 'password': 'adminpass', 'role': 'admin'},
#         {'username': 'store_manager_user', 'email': 'store_manager@example.com', 'password': 'storepass', 'role': 'store_manager'},
#         {'username': 'product_manager_user', 'email': 'product_manager@example.com', 'password': 'productpass', 'role': 'product_manager'},
#         {'username': 'order_manager_user', 'email': 'order_manager@example.com', 'password': 'orderpass', 'role': 'order_manager'},
#         {'username': 'customer_support_user', 'email': 'customer_support@example.com', 'password': 'supportpass', 'role': 'customer_support'},
#         {'username': 'finance_manager_user', 'email': 'finance_manager@example.com', 'password': 'financepass', 'role': 'finance_manager'},
#         {'username': 'marketing_specialist_user', 'email': 'marketing_specialist@example.com', 'password': 'marketingpass', 'role': 'marketing_specialist'},
#     ]

#     for user in users:
#         create_user(user['username'], user['email'], user['password'], user['role'])

# if __name__ == '__main__':
#     seed()
import os
import django
from django.contrib.auth import get_user_model

# 设置 Django 环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import BusinessUser

def create_business_users():
    users = [
        {'username': 'admin', 'email': 'admin@ecommerce.com', 'role': 'admin'},
        {'username': 'manager', 'email': 'manager@ecommerce.com', 'role': 'store_manager'},
        {'username': 'product', 'email': 'product@ecommerce.com', 'role': 'product_manager'},
        {'username': 'order', 'email': 'order@ecommerce.com', 'role': 'order_manager'},
        {'username': 'support', 'email': 'support@ecommerce.com', 'role': 'customer_support'},
        {'username': 'finance', 'email': 'finance@ecommerce.com', 'role': 'finance_manager'},
        {'username': 'marketing', 'email': 'marketing@ecommerce.com', 'role': 'marketing_specialist'},
    ]
    
    for user in users:
        if not BusinessUser.objects.filter(username=user['username']).exists():
            BusinessUser.objects.create(**user)

def create_superuser():
    User = get_user_model()
    superuser_username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    superuser_email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')

    if not User.objects.filter(username=superuser_username).exists():
        User.objects.create_superuser(superuser_username, superuser_email, superuser_password)

if __name__ == '__main__':
    create_business_users()
    create_superuser()
