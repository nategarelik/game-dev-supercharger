#!/usr/bin/env python3
"""Game Dev Supercharger MCP Server"""

import asyncio
import json
import sys
from typing import Any, Dict
from anthropic import Anthropic
import httpx

class GameDevMCPServer:
    """MCP server for game development tools"""

    def __init__(self):
        self.tools = self._register_tools()
        self.unity_mcp_url = "http://localhost:8080/mcp"

    def _register_tools(self) -> list[Dict[str, Any]]:
        """Register all available tools"""
        return [
            {
                "name": "spawn_expert_panel",
                "description": "Spawn specialized expert agents to validate a game development decision",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "decision": {"type": "string", "description": "The decision to validate"},
                        "experts": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["GameDesignExpert", "UnityArchitect", "PerformanceEngineer", "VisualDirector"]},
                            "description": "Which experts to consult"
                        },
                        "context": {"type": "string", "description": "Additional context for experts"}
                    },
                    "required": ["decision", "experts"]
                }
            },
            {
                "name": "unity_batch_command",
                "description": "Execute batch Unity commands via Unity MCP (up to 25 commands)",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "commands": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "Array of Unity MCP commands to execute",
                            "maxItems": 25
                        }
                    },
                    "required": ["commands"]
                }
            },
            {
                "name": "generate_2d_assets",
                "description": "Generate 2D game assets using AI (Gemini/Leonardo/FLUX)",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "prompt": {"type": "string", "description": "Asset description"},
                        "style": {"type": "string", "description": "Art style (pixel, vector, painterly)"},
                        "count": {"type": "integer", "description": "Number of variations", "default": 4},
                        "tool": {"type": "string", "enum": ["gemini", "leonardo", "flux"], "default": "gemini"}
                    },
                    "required": ["prompt", "style"]
                }
            },
            {
                "name": "generate_3d_assets",
                "description": "Generate 3D models using Meshy or Hunyuan3D",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "prompt": {"type": "string", "description": "Model description"},
                        "type": {"type": "string", "enum": ["text_to_3d", "image_to_3d"]},
                        "tool": {"type": "string", "enum": ["meshy", "hunyuan3d"], "default": "meshy"}
                    },
                    "required": ["prompt", "type"]
                }
            },
            {
                "name": "validate_performance",
                "description": "Run Unity performance profiling and validate against targets",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "platform": {"type": "string", "enum": ["mobile", "web", "desktop"]},
                        "target_fps": {"type": "integer", "default": 60}
                    },
                    "required": ["platform"]
                }
            }
        ]

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP requests"""
        method = request.get("method")
        params = request.get("params", {})

        if method == "tools/list":
            return {"tools": self.tools}

        elif method == "tools/call":
            tool_name = params.get("name")
            tool_input = params.get("arguments", {})

            # Route to appropriate handler
            handler = getattr(self, f"_handle_{tool_name}", None)
            if handler:
                return await handler(tool_input)
            else:
                return {"error": f"Unknown tool: {tool_name}"}

        return {"error": f"Unknown method: {method}"}

    async def _handle_spawn_expert_panel(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Spawn expert agents and return their consensus"""
        import sys
        from pathlib import Path

        # Add agents directory to path
        agents_path = Path(__file__).parent.parent / "agents"
        sys.path.insert(0, str(agents_path))

        from game_design_expert import GameDesignExpert
        from unity_architect import UnityArchitect
        from performance_engineer import PerformanceEngineer
        from visual_director import VisualDirector
        from config import ANTHROPIC_API_KEY

        decision = input_data["decision"]
        expert_names = input_data["experts"]
        context = input_data.get("context", "")

        # Map names to classes
        expert_classes = {
            "GameDesignExpert": GameDesignExpert,
            "UnityArchitect": UnityArchitect,
            "PerformanceEngineer": PerformanceEngineer,
            "VisualDirector": VisualDirector,
        }

        # Spawn experts in parallel
        experts = [expert_classes[name](ANTHROPIC_API_KEY) for name in expert_names]

        # Gather analyses
        analyses = []
        for expert in experts:
            analysis = await expert.analyze(decision, context)
            analyses.append(analysis)

        # Synthesize consensus
        consensus = self._synthesize_consensus(analyses)

        return {
            "decision": decision,
            "expert_analyses": analyses,
            "consensus": consensus
        }

    def _synthesize_consensus(self, analyses: list) -> Dict[str, Any]:
        """Synthesize expert opinions into consensus"""
        recommendations = []
        concerns = []

        for analysis in analyses:
            text = analysis["analysis"]
            # Simple keyword extraction (could be enhanced with LLM)
            if "approve" in text.lower():
                recommendations.append(f"{analysis['expert']}: Approve")
            elif "reject" in text.lower():
                recommendations.append(f"{analysis['expert']}: Reject")
            else:
                recommendations.append(f"{analysis['expert']}: Modify")

            # Extract concerns
            if "concern" in text.lower() or "risk" in text.lower():
                concerns.append(f"{analysis['expert']}: {text.split('concern')[-1][:200]}")

        return {
            "recommendations": recommendations,
            "major_concerns": concerns,
            "overall": "approved" if all("Approve" in r for r in recommendations) else "needs_revision"
        }

    async def _handle_unity_batch_command(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Forward batch commands to Unity MCP"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.unity_mcp_url}/batch_execute",
                json={"commands": input_data["commands"]}
            )
            return response.json()

    async def _handle_generate_2d_assets(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate 2D assets via AI tools"""
        import sys
        from pathlib import Path

        # Add workflows directory to path
        workflows_path = Path(__file__).parent.parent / "workflows"
        sys.path.insert(0, str(workflows_path))

        from asset_generation import AssetGenerator

        generator = AssetGenerator()
        results = await generator.generate_2d(
            prompt=input_data["prompt"],
            style=input_data["style"],
            count=input_data.get("count", 4),
            tool=input_data.get("tool", "gemini")
        )

        return {
            "status": "completed",
            "assets": results,
            "count": len(results)
        }

    async def _handle_generate_3d_assets(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate 3D assets via AI tools"""
        import sys
        from pathlib import Path

        # Add workflows directory to path
        workflows_path = Path(__file__).parent.parent / "workflows"
        sys.path.insert(0, str(workflows_path))

        from asset_generation import AssetGenerator

        generator = AssetGenerator()
        result = await generator.generate_3d(
            prompt=input_data["prompt"],
            type=input_data["type"],
            tool=input_data.get("tool", "meshy")
        )

        return {
            "status": "completed" if "model_url" in result else "failed",
            "asset": result
        }

    async def _handle_validate_performance(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Run performance validation"""
        import sys
        from pathlib import Path

        # Add tools directory to path
        tools_path = Path(__file__).parent.parent / "tools"
        sys.path.insert(0, str(tools_path))

        from performance_validator import PerformanceValidator

        validator = PerformanceValidator()
        result = await validator.validate(
            platform=input_data["platform"],
            target_fps=input_data.get("target_fps", 60)
        )

        return result

    async def run(self):
        """Start the MCP server"""
        while True:
            try:
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break

                request = json.loads(line)
                response = await self.handle_request(request)
                print(json.dumps(response), flush=True)

            except Exception as e:
                error_response = {"error": str(e)}
                print(json.dumps(error_response), flush=True)

if __name__ == "__main__":
    server = GameDevMCPServer()
    asyncio.run(server.run())
