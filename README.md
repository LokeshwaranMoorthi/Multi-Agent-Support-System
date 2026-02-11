# 🚀 Swades AI: Multi-Agent Support System

A high-performance, real-time customer support platform featuring an AI Orchestrator that dynamically routes queries to specialized agents. Built with a modern Django-React stack and powered by Groq's Llama-3-70B.

## 🏗️ Architectural Overview

The system follows a **Router-Worker pattern**. Instead of a single prompt handling everything, an Orchestrator analyzes intent and delegates tasks to specialized agents grounded in a relational database.

## 🌟 Key Features

- **Intelligent Routing**: Orchestrator identifies intent (Orders vs. Billing) to reduce token noise and increase accuracy.
- **Deterministic Grounding**: Sub-agents use Django ORM to query real data (Order status, Invoice amounts), eliminating AI hallucinations.
- **Real-time Communication**: Built on Django Channels & WebSockets for low-latency chat and live "typing" states.
- **Premium UI/UX**: A React-based glassmorphic interface with smooth CSS transitions and auto-scroll logic.

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **LLM Inference** | Groq Cloud (Llama-3-70B-Versatile) |
| **Backend** | Python 3.10+, Django, Django Rest Framework |
| **Real-time** | ASGI, Daphne, Django Channels |
| **Frontend** | React.js, WebSockets |
| **Database** | SQLite (Relational grounding) |

## 🚦 Getting Started

### 1. Prerequisites
- Python 3.10+
- Node.js & npm
- [Groq API Key](https://console.groq.com/keys)

### 2. Backend Setup
```bash
# Clone the repository
git clone https://github.com/LokeshwaranMoorthi/Multi-Agent-Support-System.git
cd Multi-Agent-Support-System

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your Groq API key: GROQ_API_KEY=your_key_here

# Run migrations & seed data
python manage.py migrate
python seed_data.py

# Start the ASGI server
python manage.py runserver
