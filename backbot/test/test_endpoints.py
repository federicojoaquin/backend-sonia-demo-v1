import json
from datetime import datetime
import django
import os
from dotenv import load_dotenv

django.setup()
import pytest
from django.db import connection
from django.urls import reverse
from pytest import approx
from rest_framework import status

from backbot.api.serializers.api_key import ApiKeySerializer

from backbot.models import (
    BotSettings,
    ApiKey,
    ListadoEtiquetas,
)

import pytest

from core import settings


@pytest.fixture(scope="function")
def django_db_setup():
    print(f"DATABASE_ENGINE: {os.getenv('DATABASE_ENGINE')}")
    print(f"DATABASE_NAME: {os.getenv('DATABASE_NAME')}")
    print(f"DATABASE_USER: {os.getenv('DATABASE_USER')}")
    print(f"DATABASE_PASSWORD: {os.getenv('DATABASE_PASSWORD')}")
    print(f"DATABASE_HOST: {os.getenv('DATABASE_HOST')}")
    print(f"DATABASE_PORT: {os.getenv('DATABASE_PORT')}")
    settings.DATABASES["default"] = {
        "ENGINE": os.getenv("DATABASE_ENGINE"),
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
        "ATOMIC_REQUESTS": True,  # Add this line
    }


@pytest.mark.django_db
def test_insert_botsettings(api_client):
    data = {
        "salesperson_name": "sarasa1",
        "company_name": "name",
        "company_business": "sarasa2",
        "company_values": "sarasa3",
        "conversation_purpose": "sarasa4",
        "salesperson_rol": "sarasa5",
        "conversation_type": "sarasa6",
        "conversation_stage": "sarasa7",
    }

    url = reverse("bot-settings-list")
    response_post = api_client.post(url, data, format="json")

    assert response_post.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_insert_apikey(api_client):
    data = {
        "key": "cacacacacaacacacac",
    }

    url = reverse("api-key-list")
    response_post = api_client.post(url, data, format="json")

    assert response_post.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_insert_morethanone_apikey(api_client):
    data = {
        "key": "cacacacacaacacacac",
    }

    data1 = {
        "key": "cacacacacaacacacac2",
    }

    data2 = {
        "key": "cacacacacaacacacac3",
    }

    data3 = {
        "key": "cacacacacaacacacac4",
    }

    url = reverse("api-key-list")
    response_post = api_client.post(url, data, format="json")

    assert response_post.status_code == status.HTTP_201_CREATED

    response_post1 = api_client.post(url, data1, format="json")
    response_post2 = api_client.post(url, data2, format="json")
    response_post3 = api_client.post(url, data3, format="json")

    assert response_post1.status_code == 400
    assert response_post2.status_code == 400
    assert response_post3.status_code == 400


@pytest.mark.django_db
def test_labels(api_client):
    url = reverse("labels-list-list")

    data = {"valor_etiqueta": "sarasa1", "observacion": "sarasa2", "color": "sarasa3"}
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    label = ListadoEtiquetas.objects.get(color="sarasa3")
    assert label.valor_etiqueta == "sarasa1"

    labels_response = api_client.get(url, format="json")
    assert labels_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_put_label(api_client):
    with connection.cursor() as cursor:
        cursor.execute(
            """
               SELECT c.id_conversation,
               c.fechaalta,
               c.number_cel,
               c.conversation_history, 
               c.state, 
               c.flag_assistant_human, 
               c.tag, 
               c.tag_id
               FROM conversations c
			   limit 1 offset 0 
        """
        )
        conversation = cursor.fetchone()

    url = reverse("conversations", args=[conversation[0]])

    data_tag = {"tag_id": 3}

    response = api_client.put(url, data=data_tag, format="json")
    assert response.status_code == 200

    with connection.cursor() as cursor:
        cursor.execute(
            """
                   SELECT 
                   c.tag_id
                   FROM conversations c
    			   WHERE c.id_conversation = %s 
            """,
            [conversation[0]],
        )

        tag = cursor.fetchone()

    assert tag[0] == data_tag["tag_id"]
