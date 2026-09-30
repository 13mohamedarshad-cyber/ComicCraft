import json
import re
from google import genai
from app.config import GEMINI_API_KEY, GEMINI_FLASH_MODEL

def _client():
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")
    return genai.Client(api_key=GEMINI_API_KEY)

def _extract_json(text: str):
    text = text.strip()
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)

def generate_outline(story_prompt, character_name, setting, tone, art_style):
    prompt = f"""
Create a structured 5-panel comic outline.

Story prompt: {story_prompt}
Main character: {character_name}
Setting: {setting}
Tone: {tone}
Art style: {art_style}

Return ONLY valid JSON in this exact shape:
[
  {{
    "panel": 1,
    "title": "...",
    "scene_description": "...",
    "image_prompt": "..."
  }}
]

Create exactly 5 panels. Keep the same main character and setting throughout.
"""
    response = _client().models.generate_content(
        model=GEMINI_FLASH_MODEL,
        contents=prompt
    )
    return _extract_json(response.text)
