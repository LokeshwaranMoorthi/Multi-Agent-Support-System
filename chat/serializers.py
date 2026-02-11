from rest_framework import serializers
from .models import Conversation, Message, Order, Invoice

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['role', 'content', 'agent_type', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = ['id', 'created_at', 'messages']