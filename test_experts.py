import asyncio
import sys
import os
from pathlib import Path

# Add project root to path so agents package can be imported
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "mcp-server"))

# Set API key in environment if not already set
if not os.getenv("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = ""

from agents.game_design_expert import GameDesignExpert
from config import ANTHROPIC_API_KEY

async def test_expert():
    print("Testing GameDesignExpert...")
    print(f"API Key available: {bool(ANTHROPIC_API_KEY)}")

    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set in environment")
        return

    expert = GameDesignExpert(ANTHROPIC_API_KEY)
    result = await expert.analyze(
        decision="Use Physics2D for arcade baseball ball physics",
        context="Building a retro arcade baseball game targeting mobile and web"
    )
    print(f"\n{result['expert']} Analysis:")
    print("=" * 60)
    print(result['analysis'])
    print("\nTool calls:", len(result['tool_calls']))
    print("Stop reason:", result['stop_reason'])

if __name__ == "__main__":
    asyncio.run(test_expert())
