import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')

        print(f"Authorization Header: {auth_header}")  # Debugging

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({"error": "Unauthorized"}, status=401)

        token = auth_header.split(' ')[1]

        try:
            # Decode the JWT token using the same secret key
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            request.user_id = decoded_token.get("user_id")

            print(f"Decoded Token: {decoded_token}")  # Debugging

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)
        except TokenError:
            return JsonResponse({"error": "Error with token processing"}, status=401)

        return self.get_response(request)
