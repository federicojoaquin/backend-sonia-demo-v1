from django.db import models


class BotSettings(models.Model):
    salesperson_name = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50)
    company_business = models.CharField(max_length=1800)
    company_values = models.CharField(max_length=1800)
    conversation_purpose = models.CharField(max_length=1800)
    salesperson_rol = models.CharField(max_length=25)
    conversation_type = models.CharField(max_length=20)
    conversation_stage = models.CharField(max_length=1800)

    def __str__(self):
        return self.salesperson_name


class ApiKey(models.Model):
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.key


class ListadoEtiquetas(models.Model):
    valor_etiqueta = models.CharField(max_length=50, unique=True)
    observacion = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=15, unique=True, null=True)

    def __str__(self):
        return self.key
