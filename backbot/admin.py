from backbot.models import BotSettings
from backbot.models import ApiKey
from backbot.models import ListadoEtiquetas
from django.contrib import admin


# Register your models here.
@admin.register(BotSettings)
class BotSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(ListadoEtiquetas)
class ListadoEtiquetasAdmin(admin.ModelAdmin):
    pass
