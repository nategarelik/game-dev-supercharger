# Game Dev Supercharger Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      Claude Code CLI                         │
└────────────────────────┬────────────────────────────────────┘
                         │ MCP Protocol (JSON-RPC)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Game Dev Supercharger MCP Server                │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   Tool Router                         │  │
│  │  - spawn_expert_panel                                 │  │
│  │  - unity_batch_command                                │  │
│  │  - generate_2d_assets                                 │  │
│  │  - generate_3d_assets                                 │  │
│  │  - validate_performance                               │  │
│  └──────────────┬───────────────────────────────────────┘  │
│                 │                                            │
│  ┌──────────────▼───────────────────────────────────────┐  │
│  │              Multi-Agent Expert Panel                 │  │
│  │                                                        │  │
│  │  ┌──────────────┐  ┌──────────────┐                  │  │
│  │  │ GameDesign   │  │   Unity      │                  │  │
│  │  │   Expert     │  │  Architect   │                  │  │
│  │  └──────┬───────┘  └──────┬───────┘                  │  │
│  │         │                  │                          │  │
│  │         │  ┌──────────────┐│  ┌──────────────┐       │  │
│  │         └──│ Performance  ││  │   Visual     │       │  │
│  │            │  Engineer    │└──│  Director    │       │  │
│  │            └──────┬───────┘   └──────┬───────┘       │  │
│  │                   │                   │               │  │
│  │              ┌────▼───────────────────▼────┐         │  │
│  │              │  Consensus Synthesizer       │         │  │
│  │              └──────────────────────────────┘         │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            Asset Generation Pipeline                  │  │
│  │                                                        │  │
│  │  2D: Gemini → Leonardo → FLUX                         │  │
│  │  3D: Meshy → Hunyuan3D                                │  │
│  │  Automation: n8n workflows                            │  │
│  └────────────────┬─────────────────────────────────────┘  │
│                   │                                          │
│  ┌────────────────▼─────────────────────────────────────┐  │
│  │         Performance Validator                         │  │
│  │                                                        │  │
│  │  - Unity Profiler integration                         │  │
│  │  - Platform-specific targets                          │  │
│  │  - Markdown report generation                         │  │
│  └────────────────┬─────────────────────────────────────┘  │
└───────────────────┼─────────────────────────────────────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
┌────────────────┐    ┌────────────────┐
│   Unity MCP    │    │  External APIs │
│   (port 8080)  │    │                │
│                │    │  - Anthropic   │
│  - batch_exec  │    │  - Gemini      │
│  - manage_*    │    │  - Leonardo    │
│  - profiler    │    │  - Meshy       │
└────────────────┘    └────────────────┘
```

## Component Descriptions

### MCP Server (`mcp-server/server.py`)

Central coordinator handling tool routing and orchestration. Implements JSON-RPC protocol for Claude Code integration.

**Responsibilities:**
- Register and expose tools to Claude
- Route tool calls to appropriate handlers
- Manage async operations and timeouts
- Error handling and response formatting

### Expert Agent System (`agents/`)

Multi-agent decision validation using specialized AI experts. Each expert has:
- Specialized system prompt defining expertise area
- Access to external knowledge sources (Context7, WebSearch)
- Tool use capabilities for research
- Independent analysis capabilities

**Expert Types:**
- **GameDesignExpert**: Player experience, game feel, engagement
- **UnityArchitect**: Unity patterns, architecture, best practices
- **PerformanceEngineer**: Optimization, frame budgets, profiling
- **VisualDirector**: Art direction, visual cohesion, style

**Consensus Process:**
1. Each expert analyzes decision independently
2. Experts can use tools for research (search docs, find examples)
3. Analyses collected with recommendations (approve/reject/modify)
4. Consensus synthesizer identifies conflicts and patterns
5. Final recommendation with confidence level returned

### Asset Pipeline (`workflows/`)

Automated AI asset generation with multiple provider support.

**2D Asset Flow:**
```
User Prompt
    ↓
[Select Tool: Gemini/Leonardo/FLUX]
    ↓
[Batch Generate 4-8 Variations]
    ↓
[Base64 or URL Response]
    ↓
[Optional: Auto-import to Unity]
```

**3D Asset Flow:**
```
User Prompt
    ↓
[Select Tool: Meshy/Hunyuan3D]
    ↓
[Submit Generation Job]
    ↓
