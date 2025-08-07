from openai import OpenAI
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Ask the skincare chatbot a question",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING, description='User question'),
            },
            required=['question']
        ),
        responses={200: openapi.Response("Chatbot response", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING),
                'answer': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ))}
    )
    def post(self, request):
        user_question = request.data.get("question", "")

        if not user_question:
            return Response({"error": "Question is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful skincare assistant."},
                    {"role": "user", "content": user_question}
                ]
            )
            answer = response.choices[0].message.content
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "question": user_question,
            "answer": answer
        }, status=status.HTTP_200_OK)
