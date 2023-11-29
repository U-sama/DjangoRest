from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    my_url_get_detail = serializers.SerializerMethodField(read_only = True)
    my_url_edit = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk') 
    # short cut for serializers.ModelSerializer

    #email = serializers.EmailField(write_only = True)
    
    # Add validators
    title = serializers.CharField(validators=[
        validators.validate_title_no_hello,
        validators.unique_product_title])
    
    #name = serializers.CharField(source="title", read_only=True)
    class Meta:
        model = Product
        fields = [
            #"email",
            #"name",
            "url",
            "my_url_get_detail",
            "my_url_edit",
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

# # Validate field
#     def validate_title(self, value):
#         requset = self.context.get("request")
#         user = requset.user

#         exists = Product.objects.filter(user=user, title__iexact=value) # "i" is for case insensitive
#         if exists:
#             raise serializers.ValidationError("This title already a product name.")
#         return value

    # pop the email in the view fo to view
    def create(self, validated_data):
        # print(validated_data)
        # email = validated_data.pop("email")
        # print("After pop")
        # print(validated_data)
        # print(f"Email: {email}")
        obj = super().create(validated_data)
        return obj
    
    def update(self, instance, validated_data): 
        email = validated_data.pop("email")
        return super().update(instance, validated_data)

    def get_my_url_edit(self, obj):
        #return f"/api/products/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)
    
    def get_my_url_get_detail(self, obj):
        #return f"/api/products/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
