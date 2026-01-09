#!/bin/bash
# Installation script for Game Dev Supercharger

set -e

echo "🎮 Installing Game Dev Supercharger..."

# Check Python version
python_version=$(python3 --version 2>/dev/null | cut -d' ' -f2 | cut -d'.' -f1-2 || echo "0.0")
if [ $(echo "$python_version < 3.10" | bc -l 2>/dev/null || echo "1") -eq 1 ]; then
    echo "❌ Python 3.10+ required (found $python_version)"
    exit 1
fi
echo "✅ Python $python_version"

# Check uv
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi
echo "✅ uv installed"

# Install plugin dependencies
echo "📦 Installing dependencies..."
cd "$(dirname "$0")"
uv venv
source .venv/bin/activate || source .venv/Scripts/activate
uv pip install -e ".[dev]"
echo "✅ Dependencies installed"

# Check for Unity MCP
if ! curl -s http://localhost:8080/mcp > /dev/null 2>&1; then
    echo "⚠️  Unity MCP not running at localhost:8080"
    echo "   Install from: https://assetstore.unity.com/packages/tools/generative-ai/mcp-for-unity-ai-driven-development-329908"
    echo "   Then start: Window > MCP for Unity > Start Server"
else
    echo "✅ Unity MCP detected"
fi

# Create .env from example
if [ ! -f .env ]; then
    cp env.example .env
    echo "📝 Created .env file - please configure API keys"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your API keys"
echo "2. Add to Claude Code:"
echo "   claude mcp add --scope user GameDevSupercharger -- uv --directory $(pwd)/mcp-server run server.py"
echo "3. Start Unity and run Window > MCP for Unity > Start Server"
echo "4. Start building games!"
