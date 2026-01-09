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

```bash
# Clone the repository
git clone https://github.com/nategarelik/game-dev-supercharger.git
cd game-dev-supercharger

# Run installation script
./install.sh

# Configure API keys
cp env.example .env
# Edit .env with your keys

# Add to Claude Code
claude mcp add --scope user GameDevSupercharger \
  -- uv --directory $(pwd)/mcp-server run server.py
```

### API Keys Required

- **Anthropic API Key** (required): Expert panel functionality
- **Gemini API Key** (optional): Free 2D asset generation (500/day)
- **Leonardo API Key** (optional): Premium 2D assets (150 tokens/day free)
- **Meshy API Key** (optional): 3D model generation ($20/mo)

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

## 📁 Project Structure

```
game-dev-supercharger/
├── mcp-server/          # MCP server implementation
│   ├── server.py        # Main server with tool routing
│   └── config.py        # Configuration and environment
├── agents/              # Expert AI agents
│   ├── base_expert.py
│   ├── game_design_expert.py
│   ├── unity_architect.py
│   ├── performance_engineer.py
│   └── visual_director.py
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
