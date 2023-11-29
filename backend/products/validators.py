from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# #Validate field
# def validate_title(value):
#     exists = Product.objects.filter(title__iexact=value) # "i" is for case insensitive
#     if exists:
#         raise serializers.ValidationError("This title already a product name.")
#     return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("This title cannot contain hello.")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all())