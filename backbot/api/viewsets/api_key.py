from rest_framework import viewsets
from backbot.models import ApiKey
from backbot.api.serializers.api_key import ApiKeySerializer


class ApiKeyViewSet(viewsets.ModelViewSet):
    queryset = ApiKey.objects.all()
    serializer_class = ApiKeySerializer
    http_method_names = ["get", "put", "post"]
