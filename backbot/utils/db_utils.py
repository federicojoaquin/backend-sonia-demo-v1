from django.db import connection
import json
from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 10  # default number of items per page
    max_limit = 100  # maximum number of items per page


def get_latest_conversations(connection, id_conversation=None):
    with connection.cursor() as cursor:
        sql_query = """
           SELECT c.id_conversation,
           c.fechaalta,
           c.number_cel,
           c.conversation_history, 
           c.state, 
           c.flag_assistant_human, 
           c.tag, 
           c.tag_id
           FROM conversations c
           JOIN (
               SELECT id_conversation, MAX(fechaalta) AS max_fechaalta
               FROM conversations
               GROUP BY id_conversation
           ) subq ON c.id_conversation = subq.id_conversation AND c.fechaalta = subq.max_fechaalta
           ORDER BY c.fechaalta DESC;
       """
        params = []
        if id_conversation is not None:
            sql_query += " WHERE c.id_conversation = %s"
            params.append(id_conversation)
        cursor.execute(sql_query, params)
        rows = cursor.fetchall()

        # Convert the rows into a list of dictionaries
        data = [
            dict(zip([column[0] for column in cursor.description], row)) for row in rows
        ]

        # Convert the conversation_history field from a string representation of a list to an actual list
        for item in data:
            item["conversation_history"] = json.loads(item["conversation_history"])

        # Replace all occurrences of the \ character in the conversation_history field with an empty string
        for item in data:
            item["conversation_history"] = [
                text.replace("\\", "") for text in item["conversation_history"]
            ]

        return data
