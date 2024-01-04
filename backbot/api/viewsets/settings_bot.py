from backbot.api.serializers.settings_bot import BotSettingsSerializer
from backbot.models import BotSettings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BotSettingsViewSet(viewsets.ModelViewSet):
    queryset = BotSettings.objects.all()
    serializer_class = BotSettingsSerializer
    # permission_classes = [IsAuthenticated]
