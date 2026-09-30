from google import genai
from app.config import GEMINI_API_KEY, GEMINI_PRO_MODEL

def generate_story(outline, character_name, tone):
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    prompt = f"""
Turn the following 5-panel comic outline into a complete comic script.

Main character: {character_name}
Tone: {tone}

For every panel provide:
- Caption
- Narration
- Dialogue

Keep continuity between panels. Do not add extra panels.

OUTLINE:
{outline}
"""
    response = genai.Client(api_key=GEMINI_API_KEY).models.generate_content(
        model=GEMINI_PRO_MODEL,
        contents=prompt
    )
    return response.text
