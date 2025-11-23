from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="AutoQuote AI Demo")

# Allow all origins for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Demo quote pool
quotes = [
    # Motivational / confidence
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "Every day is a fresh start. Use it wisely and make it count. Small steps lead to great achievements.",
    "Dream big, work hard, and never give up. Your persistence will shape your success.",
    "Success is the sum of small efforts repeated day in and day out. Keep going even when it's tough.",
    "Courage is not the absence of fear, but taking action in spite of it.",

    # Happiness / positivity
    "Happiness does not depend on what you have, but on how you see life. Smile and embrace the moment.",
    "A joyful heart is the ultimate wealth. Find beauty in the little things every day.",
    "Life is 10% what happens to you and 90% how you respond. Choose joy, always.",

    # Love / relationships
    "Love is the bridge between you and everything. Cherish those who bring warmth to your life.",
    "Kindness and empathy create connections that words alone cannot describe. Spread love wherever you go.",
    "True love is not about perfection, it is about embracing each other's imperfections with grace.",

    # Sadness / reflection
    "Sometimes the hardest storms bring the most beautiful rainbows. Trust the process of life.",
    "Pain is inevitable, but suffering is optional. Learn, grow, and move forward.",
    "Even in darkness, there is light to be found. Keep searching and hope will guide you."
]

class QuoteRequest(BaseModel):
    topic: str

@app.post("/generate-quote")
def generate_quote(req: QuoteRequest):
    """
    Returns a random quote from the demo pool.
    Adds the topic to make it feel personalized.
    """
    topic = req.topic.strip()
    quote = random.choice(quotes)
    # Optionally include the topic in the quote
    return {"quote": f"{quote}"}