[Poll for Completion (10-60s)]
    ↓
[GLB/FBX Download URL]
    ↓
[Optional: Auto-import to Unity]
```

**n8n Integration:**
- Templates for batch workflows
- Scheduled generation (e.g., overnight asset creation)
- Webhook triggers from Unity events

### Performance Validator (`tools/`)

Unity profiling integration with platform-specific validation.

**Workflow:**
1. Enable Unity Profiler via MCP
2. Enter Play Mode
3. Collect 60 frames of data
4. Exit Play Mode
5. Extract metrics: FPS, frame time, draw calls, memory
6. Compare against platform targets
7. Generate issues list with suggestions
8. Format markdown report

**Platform Targets:**
- Mobile: 60 FPS, 16.67ms frame, 100 draw calls
- Web: 30 FPS, 33.33ms frame, 50 draw calls
- Desktop: 60 FPS, 16.67ms frame, 500 draw calls

## Data Flow Example: Complete Feature

**User:** "Add power-up pickup system"

1. **Planning Phase**
   ```
   Claude → spawn_expert_panel()
      ├→ GameDesignExpert: Validates power-up balance
      ├→ UnityArchitect: Recommends ScriptableObject pattern
      ├→ PerformanceEngineer: Validates object pooling approach
      └→ VisualDirector: Suggests particle effects for pickup

   Experts return consensus → Claude presents plan
   User approves
   ```

2. **Implementation Phase**
   ```
   Claude → unity_batch_command()
      ├→ create PowerUp prefab
      ├→ create PowerUpManager script
      ├→ create PowerUpData ScriptableObject
      ├→ add particle system
      └→ configure physics layers

   Unity MCP executes 25 commands in parallel
   Returns success/failure status
   ```

3. **Asset Generation Phase**
   ```
   Claude → generate_2d_assets()
      └→ "Power-up icon, glowing star, pixel art"

   Gemini generates 4 variations
   Returns base64 encoded PNGs

   Claude → unity_batch_command()
      └→ import sprites to Unity
   ```

4. **Validation Phase**
   ```
   Claude → validate_performance()
      └→ Run profiler on mobile target

   Performance Validator returns metrics

   If issues found:
      Claude → spawn_expert_panel()
         └→ PerformanceEngineer analyzes bottlenecks
   ```

5. **Completion**
   ```
   Claude generates documentation
   Commits changes
   Returns summary to user
   ```

## Extensibility

### Adding New Tools

1. Add tool definition to `server.py:_register_tools()`
2. Implement handler method `_handle_{tool_name}()`
3. Add tests in `test_{tool_name}.py`
4. Document in `docs/GUIDE.md`

### Adding New Experts

1. Create `agents/{expert_name}.py` inheriting from `BaseExpert`
2. Implement `get_system_prompt()` and `get_tools()`
3. Add to expert_classes dict in `server.py`
4. Document expertise area and example usage

### Adding New Asset Providers

1. Add method to `workflows/asset_generation.py`
2. Handle authentication and rate limiting
3. Normalize response format
4. Add to tool selection logic
5. Update documentation with pricing/limits

## Security Considerations

- API keys stored in `.env` (not committed)
- Unity MCP runs locally only (no remote access)
- Expert agents use user's Anthropic API key
- Generated assets stored locally before import
- No automatic code execution without user approval

## Performance Characteristics

- Expert panel: 5-15 seconds (4 parallel agents)
- Asset generation: 10-60 seconds (depends on provider)
- Unity batch commands: < 1 second (25 commands)
- Performance validation: 2-3 seconds (60 frames)

## Technology Stack

- **Python 3.10+**: Core implementation language
- **uv**: Fast Python package manager
- **httpx**: Async HTTP client for MCP/API calls
- **Anthropic SDK**: Expert agent AI
- **Unity MCP**: Unity Editor integration
- **Gemini API**: Free 2D asset generation
- **Leonardo.ai**: Premium 2D assets
- **Meshy Pro**: 3D model generation
- **n8n**: Workflow automation (optional)

## Future Enhancements

- [ ] Caching layer for expert consensus on common questions
- [ ] Local LLM option for privacy-sensitive projects
- [ ] Unity Editor plugin GUI for direct access
- [ ] Automated testing integration (play mode tests)
- [ ] Steam integration for builds and uploads
- [ ] Multi-project workspace management
