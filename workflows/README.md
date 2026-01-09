# Asset Generation Pipeline

## 2D Assets

### Gemini (Free - 500/day)
```python
await generate_2d_assets(
    prompt="Baseball player sprite, batting pose",
    style="pixel art, 16-bit",
    count=4,
    tool="gemini"
)
```

### Leonardo.ai (Free - 150 tokens/day)
```python
await generate_2d_assets(
    prompt="Team logo, retro sports",
    style="vector, clean",
    count=4,
    tool="leonardo"
)
```

## 3D Assets

### Meshy Pro ($20/mo)
```python
await generate_3d_assets(
    prompt="Baseball stadium seating section",
    type="text_to_3d",
    tool="meshy"
)
```

## n8n Workflows

Import `.n8n_templates/batch_2d_assets.json` into n8n for automated batch generation.

Configure credentials:
- Gemini API Key
- Leonardo API Key
- Meshy API Key
