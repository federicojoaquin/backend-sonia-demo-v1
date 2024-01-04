from backbot.api.serializers.listado_etiquetas import ListadoEtiquetasSerializer
from backbot.models import ListadoEtiquetas
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ListadoEtiquetasViewSet(viewsets.ModelViewSet):
    queryset = ListadoEtiquetas.objects.all()
    serializer_class = ListadoEtiquetasSerializer
    # permission_classes = [IsAuthenticated]
