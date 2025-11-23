from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

import random
import os

app = FastAPI(title="AutoQuote AI Demo")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder (for CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html for root route
@app.get("/")
def serve_home():
    return FileResponse("index.html")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Demo quote pool
quotes = [
    # Motivational
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "Every day is a fresh start. Use it wisely and make it count. Small steps lead to great achievements.",
    "Dream big, work hard, and never give up. Your persistence will shape your success.",
    "Success is the sum of small efforts repeated day in and day out. Keep going even when it's tough.",
    "Courage is not the absence of fear, but taking action in spite of it.",
    
    # Happiness
    "Happiness does not depend on what you have, but on how you see life. Smile and embrace the moment.",
    "A joyful heart is the ultimate wealth. Find beauty in the little things every day.",
    "Life is 10% what happens to you and 90% how you respond. Choose joy, always.",
    
    # Love
    "Love is the bridge between you and everything. Cherish those who bring warmth to your life.",
    "Kindness and empathy create connections deeper than words. Spread love wherever you go.",
    "True love is not about perfection, but embracing each other's imperfections with grace.",
    
    # Sadness
    "Sometimes the hardest storms bring the most beautiful rainbows. Trust the process of life.",
    "Pain is inevitable, but suffering is optional. Learn, grow, and move forward.",
    "Even in darkness, there is light to be found. Keep searching and hope will guide you."
]

class QuoteRequest(BaseModel):
    topic: str

@app.post("/generate-quote")
def generate_quote(req: QuoteRequest):
    topic = req.topic.strip()
    quote = random.choice(quotes)
    return {"quote": quote}
