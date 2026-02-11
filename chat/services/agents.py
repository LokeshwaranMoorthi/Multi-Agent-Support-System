import os
import re
from groq import Groq
from ..models import Order, Invoice

client = Groq(api_key="GROQ_API_KEY")

class MultiAgentSystem:
    def process_query(self, query):
        # 1. Router Agent - Decides which agent to use
        route_prompt = f"Categorize query into ORDER, BILLING, or SUPPORT. Query: {query}. Return ONLY the word."
        category = client.chat.completions.create(
            messages=[{"role": "user", "content": route_prompt}],
            model="llama-3.3-70b-versatile"
        ).choices[0].message.content.strip().upper()

        # 2. Extract ID using Regex (Finding ORDXXX or INVXXX)
        order_match = re.search(r'ORD-\d+|ORD\d+', query.upper())
        invoice_match = re.search(r'INV-\d+|INV\d+', query.upper())

        # 3. Sub-Agent Logic with REAL Database Queries
        if "ORDER" in category:
            if order_match:
                order_id = order_match.group()
                result = self.get_order_status(order_id)
                return "Order Agent", result
            return "Order Agent", "Please provide a valid Order ID (e.g., ORD101)."

        elif "BILLING" in category:
            if invoice_match:
                inv_id = invoice_match.group()
                result = self.get_invoice_status(inv_id)
                return "Billing Agent", result
            return "Billing Agent", "Please provide a valid Invoice ID (e.g., INV-5001)."

        else:
            return "Support Agent", "I'm here to help! Could you please specify your order or billing concern?"

    def get_order_status(self, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
            return f"Order {order_id} ({order.item}) is currently {order.status}."
        except Order.DoesNotExist:
            return f"Sorry, I couldn't find any record for Order {order_id}."

    def get_invoice_status(self, inv_id):
        try:
            inv = Invoice.objects.get(invoice_id=inv_id)
            status = "Paid" if inv.is_paid else "Unpaid"
            return f"Invoice {inv_id} for ${inv.amount} is currently {status}."
        except Invoice.DoesNotExist:
            return f"Invoice {inv_id} was not found in our records."