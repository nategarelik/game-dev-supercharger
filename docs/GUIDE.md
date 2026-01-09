# Game Dev Supercharger Usage Guide

## Quick Start

1. **Install Unity MCP**
   - Download: https://assetstore.unity.com/packages/tools/generative-ai/mcp-for-unity-ai-driven-development-329908
   - Open Unity → Window > MCP for Unity → Start Server

2. **Install Game Dev Supercharger**
   ```bash
   cd ~/.claude-plugins/game-dev-supercharger
   ./install.sh
   ```

3. **Configure API Keys**
   Edit `.env` with your API keys (copy from `env.example`)

4. **Add to Claude Code**
   ```bash
   claude mcp add --scope user GameDevSupercharger -- uv --directory ~/.claude-plugins/game-dev-supercharger/mcp-server run server.py
   ```

## Available Tools

### 1. spawn_expert_panel

Spawn specialized AI agents to validate game dev decisions.

**Experts:**
- `GameDesignExpert`: Game feel, player psychology, engagement loops
- `UnityArchitect`: Unity patterns, architecture, best practices
- `PerformanceEngineer`: Optimization, frame budgets, profiling
- `VisualDirector`: Art style, visual cohesion, asset quality

**Example:**
```python
spawn_expert_panel(
  decision="Use Physics2D for arcade baseball ball physics",
  experts=["GameDesignExpert", "UnityArchitect", "PerformanceEngineer"],
  context="Building retro arcade baseball targeting mobile and web"
)
```

### 2. unity_batch_command

Execute multiple Unity commands efficiently (up to 25).

**Example:**
```python
unity_batch_command(
  commands=[
    {"tool": "manage_scene", "action": "create", "name": "Level1"},
    {"tool": "manage_gameobject", "action": "create", "name": "Player",
     "components": ["Rigidbody2D", "BoxCollider2D"]},
    {"tool": "manage_material", "action": "create", "name": "PlayerMat", "color": "#FF0000"}
  ]
)
```

### 3. generate_2d_assets

Generate 2D game assets using AI.

**Supported tools:**
- `gemini`: Free 500/day
- `leonardo`: Free 150 tokens/day
- `flux`: Free via HuggingFace

**Example:**
```python
generate_2d_assets(
  prompt="Baseball player sprite, batting pose, front view",
  style="pixel art, 16-bit, retro",
  count=4,
  tool="gemini"
)
```

### 4. generate_3d_assets

Generate 3D models using AI.

**Supported tools:**
- `meshy`: $20/mo subscription
- `hunyuan3d`: Local GPU required

**Example:**
```python
generate_3d_assets(
  prompt="Baseball stadium bleachers section, weathered wood",
  type="text_to_3d",
  tool="meshy"
)
```

### 5. validate_performance

Run performance profiling and validation against platform targets.

**Platform targets:**
- Mobile: 60 FPS, 16.67ms frame, 100 draw calls
- Web: 30 FPS, 33.33ms frame, 50 draw calls
- Desktop: 60 FPS, 16.67ms frame, 500 draw calls

**Example:**
```python
validate_performance(
  platform="mobile",
  target_fps=60
)
```

## Typical Workflows

### New Feature Decision

1. Brainstorm approach
2. **Spawn expert panel** to validate
3. Iterate based on feedback
4. Implement with **batch Unity commands**
5. **Validate performance**

### Asset Creation

1. Generate concepts with **generate_2d_assets** or **generate_3d_assets**
2. Review and select best variations
3. Import to Unity with **batch commands**
4. Expert **VisualDirector** validates cohesion

### Performance Optimization

1. **Validate performance** to identify issues
2. Spawn **PerformanceEngineer** for detailed analysis
3. Apply suggested optimizations
4. Re-validate until targets met

## Best Practices

1. **Always consult experts before major decisions**
   - Prevents rework from bad architectural choices
   - Catches platform-specific gotchas early

2. **Use batch commands for scene setup**
   - 10-100x faster than individual calls
   - Reduces API round-trips

3. **Generate asset variations**
   - Create 4-8 options and pick best
   - AI can surprise with better ideas

4. **Validate performance early and often**
   - Don't wait until end to discover issues
   - Test on target platform (mobile especially)

5. **Document expert consensus**
   - Save expert panel responses for reference
   - Build knowledge base of validated patterns

## Troubleshooting

### Unity MCP not connecting
- Check Unity is running with MCP server started
- Verify http://localhost:8080/mcp is accessible
- Restart Unity MCP: Window > MCP for Unity > Restart Server

### Expert panel timeout
- Check ANTHROPIC_API_KEY is set in .env
- Verify API key is valid at https://console.anthropic.com

### Asset generation failing
- Check API keys for Gemini/Leonardo/Meshy in .env
- Verify rate limits haven't been exceeded
- Try alternative tool (gemini → leonardo)

### Performance validation shows dummy data
- Unity MCP must be running
- Unity project must be open
- Performance data collected during Play Mode
