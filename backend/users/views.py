from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from pydantic import ValidationError
from .schemas import BusinessUserSchema
from .models import BusinessUser

def create_business_user(request):
    try:
        data = BusinessUserSchema.model_validate_json(request.body)
        user = BusinessUser.objects.create(**data.model_dump())
        return JsonResponse({'message': 'User created successfully', 'user': user.id}, status=201)
    except ValidationError as e:
        return JsonResponse({'errors': e.errors()}, status=400)
