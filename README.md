# Cookbot



**Cookbot** is an AI-powered Indian cuisine assistant that acts as a digital cookbook and kitchen companion. It provides recipes, meal suggestions, leftover ideas, and dietary customizations (e.g., Jain, no onion-garlic) using Google's Gemini AI.

---

## Features

- **Recipe expert** — Step-by-step recipes for North Indian, South Indian, Gujarati, Maharashtrian, Bengali, Jain, and other regional cuisines
- **Meal planner** — Suggestions for balanced meals and food combinations
- **Leftover advisor** — Ideas for recipes using ingredients you already have
- **Dietary customization** — No onion-garlic, Jain, and healthier variants on request
- **Cultural context** — Optional fun facts and background about dishes

You can use Cookbot in two ways:

1. **CLI** — Interactive chat in the terminal (`bot.py`)
2. **Web app** — Browser-based chat with a welcome page and chat interface (`integration.py` + Flask)

---

## Project structure

```
Cookbot/
├── bot.py           # CLI chat interface (Gemini)
├── integration.py   # Flask app: web UI + /api/chat, /api/new-chat, /api/health
├── templates/
│   ├── frontend.html   # Welcome/landing page
│   └── page_2.html     # Chat page
├── .env              # API key (create from .env.example)
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Prerequisites

- **Python 3.8+**
- A **Google Gemini API key** from [Google AI Studio]  (https://makersuite.google.com/app/apikey)

---

## Setup

### 1. Clone or download the project

```bash
cd Cookbot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your key from Google AI Studio. Do not commit `.env` or share your key.

---

## Usage

### Option A: Command-line chat

Run the interactive terminal bot:

```bash
python bot.py
```

- Type your messages and press Enter.
- Type `exit` or `quit` to end the session.

### Option B: Web application

Start the Flask server:

```bash
python integration.py
```

Then open in your browser:

- **Welcome page:** http://localhost:5000  
- **Chat page:** http://localhost:5000/chat  

The app uses a single chat session; use “New chat” on the chat page to start a fresh conversation.

---

## API endpoints (Flask app)

| Endpoint           | Method | Description                          |
|--------------------|--------|--------------------------------------|
| `/`                | GET    | Welcome/landing page                 |
| `/chat`            | GET    | Chat UI page                         |
| `/api/chat`        | POST   | Send a message, get bot reply        |
| `/api/new-chat`    | POST   | Start a new chat session             |
| `/api/health`      | GET    | Health check (model & API key status)|

**Example: send a chat message**

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Give me a simple dal recipe"}'
```

---

## Tech stack

- **Python 3**
- **Google Generative AI (Gemini)** — `gemini-2.0-flash-exp` in the web app, `gemini-1.5-flash` in the CLI
- **Flask** — Web server and API
- **Flask-CORS** — Cross-origin support for the frontend
- **python-dotenv** — Load `GEMINI_API_KEY` from `.env`

---

## Troubleshooting

- **“GEMINI_API_KEY not found”**  
  Ensure `.env` exists in the project root and contains `GEMINI_API_KEY=...`. Restart the app after changing `.env`.

- **“AI model not initialized”**  
  Check that your API key is valid and that you have network access. The health endpoint `/api/health` reports whether the model and key are configured.

- **Chat not updating / stale replies**  
  Use “New chat” (or restart the Flask app) to reset the conversation and start a new session.

---

## License

This project is for educational and personal use. Respect Google’s Gemini API terms of use when using your API key.

**Author:** Sanvi Tripathi
