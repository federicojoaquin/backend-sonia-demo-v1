from abc import ABC, abstractmethod
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.pagination import LimitOffsetPagination
from ...utils.db_utils import get_latest_conversations
import json
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import reverse


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class BaseConversationsView(APIView):
    pagination_class = CustomPagination

    def get_paginated_conversations(self, request, id_conversation=None):
        data = get_latest_conversations(connection, id_conversation)

        # Apply pagination
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_queryset(data, request)

        return paginator.get_paginated_response(paginated_data)


class ConversationsGetView(BaseConversationsView):
    def get(self, request, id_conversation=None, format=None):
        return self.get_paginated_conversations(request, id_conversation)


class ConversationsPutView(BaseConversationsView):
    def put(self, request, id_conversation, format=None):
        user = request.user
        print(f"User: {user}")

        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid JSON data provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tag_id = request_data.get("tag_id")
        flag_assistant_human = request_data.get("flag_assistant_human")

        if tag_id is not None:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE conversations
                        SET tag_id = %s
                        WHERE id_conversation = %s
                        """,
                        [tag_id, id_conversation],
                    )
            except IntegrityError as e:
                return Response(
                    {"error": "Database error: " + str(e.__cause__)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        elif flag_assistant_human is not None:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE conversations
                        SET flag_assistant_human = %s
                        WHERE id_conversation = %s
                        """,
                        [flag_assistant_human, id_conversation],
                    )
            except Exception as e:
                return Response(
                    {"error": "Database error: " + str(e.__cause__)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return self.get_paginated_conversations(request, id_conversation=None)
