import re
from pathlib import Path
import requests
from app.config import HF_API_KEY, HF_IMAGE_MODEL

PANELS_DIR = Path("app/static/panels")
PANELS_DIR.mkdir(parents=True, exist_ok=True)

def _safe_name(value):
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", value).strip("_")[:70]

def generate_image(image_prompt, panel_number):
    """
    Uses Hugging Face Inference API when HF_API_KEY is available.
    Returns a URL usable by the Jinja2 templates.
    """
    if not HF_API_KEY:
        return None

    url = f"https://api-inference.huggingface.co/models/{HF_IMAGE_MODEL}"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(
        url,
        headers=headers,
        json={"inputs": image_prompt},
        timeout=180
    )
    response.raise_for_status()

    filename = f"panel_{panel_number}_{_safe_name(image_prompt)}.png"
    output = PANELS_DIR / filename
    output.write_bytes(response.content)

    return f"/static/panels/{filename}"
