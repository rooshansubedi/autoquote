# api/generate_quote.py
import json
import random

quotes = [
    "Believe in yourself. Great things take time.",
    "Every day is a new chance to improve and grow.",
    "Dream big and act courageously.",
    "Happiness comes from appreciating the small things.",
    "Kindness is a language everyone understands.",
]

def handler(request):
    try:
        body = json.loads(request.body)
        topic = body.get("topic", "").strip()
        quote = random.choice(quotes)
        return {
            "statusCode": 200,
            "body": json.dumps({"quote": f"{quote} (about {topic})"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"quote": "Error generating quote"})
        }
