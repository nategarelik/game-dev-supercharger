"""Visual Director - Validates art style and visual cohesion"""

from .base_expert import BaseExpert
from typing import Dict, Any, List

class VisualDirector(BaseExpert):
    """Expert in visual style, art direction, and asset quality"""

    def get_system_prompt(self) -> str:
        return """You are an art director with expertise in indie game visual design.

Your expertise areas:
- Art style consistency (pixel art, vector, 3D, etc.)
- Color theory and palette selection
- Visual hierarchy and readability
- Asset quality standards for Steam publishing
- Shader and post-processing effects
- UI/UX visual design

You have access to:
- AI art generation tools (Gemini, Leonardo, FLUX)
- Steam/itch.io for reference examples
- Knowledge of successful indie game art styles

When analyzing decisions:
1. Validate visual cohesion across assets
2. Check for "programmer art" vs professional quality
3. Suggest specific art techniques or tools
4. Reference successful similar visual styles

Be specific about colors, styles, and techniques."""

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "search_reference_games",
                "description": "Find games with similar visual style for reference",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "style": {"type": "string"},
                        "platform": {"type": "string"}
                    },
                    "required": ["style"]
                }
            },
            {
                "name": "generate_style_guide",
                "description": "Generate a visual style guide",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "game_genre": {"type": "string"},
                        "target_aesthetic": {"type": "string"}
                    },
                    "required": ["game_genre"]
                }
            }
        ]
