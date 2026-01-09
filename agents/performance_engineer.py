"""Performance Engineer - Validates performance and optimization"""

from .base_expert import BaseExpert
from typing import Dict, Any, List

class PerformanceEngineer(BaseExpert):
    """Expert in game performance optimization"""

    def get_system_prompt(self) -> str:
        return """You are a performance optimization expert specializing in Unity mobile/web games.

Your expertise areas:
- Frame time budgets (60 FPS = 16.67ms, 30 FPS = 33.33ms)
- Draw call optimization and batching
- Memory management and garbage collection avoidance
- WebGL limitations and optimization
- Mobile GPU considerations
- Profiling and bottleneck identification

You have access to:
- Context7 for Unity Profiler documentation
- WebSearch for mobile performance best practices
- Knowledge of typical performance budgets

When analyzing decisions:
1. Calculate frame time impact
2. Identify potential bottlenecks (CPU/GPU/memory)
3. Suggest object pooling, batching, LOD strategies
4. Validate against platform-specific limits

Provide numbers and measurements, not just opinions."""

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "search_profiling_docs",
                "description": "Search Unity Profiler and optimization documentation",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "platform": {"type": "string"}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "estimate_frame_budget",
                "description": "Estimate frame time budget for a system",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "operation": {"type": "string"},
                        "frequency": {"type": "string"},
                        "platform": {"type": "string"}
                    },
                    "required": ["operation", "platform"]
                }
            }
        ]
