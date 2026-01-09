# Game Dev Supercharger Examples

## Example 1: Expert Panel for Physics Decision

**User asks:** "Should I use Unity's built-in Physics2D or write custom physics for my arcade baseball game?"

**Claude spawns expert panel:**

```python
spawn_expert_panel(
  decision="Use Unity Physics2D with custom arcade tweaks for baseball game",
  experts=["GameDesignExpert", "UnityArchitect", "PerformanceEngineer"],
  context="Retro arcade baseball, targeting mobile and web, needs: realistic ball arcs, exaggerated curves for pitches, predictable bounces"
)
```

**Expert Responses:**

**GameDesignExpert:**
> Recommendation: MODIFY
>
> Unity Physics2D alone won't give you the arcade feel. Physics2D is simulation-accurate, but arcade games need exaggeration. I recommend:
> - Use Physics2D for collision detection and basic trajectory
> - Override velocity calculations for pitches (add sinusoidal curves)
> - Dampen ball bounces for predictability
> - Reference: RBI Baseball, Super Mega Baseball use similar hybrid approach

**UnityArchitect:**
> Recommendation: APPROVE with modifications
>
> Unity Physics2D is the right foundation:
> - Mature, battle-tested collision system
> - Handles raycasts for fielding AI
> - Triggers for base detection
>
> Custom layer: Use FixedUpdate to apply "arcade forces" on top
> Avoid fully custom physics - reinventing collision detection is error-prone.

**PerformanceEngineer:**
> Recommendation: APPROVE
>
> Physics2D performance on mobile:
> - Collision checks: ~0.1-0.3ms for simple shapes
> - Keep physics layers minimal (< 8)
> - Use Continuous Collision Detection only for ball
> - Budget: 2-3ms per frame for physics (acceptable for 60 FPS)
>
> Custom physics wouldn't be faster - Unity's is heavily optimized C++.

**Consensus:**
✅ Use Unity Physics2D with custom arcade force layer

---

## Example 2: Batch Scene Creation

**User asks:** "Create a baseball field scene with all the bases, mound, and outfield wall"

**Claude executes:**

```python
unity_batch_command(
  commands=[
    # Create scene
    {"tool": "manage_scene", "action": "create", "name": "BaseballField"},

    # Create field ground
    {"tool": "manage_gameobject", "action": "create", "name": "InfieldGrass",
     "components": ["SpriteRenderer"]},
    {"tool": "manage_components", "action": "set_property", "gameobject": "InfieldGrass",
     "component": "SpriteRenderer", "property": "color", "value": "#2E8B57"},
    {"tool": "manage_components", "action": "set_property", "gameobject": "InfieldGrass",
     "property": "localScale", "value": {"x": 20, "y": 20}},

    # Create bases
    {"tool": "manage_gameobject", "action": "create", "name": "HomePlate",
     "position": {"x": 0, "y": 0}, "components": ["SpriteRenderer", "BoxCollider2D"]},
    {"tool": "manage_gameobject", "action": "create", "name": "FirstBase",
     "position": {"x": 5, "y": 5}, "components": ["SpriteRenderer", "BoxCollider2D"]},
    {"tool": "manage_gameobject", "action": "create", "name": "SecondBase",
     "position": {"x": 0, "y": 10}, "components": ["SpriteRenderer", "BoxCollider2D"]},
    {"tool": "manage_gameobject", "action": "create", "name": "ThirdBase",
     "position": {"x": -5, "y": 5}, "components": ["SpriteRenderer", "BoxCollider2D"]},

    # Create camera
    {"tool": "manage_gameobject", "action": "create", "name": "MainCamera",
     "position": {"x": 0, "y": 5, "z": -10}, "components": ["Camera"]},
    {"tool": "manage_components", "action": "set_property", "gameobject": "MainCamera",
     "component": "Camera", "property": "orthographic", "value": true},

    # Save scene
    {"tool": "manage_scene", "action": "save"}
  ]
)
```

**Result:** Complete baseball field created in < 2 seconds

---

## Example 3: AI Asset Generation + Import

**User asks:** "Create player sprites for 4 different teams"

**Claude executes:**

