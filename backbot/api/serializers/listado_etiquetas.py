from backbot.models import ListadoEtiquetas
from rest_framework import serializers


class ListadoEtiquetasSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ListadoEtiquetas
        fields = [
            "id",
            "valor_etiqueta",
            "observacion",
            "color",
        ]
