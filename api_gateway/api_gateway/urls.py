from django.urls import path
from django.http import JsonResponse
import requests

BASE_URLS = {
    "users": "http://127.0.0.1:8001/api/users/",
    "products": "http://127.0.0.1:8002/api/products/",
    "orders": "http://127.0.0.1:8003/api/orders/",
}

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def proxy_request(request, service_name, endpoint=None):
    # Get the base URL for the service
    service_url = BASE_URLS.get(service_name)
    
    # If no URL for the service, return an error
    if not service_url:
        return JsonResponse({"error": "Invalid service"}, status=400)

    # If an endpoint is provided, append it to the service URL
    if endpoint:
        service_url += endpoint

    # Forward the request to the appropriate service
    response = requests.request(
        method=request.method,
        url=service_url,
        headers=request.headers,
        data=request.body,
    )
    return JsonResponse(response.json(), status=response.status_code)

# Define the URL patterns for API Gateway routing
urlpatterns = [
    # Users Service
    path("users/register/", proxy_request, {'service_name': 'users', 'endpoint': 'register/'}),
    path("users/login/", proxy_request, {'service_name': 'users', 'endpoint': 'login/'}),

    # Products Service
    path("products/", proxy_request, {'service_name': 'products', 'endpoint': ''}),

    # Orders Service
    path("orders/", proxy_request, {'service_name': 'orders', 'endpoint': ''}),
]
