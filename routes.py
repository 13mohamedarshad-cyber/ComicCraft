from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import PromptRequest
from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def create_comic(data):
    outline = generate_outline(
        data["story_prompt"],
        data["character_name"],
        data["setting"],
        data["tone"],
        data["art_style"]
    )

    story = generate_story(
        outline,
        data["character_name"],
        data["tone"]
    )

    images = []
    for panel in outline:
        images.append(generate_image(panel["image_prompt"], panel["panel"]))

    layout = build_comic_layout(outline, story, images)
    pdf_path = save_pdf(layout)

    return layout, pdf_path

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@router.post("/generate")
async def generate(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):
    try:
        layout, pdf_path = create_comic({
            "story_prompt": story_prompt,
            "character_name": character_name,
            "setting": setting,
            "tone": tone,
            "art_style": art_style
        })
        return templates.TemplateResponse(
            "comic_preview.html",
            {"request": request, "layout": layout, "pdf_path": pdf_path}
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.post("/generate-comic/json")
async def generate_json(payload: PromptRequest):
    try:
        layout, pdf_path = create_comic(payload.model_dump())
        return {"success": True, "layout": layout, "pdf_path": pdf_path}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.get("/test-image")
async def test_image(prompt: str = "A heroic fox in an enchanted forest, comic book art"):
    try:
        image_path = generate_image(prompt, 0)
        return {"success": bool(image_path), "image_path": image_path}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@router.get("/export-success")
async def export_success(request: Request):
    return templates.TemplateResponse(
        "export_success.html",
        {"request": request}
    )
