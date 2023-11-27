from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

#class ProductCreateAPIView(generics.CreateAPIView): #Only create products
class ProductListCreateAPIView(generics.ListCreateAPIView): # will create if it's POST and return all if GET
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        
        if content is None:
            content = title
        serializer.save(content=content, )

class productDetailsAPIView(generics.RetrieveAPIView): # this will get the data from the model according to the id provided
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'id'

product_detail_view = productDetailsAPIView.as_view()


# you can make all the logic on one view but its very not recommended
@api_view(["GET", "POST",])
def product_alt_view(request, pk=None,*args, **kwargs):
    method = request.method

    if method == "GET":
        #url_arg ???
        #get detail view
        if pk is not None:
            instance = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(instance, many=False).data
            return Response(data)
        #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    elif method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #instance = serializer.save()
            #print(instance)
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content, )
            #print(serializer.data)
            return Response(serializer.data)

    