from rest_framework.routers import DefaultRouter

from products.viewsets import productViewSet, ProductGenericViewSet


router = DefaultRouter()
#router.register('products', productViewSet, basename="products")
router.register('products', ProductGenericViewSet, basename="products")

print(router.urls)
urlpatterns = router.urls
