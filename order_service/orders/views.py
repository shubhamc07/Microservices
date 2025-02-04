import requests
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied, APIException, NotFound


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Ensure user_id is extracted from the middleware (already decoded in the request)
        user_id = getattr(self.request, 'user_id', None)

        if not user_id:
            raise PermissionDenied({"detail": "User ID not found in token."})

        # Get product_id from the request data
        product_id = self.request.data.get('product_id')

        if not product_id:
            raise ValidationError({"detail": "Product ID is required."})

        # Validate product by calling the Product service
        product_url = f'http://127.0.0.1:8002/api/products/{product_id}/'
        
        try:
            product_response = requests.get(product_url, timeout=5)  # Timeout after 5 sec
            product_response.raise_for_status()  # Raise an error for non-200 responses
        except requests.exceptions.RequestException as e:
            raise APIException({"detail": f"Failed to connect to Product Service: {str(e)}"})

        # If product doesn't exist (404 or other errors), return an error
        if product_response.status_code == 404:
            raise NotFound({"detail": "Product not found."})

        # Save the order with the extracted user ID from JWT
        serializer.save(user_id=user_id)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
