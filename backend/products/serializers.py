from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    my_url_get_detail = serializers.SerializerMethodField(read_only = True)
    my_url_edit = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk') 
    # short cut for serializers.ModelSerializer
    class Meta:
        model = Product
        fields = [
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
