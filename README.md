# 🎮 Game Dev Supercharger

> Universal Claude Code MCP plugin for professional 2D/3D Unity game development

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-MCP%20Plugin-purple)](https://claude.ai/code)

Transform your Unity game development workflow with AI-powered expert validation, automated asset generation, and performance profiling—all integrated directly into Claude Code.

## ✨ Features

### 🤖 Multi-Agent Expert Panel
Get expert validation before making critical decisions:
- **GameDesignExpert**: Player psychology, game feel, engagement loops
- **UnityArchitect**: Unity patterns, architecture, best practices
- **PerformanceEngineer**: Optimization, frame budgets, profiling
- **VisualDirector**: Art direction, visual cohesion, asset quality

### 🎨 Automated Asset Generation
Generate game-ready assets with AI:
- **2D Assets**: Gemini (500/day free), Leonardo.ai, FLUX
- **3D Models**: Meshy Pro, Hunyuan3D
- **Batch Processing**: n8n workflow templates included

### ⚡ Unity MCP Integration
Control Unity directly from Claude Code:
- Execute up to 25 commands in parallel
- Scene composition and asset management
- Real-time Unity Editor manipulation

### 📊 Performance Validation
Platform-specific performance profiling:
- Mobile: 60 FPS, 100 draw calls target
- Web: 30 FPS, 50 draw calls target
- Desktop: 60 FPS, 500 draw calls target
- Actionable optimization suggestions

## 🚀 Quick Start

### Prerequisites

1. **Unity MCP** - [Download from Asset Store](https://assetstore.unity.com/packages/tools/generative-ai/mcp-for-unity-ai-driven-development-329908)
2. **Python 3.10+** with `uv` package manager
3. **Claude Code CLI** installed

### Installation

**Method 1: Claude Code Plugin (Recommended)**

```bash
# Install as a Claude Code plugin
/plugin marketplace add https://github.com/nategarelik/game-dev-supercharger
/plugin install game-dev-supercharger@game-dev-supercharger-dev

# Configure API keys in your environment
export ANTHROPIC_API_KEY="your-key-here"
export GEMINI_API_KEY="your-key-here"  # Optional
export LEONARDO_API_KEY="your-key-here"  # Optional
export MESHY_API_KEY="your-key-here"  # Optional

# Restart Claude Code to load the plugin
```

**Method 2: Local Development**

```bash
# Clone and test locally
git clone https://github.com/nategarelik/game-dev-supercharger.git
cd game-dev-supercharger

# Add local marketplace for testing
/plugin marketplace add /path/to/game-dev-supercharger
/plugin install game-dev-supercharger@game-dev-supercharger-dev

# Restart Claude Code
```

**Method 3: Standalone MCP Server**

```bash
# For advanced users who want to run the MCP server independently
git clone https://github.com/nategarelik/game-dev-supercharger.git
cd game-dev-supercharger
./install.sh

# Configure API keys
cp env.example .env
# Edit .env with your keys

# Add to Claude Code manually
claude mcp add --scope user GameDevSupercharger \
  -- uv --directory $(pwd)/mcp-server run server.py
```

### API Keys Required

Add these to your environment variables (Windows: System Properties, macOS/Linux: ~/.bashrc or ~/.zshrc):

- **ANTHROPIC_API_KEY** (required): Expert panel functionality
- **GEMINI_API_KEY** (optional): Free 2D asset generation (500/day)
- **LEONARDO_API_KEY** (optional): Premium 2D assets (150 tokens/day free)
- **MESHY_API_KEY** (optional): 3D model generation ($20/mo)

## 📖 Usage Examples

### Expert Panel Validation

```python
spawn_expert_panel(
  decision="Use Physics2D for arcade baseball ball physics",
  experts=["GameDesignExpert", "UnityArchitect", "PerformanceEngineer"],
  context="Building retro arcade baseball targeting mobile and web"
)
```

### Generate Game Assets

```python
# Generate 2D sprites
generate_2d_assets(
  prompt="Baseball player sprite, batting pose, front view",
  style="pixel art, 16-bit, retro",
  count=4,
  tool="gemini"
)

# Generate 3D models
generate_3d_assets(
  prompt="Baseball stadium bleachers, weathered wood",
  type="text_to_3d",
  tool="meshy"
)
```

### Unity Batch Commands

```python
unity_batch_command(
  commands=[
    {"tool": "manage_scene", "action": "create", "name": "Level1"},
    {"tool": "manage_gameobject", "action": "create",
     "name": "Player", "components": ["Rigidbody2D", "BoxCollider2D"]},
    {"tool": "manage_material", "action": "create",
     "name": "PlayerMat", "color": "#FF0000"}
  ]
)
```

### Performance Validation

```python
validate_performance(
  platform="mobile",
  target_fps=60
)
```

## 🤖 Specialized AI Agents

The plugin includes **5 specialized agents**, each with deep expertise and access to specific tools. Claude automatically invokes the right agent based on your request:

### 1. Expert Consultant 🎓
Validates decisions by consulting a panel of 4 AI experts (GameDesign, Unity, Performance, Visual).

**Activates when you ask**: "Should I use X or Y?", "Is this a good approach?"

**Example:**
> **You**: "Should I use Physics2D or custom physics for my arcade game?"
>
> **Expert Consultant**: "Let me consult the panel..."
> - **GameDesignExpert**: Physics2D with arcade tweaks for predictable fun
> - **UnityArchitect**: Battle-tested, integrates well with Unity systems
> - **PerformanceEngineer**: Excellent mobile performance (< 3ms/frame)
>
> **Recommendation**: Unity Physics2D + custom arcade force layer ✅

### 2. Asset Generator 🎨
Creates 2D sprites and 3D models using AI (Gemini, Leonardo, Meshy).

**Activates when you ask**: "Create sprites for...", "Generate a 3D model of..."

**Example:**
> **You**: "I need player sprites for 4 teams"
>
> **Asset Generator**: "I'll use Leonardo for style consistency across teams..."
> *[Generates 16 sprite variations - 4 per team with team colors]*
> "Here are your options. Should I have VisualDirector validate coherence?"

### 3. Performance Profiler ⚡
Profiles your game and identifies bottlenecks with actionable optimizations.

**Activates when you ask**: "Is my game performant?", "Check performance"

**Example:**
> **You**: "Check if this runs well on mobile"
>
> **Performance Profiler**: *[Runs Unity Profiler]*
> **Result**: ❌ FAIL - 247 draw calls (target: 100)
>
> **Fix**: Create Sprite Atlas (saves ~150 calls), enable Static Batching (~30 calls)
> *[Specific, actionable steps with expected impact]*

### 4. Unity Builder 🔧
Rapidly builds Unity scenes with batch commands (up to 25 operations in parallel).

**Activates when you ask**: "Create a scene with...", "Set up GameObjects for..."

**Example:**
> **You**: "Create a baseball field with all bases"
>
> **Unity Builder**: *[Executes 18 commands in one batch]*
> - Baseball diamond with 4 bases (collision detection)
> - Pitcher's mound at regulation position
> - Outfield wall, orthographic camera
> "Scene created in < 2 seconds! Ready for sprites?"

### 5. Game Architect 🏗️
Orchestrates all agents to take features from concept → implementation.

**Activates when you ask**: "Build a [feature]", "Plan implementation of..."

**Example:**
> **You**: "Add a power-up system"
>
> **Game Architect**:
> **Phase 1**: Expert validation → ScriptableObject pattern approved ✅
> **Phase 2**: Generate 8 power-up icons with Asset Generator ✅
> **Phase 3**: Build scene structure with Unity Builder ✅
> **Phase 4**: Performance validation → 60 FPS maintained ✅
>
> "Complete! Power-up system ready with expert-validated architecture."

## 💬 Natural Conversation Flow

Just talk naturally - Claude invokes the right agent automatically:

- "Should I use X?" → **Expert Consultant**
- "Create sprites" → **Asset Generator**
- "Is it fast?" → **Performance Profiler**
- "Build the scene" → **Unity Builder**
- "Add [feature]" → **Game Architect** (coordinates all agents)

## 📁 Project Structure

```
game-dev-supercharger/
├── .claude-plugin/      # Claude Code plugin manifests
│   ├── plugin.json      # Plugin metadata and MCP config
│   └── marketplace.json # Development marketplace
├── agents/              # Specialized AI agents (Claude Code)
│   ├── expert-consultant.md   # Decision validation agent
│   ├── asset-generator.md     # 2D/3D asset creation agent
│   ├── performance-profiler.md # Performance validation agent
│   ├── unity-builder.md       # Scene construction agent
│   ├── game-architect.md      # Orchestrator agent
│   ├── base_expert.py         # Expert panel base class
│   ├── game_design_expert.py  # Game design expert
│   ├── unity_architect.py     # Unity architecture expert
│   ├── performance_engineer.py # Performance expert
│   └── visual_director.py     # Visual direction expert
├── mcp-server/          # MCP server implementation
│   ├── server.py        # Main server with tool routing
│   └── config.py        # Configuration and environment
├── workflows/           # Asset generation pipeline
│   ├── asset_generation.py
│   └── n8n_templates/   # n8n workflow templates
├── tools/               # Performance validation
│   ├── performance_validator.py
│   └── performance_report.py
├── docs/                # Comprehensive documentation
│   ├── GUIDE.md         # Usage guide
│   ├── EXAMPLES.md      # Real-world examples
│   └── ARCHITECTURE.md  # System architecture
└── pyproject.toml       # Python dependencies
```

## 📚 Documentation

- **[Usage Guide](docs/GUIDE.md)**: Complete feature documentation
- **[Examples](docs/EXAMPLES.md)**: 5 real-world scenarios
- **[Architecture](docs/ARCHITECTURE.md)**: System design and data flow

## 🛠️ Technology Stack

- **Python 3.10+**: Core implementation
- **Anthropic SDK**: Expert agent AI
- **Unity MCP**: Unity Editor integration
- **httpx**: Async HTTP client
- **Gemini/Leonardo/Meshy**: Asset generation APIs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

Built with Claude Code and Claude Sonnet 4.5

- Inspired by professional game dev workflows
- Unity MCP integration enables direct editor control
- Multi-agent validation prevents costly architectural mistakes

## 📬 Support

- **Issues**: [GitHub Issues](https://github.com/nategarelik/game-dev-supercharger/issues)
- **Discussions**: [GitHub Discussions](https://github.com/nategarelik/game-dev-supercharger/discussions)

---

**Made with 🎮 by Retro Baseball Dev**
