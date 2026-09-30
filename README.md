# ComicCraft 🎨📖

**ComicCraft** is a FastAPI-based AI comic story creator. Users enter a story idea, character, setting, tone and art style. The application creates a structured 5-panel outline, expands it into a comic script, optionally generates illustrations, previews the result in a browser, and exports the comic as a PDF.

The project follows the architecture described in the supplied ComicCraft project document: FastAPI + Jinja2 for the web application, Gemini models for structured story generation and narration, image generation through Hugging Face, and FPDF for PDF export.

## Features

- 5-panel AI comic outline
- Character, setting, tone and art-style inputs
- Gemini-powered story generation
- Hugging Face image-generation integration
- Panel-by-panel web preview
- PDF export
- JSON API endpoint
- Image-generation test endpoint
- Modular backend architecture

## Project Structure

```text
ComicCraft/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── config.py
│   ├── gemini_flash.py
│   ├── gemini_pro.py
│   ├── image_generator.py
│   ├── layout_builder.py
│   ├── exporters.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── comic_preview.html
│   │   └── export_success.html
│   └── static/
│       ├── style.css
│       ├── panels/
│       └── exports/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/ComicCraft.git
cd ComicCraft
```

### 2. Create virtual environment

Windows:

```bash
python -m venv env
env\Scripts\activate
```

macOS/Linux:

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Copy `.env.example` to `.env`:

```text
GEMINI_API_KEY=your_key
HF_API_KEY=your_key
```

Never upload `.env` or real API keys to GitHub.

### 5. Run

```bash
uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## API

### POST `/generate`

Browser form endpoint for complete comic generation.

### POST `/generate-comic/json`

Example JSON:

```json
{
  "story_prompt": "A brave fox exploring an enchanted forest.",
  "character_name": "Finn",
  "setting": "Forest",
  "tone": "Dramatic",
  "art_style": "Comic book"
}
```

### GET `/test-image`

Example:

```text
/test-image?prompt=A%20heroic%20fox%20in%20an%20enchanted%20forest
```

## Important note about image generation

Image generation is optional until `HF_API_KEY` is configured. Without it, ComicCraft still demonstrates the story-generation and PDF pipeline, but image placeholders are shown.

## GitHub upload

```bash
git init
git add .
git commit -m "Initial ComicCraft AI comic creator"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ComicCraft.git
git push -u origin main
```

## Future Improvements

- User accounts and saved comic libraries
- Multi-page story arcs
- Better panel-specific narration/dialogue parsing
- Image consistency for recurring characters
- Background image upload
- Cloud deployment
- Authentication and rate limiting
- Regenerate individual panels
