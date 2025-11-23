from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="AutoQuote AI Demo")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    "Believe in yourself. Great things take time.",
    "Every day is a new chance to improve and grow.",
    "Dream big and act courageously.",
    "Happiness comes from appreciating the small things.",
    "Kindness is a language everyone understands.",
]

class QuoteRequest(BaseModel):
    topic: str

@app.post("/generate-quote")
def generate_quote(req: QuoteRequest):
    topic = req.topic.strip()
    return {"quote": f"{random.choice(quotes)}"}