**Step 1: Generate assets**
```python
teams = [
  {"name": "Red Sox", "colors": "red and white"},
  {"name": "Blue Jays", "colors": "blue and white"},
  {"name": "Cardinals", "colors": "red and gold"},
  {"name": "Yankees", "colors": "navy and white"}
]

for team in teams:
  generate_2d_assets(
    prompt=f"Baseball player sprite, {team['colors']} uniform, batting pose",
    style="pixel art, 16-bit, retro, clean background",
    count=4,
    tool="leonardo"  # Better for character consistency
  )
```

**Step 2: Import to Unity**
```python
unity_batch_command(
  commands=[
    {"tool": "manage_asset", "action": "import", "path": "./red_sox_player_0.png",
     "assetType": "sprite"},
    {"tool": "manage_material", "action": "create", "name": "RedSoxPlayerMat",
     "shader": "Sprites/Default"},
    # ... repeat for all teams
  ]
)
```

**Step 3: Expert validation**
```python
spawn_expert_panel(
  decision="Use these AI-generated player sprites",
  experts=["VisualDirector"],
  context="Retro baseball game, need consistent pixel art style across 4 teams"
)
```

**VisualDirector response:**
> APPROVE with minor tweaks
>
> Visual cohesion: ✅ Good
> - Consistent pixel density across all sprites
> - Uniform outline thickness
> - Retro aesthetic maintained
>
> Overall: Production-ready with minor adjustments

---

## Example 4: Performance Validation

**User:** "Check if my game runs well on mobile"

**Claude executes:**

```python
validate_performance(
  platform="mobile",
  target_fps=60
)
```

**Result:**
```markdown
# Performance Validation Report

**Platform:** mobile
**Status:** ❌ FAIL

## Targets vs Measured

| Metric | Target | Measured | Status |
|--------|--------|----------|--------|
| FPS | 60 | 45.3 | ❌ |
| Frame Time | 16.67ms | 22.08ms | ❌ |
| Draw Calls | 100 | 247 | ❌ |

## Issues Found

### 🔴 Draw Calls (HIGH)
**Problem:** Draw calls 247 exceed target 100
**Suggestion:** Enable Static Batching, use Sprite Atlases, reduce materials
```

**Claude spawns expert:**
```python
spawn_expert_panel(
  decision="Fix performance issues: high draw calls and low FPS",
  experts=["PerformanceEngineer"],
  context="Mobile game at 45 FPS with 247 draw calls"
)
```

**PerformanceEngineer response:**
> CRITICAL: 247 draw calls is 2.5x over budget
>
> Action plan:
> 1. **Sprite Atlas**: Combine all UI sprites → saves 100-150 draw calls
> 2. **Static Batching**: Mark field elements as Static → saves 20-30 draw calls
> 3. **Material Consolidation**: Reuse materials → target < 10 unique materials
> 4. **Object Pooling**: Avoid Instantiate() during gameplay
>
> After these fixes, re-validate. Target should be achievable.

---

## Example 5: Complete Feature Implementation

**User:** "Implement a home run camera zoom effect"

**Phase 1: Expert validation**
```python
spawn_expert_panel(
  decision="Add cinematic camera zoom on home runs using Cinemachine",
  experts=["GameDesignExpert", "UnityArchitect", "PerformanceEngineer"],
  context="When ball leaves park, dramatic slow-motion zoom following ball"
)
```

**Experts approve with recommendations:**
- Use Cinemachine Virtual Cameras for smooth transitions
- Time.timeScale for slow-motion (0.5x)
- Particle trail on ball for impact

**Phase 2: Implementation**
```python
unity_batch_command(
  commands=[
    # Create virtual cameras
    {"tool": "manage_gameobject", "action": "create", "name": "CM_Normal",
     "components": ["CinemachineVirtualCamera"]},
    {"tool": "manage_gameobject", "action": "create", "name": "CM_HomeRun",
     "components": ["CinemachineVirtualCamera"]},
    # Configure cameras
    {"tool": "manage_components", "action": "set_property", "gameobject": "CM_HomeRun",
     "property": "m_Lens.OrthographicSize", "value": 5},
    # Create script
    {"tool": "manage_script", "action": "create", "name": "HomeRunCamera",
     "path": "Assets/Scripts/"}
  ]
)
```

**Phase 3: Validate**
```python
validate_performance(platform="mobile", target_fps=60)
```

✅ Performance still meets targets with new camera system
