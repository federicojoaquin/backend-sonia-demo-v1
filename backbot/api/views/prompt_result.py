from django.http import HttpResponse
from django.views import View
from django.db import connection
import json


class GetPromptResults(View):
    def get(self, request, id_conversation):
        with connection.cursor() as cursor:
            query = """
            SELECT resultadoprompt
            FROM (
               SELECT DISTINCT id_conversation, idprompt, promptgenerado1, resultadoprompt
               FROM prompts_sentimiento ps 
               WHERE id_conversation = %s
               ORDER BY idprompt
            ) AS subquery_alias;"""
            cursor.execute(query, [id_conversation])
            result = cursor.fetchall()
        if result is None:
            result = "No result found for this id_conversation"
        else:
            # Convert each JSON string in the result list into a dictionary
            result = [json.loads(r[0]) for r in result]
        return HttpResponse(json.dumps(result), content_type="application/json")
