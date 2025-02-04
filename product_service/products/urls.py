from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path("", ProductViewSet.as_view({"get": "list", "post": "create"})),  # List and create products
    path("<int:pk>/", ProductViewSet.as_view({"get": "retrieve"})),  # Retrieve a single product by ID
]
