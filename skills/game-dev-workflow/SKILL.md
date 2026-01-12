---
name: game-dev-workflow
description: Use when working on Unity game development - provides expert validation, asset generation, and performance profiling
---

# Game Dev Supercharger Workflow

## Overview

This skill provides professional Unity game development workflows with AI-powered expert validation, automated asset generation, and performance profiling.

## When to Use

Use this skill when:
- Making architectural decisions about Unity game systems
- Generating game assets (2D sprites, 3D models)
- Setting up Unity scenes with batch commands
- Validating game performance against platform targets
- Needing expert feedback on game design, architecture, or optimization

## Available Tools

### 1. spawn_expert_panel

Get expert validation before making critical decisions.

**Experts available:**
- **GameDesignExpert**: Player psychology, game feel, engagement loops
- **UnityArchitect**: Unity patterns, architecture, best practices
- **PerformanceEngineer**: Optimization, frame budgets, profiling
- **VisualDirector**: Art direction, visual cohesion, asset quality

**When to use:**
- Before implementing major game systems
- When choosing between architectural approaches
- To validate asset visual coherence
- For performance optimization strategies

**Example:**
```
User: "Should I use Unity's Physics2D or custom physics for my arcade game?"

Claude: Let me consult the expert panel...
spawn_expert_panel(
  decision="Use Unity Physics2D with arcade tweaks",
  experts=["GameDesignExpert", "UnityArchitect", "PerformanceEngineer"],
  context="Arcade baseball game targeting mobile and web"
)
```

### 2. generate_2d_assets

Generate 2D game assets using AI (Gemini, Leonardo, FLUX).

**When to use:**
- Need sprites, icons, or UI elements
- Want multiple variations to choose from
- Prototyping visual style

**Example:**
```
generate_2d_assets(
  prompt="Baseball player sprite, batting pose",
  style="pixel art, 16-bit, retro",
  count=4,
  tool="gemini"  # Free 500/day
)
```

### 3. generate_3d_assets

Generate 3D models using AI (Meshy, Hunyuan3D).

**When to use:**
- Need 3D models for Unity scenes
- Prototyping environment props
- Creating unique game assets

**Example:**
```
generate_3d_assets(
  prompt="Baseball stadium bleachers, weathered wood",
  type="text_to_3d",
  tool="meshy"  # $20/mo subscription
)
```

### 4. unity_batch_command

Execute up to 25 Unity commands in parallel via Unity MCP.

**When to use:**
- Setting up Unity scenes
- Creating multiple GameObjects at once
- Batch importing assets
- Configuring scene hierarchies

**Example:**
```
unity_batch_command(
  commands=[
    {"tool": "manage_scene", "action": "create", "name": "Level1"},
    {"tool": "manage_gameobject", "action": "create",
     "name": "Player", "components": ["Rigidbody2D"]},
    {"tool": "manage_material", "action": "create",
     "name": "PlayerMat", "color": "#FF0000"}
  ]
)
```

### 5. validate_performance

Run Unity Profiler and validate against platform targets.

**Platform targets:**
- Mobile: 60 FPS, 16.67ms frame time, 100 draw calls
- Web: 30 FPS, 33.33ms frame time, 50 draw calls
- Desktop: 60 FPS, 16.67ms frame time, 500 draw calls

**When to use:**
- After implementing major features
- Before releasing builds
- When investigating performance issues
- To validate optimization efforts

**Example:**
```
validate_performance(
  platform="mobile",
  target_fps=60
)
```

## Typical Workflows

### New Feature Implementation

1. **Brainstorm** the approach
2. **Spawn expert panel** to validate architecture
3. **Iterate** based on expert feedback
4. **Implement** using Unity batch commands
5. **Validate performance** against targets

### Asset Creation Pipeline

1. **Generate** 4-8 asset variations with AI
2. **Review** and select best options
3. **Import** to Unity with batch commands
4. **Validate** visual coherence with VisualDirector

### Performance Optimization

1. **Validate performance** to identify issues
2. **Spawn PerformanceEngineer** for analysis
3. **Apply** suggested optimizations
4. **Re-validate** until targets met

## Best Practices

1. **Always consult experts before major decisions**
   - Prevents costly architectural mistakes
   - Catches platform-specific issues early

2. **Use batch commands for efficiency**
   - 10-100x faster than individual API calls
   - Reduces development time significantly

3. **Generate asset variations**
   - AI can surprise with creative ideas
   - Having options improves final quality

4. **Validate performance early and often**
   - Don't wait until release to find issues
   - Test on target platform (mobile especially)

## Prerequisites

- **Unity MCP** must be running (http://localhost:8080/mcp)
- **API Keys** configured in environment:
  - `ANTHROPIC_API_KEY` (required for expert panel)
  - `GEMINI_API_KEY` (optional, free 500/day)
  - `LEONARDO_API_KEY` (optional, free tier available)
  - `MESHY_API_KEY` (optional, $20/mo for 3D)

## Documentation

- **Usage Guide**: See docs/GUIDE.md for detailed examples
- **Architecture**: See docs/ARCHITECTURE.md for system design
- **Examples**: See docs/EXAMPLES.md for 5 real-world scenarios
