from django.db import models
import uuid

class Order(models.Model):
    order_id = models.CharField(max_length=100, primary_key=True)
    status = models.CharField(max_length=50) 
    item = models.CharField(max_length=200)

class Invoice(models.Model):
    invoice_id = models.CharField(max_length=100, primary_key=True)
    amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    role = models.CharField(max_length=50) # 'user' or 'assistant'
    agent_type = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)