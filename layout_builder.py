def build_comic_layout(outline, story_text, image_paths):
    """
    Keeps the generated outline, story and images together.
    Story text is retained as one full script and shown on the preview.
    """
    layout = []
    for index, panel in enumerate(outline):
        layout.append({
            "panel": panel.get("panel", index + 1),
            "title": panel.get("title", f"Panel {index + 1}"),
            "scene_description": panel.get("scene_description", ""),
            "image_prompt": panel.get("image_prompt", ""),
            "image_path": image_paths[index] if index < len(image_paths) else None,
            "story": story_text
        })
    return layout
