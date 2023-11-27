import json
from django.forms.models import model_to_dict
#rom django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET", "POST",])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["title", "price", "sale_price"])
    return Response(data)






# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data["id"] = model_data.id
#         # data["title"] = model_data.title
#         # data["content"] = model_data.content
#         # data["price"] = model_data.price

#         # data = model_to_dict(model_data)
#         data = model_to_dict(model_data, fields=["title", "price"])

#     return JsonResponse(data)
#     #return HttpResponse(data)




# def api_home(request, *args, **kwargs):
#     body  = request.body #byte string of json data
#     print(body)

#     print(f"Query parameters: {request.GET}")
#     print(f"POST parameters: {request.POST}")
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass

#     #data["Headers"] = request.headers # will thow error
#     data["headers"] = dict(request.headers)
#     print(request.headers)
#     data["content_type"] = request.content_type
#     data["params"] = dict(request.GET)

#     print(data.keys())
#     return JsonResponse(data)