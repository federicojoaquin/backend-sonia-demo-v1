from backbot.models import BotSettings
from rest_framework import serializers


class BotSettingsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = BotSettings
        fields = [
            "id",
            "salesperson_name",
            "company_name",
            "company_business",
            "company_values",
            "conversation_purpose",
            "salesperson_rol",
            "conversation_type",
            "conversation_stage",
        ]
