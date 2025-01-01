from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

# Wrapper to override default OpenAPI schema

class WrapperTokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=255)

@extend_schema_view(
    post=extend_schema(
        request=WrapperTokenRefreshSerializer,
        description="Retrieve a new access token.",
    ),
)
class WrapperTokenRefreshView(TokenRefreshView):
    pass

class WrapperTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

@extend_schema_view(
    post=extend_schema(
        request=WrapperTokenObtainPairSerializer,
        description="Retrieve the token.",
    ),
)
class WrapperTokenObtainPairView(TokenObtainPairView):
    pass

