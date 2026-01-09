"""Game Design Expert - Validates game feel and player experience"""

from .base_expert import BaseExpert
from typing import Dict, Any, List

class GameDesignExpert(BaseExpert):
    """Expert in game feel, player psychology, and fun factor"""

    def get_system_prompt(self) -> str:
        return """You are an expert game designer with 15+ years shipping successful games.

Your expertise areas:
- Player psychology and engagement loops
- Game feel and "juice" (satisfying feedback)
- Difficulty curves and progression
- Input responsiveness and control schemes
- Arcade vs simulation balance

You have access to:
- Context7 for Unity game design patterns
- WebSearch for GDC talks, postmortems, player feedback
- Knowledge of top-selling indie games on Steam

When analyzing decisions:
1. Consider player experience first
2. Reference successful games in the genre
3. Identify potential fun-killers or friction
4. Suggest enhancements for "game feel"

Be opinionated but back it up with data."""

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "search_game_design_patterns",
                "description": "Search for game design patterns and best practices",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "genre": {"type": "string"}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "analyze_similar_games",
                "description": "Find and analyze similar successful games",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "genre": {"type": "string"},
                        "platform": {"type": "string"}
                    },
                    "required": ["genre"]
                }
            }
        ]
