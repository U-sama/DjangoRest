from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view(), name="product-list"),
    path("<int:pk>/", views.product_detail_view, name="product-detail"),
    path("<int:pk>/update/", views.productUpdateAPIView.as_view(), name="product-update"),
    path("<int:pk>/delete/", views.productDestroyAPIView.as_view())


#    path("", views.productMixinView.as_view()),
#    path("<int:pk>/", views.productMixinView.as_view()),

    #path("<int:pk>/", views.product_alt_view)
    #path("", views.product_alt_view),

]
