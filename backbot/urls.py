from backbot.api.viewsets.settings_bot import BotSettingsViewSet
from backbot.api.viewsets.api_key import ApiKeyViewSet
from backbot.api.viewsets.listado_etiquetas import ListadoEtiquetasViewSet
from backbot.api.views.conversations import ConversationsPutView, ConversationsGetView
from backbot.api.views.prompt_result import GetPromptResults
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"bot-settings", BotSettingsViewSet, basename="bot-settings")
router.register(r"api-key", ApiKeyViewSet, basename="api-key")
router.register(r"labels-list", ListadoEtiquetasViewSet, basename="labels-list")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "get-prompts-results/<str:id_conversation>",
        GetPromptResults.as_view(),
        name="get_prompt_results",
    ),
    path("conversations/", ConversationsGetView.as_view(), name="conversations"),
    path(
        "conversations/<str:id_conversation>",
        ConversationsPutView.as_view(),
        name="conversations",
    ),
]
