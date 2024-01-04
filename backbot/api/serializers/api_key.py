from backbot.models import ApiKey
from rest_framework import serializers


class ApiKeySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ApiKey
        fields = ["id", "key"]

    def validate(self, data):
        if ApiKey.objects.count() >= 1:
            raise serializers.ValidationError("Row limit exceeded")
        return data
