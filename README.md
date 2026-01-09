# Universal Game Dev Supercharger

Claude Code MCP plugin for professional 2D/3D Unity game development.

## Features

- **Multi-Agent Expert Panel**: GameDesignExpert, UnityArchitect, PerformanceEngineer, VisualDirector
- **Unity MCP Integration**: Direct Unity Editor control via batch_execute
- **Automated Asset Pipeline**: n8n workflows for Gemini/Leonardo/Meshy
- **Reusable Tools**: Scene composition, performance profiling, architecture validation

## Installation

```bash
# Install Unity MCP first
# Download from: https://assetstore.unity.com/packages/tools/generative-ai/mcp-for-unity-ai-driven-development-329908

# Configure Claude Code
claude mcp add --scope user GameDevSupercharger -- uv --directory ~/.claude-plugins/game-dev-supercharger/mcp-server run server.py
```

## Architecture

- `mcp-server/` - MCP server for Claude Code integration
- `agents/` - Expert agent prompts and tools
- `workflows/` - n8n asset pipeline templates
- `tools/` - Reusable Unity development tools
