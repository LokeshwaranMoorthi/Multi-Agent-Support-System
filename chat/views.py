from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation
from .serializers import ConversationSerializer


class ConversationListView(APIView):
    def get(self, request):
        conversations = Conversation.objects.all().order_by('-created_at')
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

class ConversationDetailView(APIView):
    def get(self, request, id):
        try:
            conversation = Conversation.objects.get(id=id)
            serializer = ConversationSerializer(conversation)
            return Response(serializer.data)
        except Conversation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"}, status=200)