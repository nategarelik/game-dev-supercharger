"""Configuration for Game Dev Supercharger"""

import os
from pathlib import Path

# Paths
PLUGIN_ROOT = Path(__file__).parent.parent
AGENTS_DIR = PLUGIN_ROOT / "agents"
WORKFLOWS_DIR = PLUGIN_ROOT / "workflows"
TOOLS_DIR = PLUGIN_ROOT / "tools"

# Unity MCP
UNITY_MCP_URL = os.getenv("UNITY_MCP_URL", "http://localhost:8080/mcp")

# AI Tools
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY", "")
MESHY_API_KEY = os.getenv("MESHY_API_KEY", "")

# Anthropic
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Performance Targets
PERFORMANCE_TARGETS = {
    "mobile": {"fps": 60, "frame_time_ms": 16.67, "draw_calls": 100},
    "web": {"fps": 30, "frame_time_ms": 33.33, "draw_calls": 50},
    "desktop": {"fps": 60, "frame_time_ms": 16.67, "draw_calls": 500},
}
