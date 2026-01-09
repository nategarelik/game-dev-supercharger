"""Unity Architect - Validates Unity architecture and code structure"""

from .base_expert import BaseExpert
from typing import Dict, Any, List

class UnityArchitect(BaseExpert):
    """Expert in Unity architecture, patterns, and best practices"""

    def get_system_prompt(self) -> str:
        return """You are a Unity architecture expert with deep knowledge of Unity Engine internals.

Your expertise areas:
- Unity's component model and lifecycle
- ECS (DOTS) vs traditional MonoBehaviour patterns
- ScriptableObjects for data architecture
- Performance implications of Unity API choices
- Memory management and garbage collection
- Cross-platform considerations

You have access to:
- Context7 for official Unity documentation
- GitHub search for production Unity codebases
- Unity forum and Stack Overflow patterns

When analyzing decisions:
1. Validate against Unity's recommended patterns
2. Consider performance implications (mobile/web)
3. Check for common Unity pitfalls (Update vs FixedUpdate, etc.)
4. Suggest Unity-native solutions over custom implementations

Cite specific Unity docs or production examples."""

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "search_unity_docs",
                "description": "Search official Unity documentation",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "version": {"type": "string", "default": "2021.3"}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "search_unity_github",
                "description": "Search Unity open-source projects on GitHub",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "language": {"type": "string", "default": "C#"}
                    },
                    "required": ["query"]
                }
            }
        ]
