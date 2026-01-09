"""Base class for expert agents"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List
from anthropic import Anthropic

class BaseExpert(ABC):
    """Base class for specialized expert agents"""

    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-5-20250929"
        self.name = self.__class__.__name__

    @abstractmethod
    def get_system_prompt(self) -> str:
        """Return the system prompt for this expert"""
        pass

    @abstractmethod
    def get_tools(self) -> List[Dict[str, Any]]:
        """Return tools available to this expert"""
        pass

    async def analyze(self, decision: str, context: str = "") -> Dict[str, Any]:
        """Analyze a decision and provide expert opinion"""

        prompt = f"""You are {self.name}, a specialized expert in game development.

Decision to analyze:
{decision}

Additional context:
{context}

Provide your expert analysis covering:
1. Your assessment of this approach
2. Risks or concerns from your expertise area
3. Alternative approaches if this is suboptimal
4. Your recommendation (approve/reject/modify)

Be direct and technical. Cite specific Unity docs, performance data, or industry practices.
"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            system=self.get_system_prompt(),
            tools=self.get_tools(),
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract analysis from response
        analysis_text = ""
        tool_calls = []

        for block in response.content:
            if block.type == "text":
                analysis_text += block.text
            elif block.type == "tool_use":
                tool_calls.append({
                    "tool": block.name,
                    "input": block.input
                })

        return {
            "expert": self.name,
            "analysis": analysis_text,
            "tool_calls": tool_calls,
            "stop_reason": response.stop_reason
        }
