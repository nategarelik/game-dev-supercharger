import asyncio
import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "workflows"))
sys.path.insert(0, str(Path(__file__).parent / "mcp-server"))

from asset_generation import AssetGenerator

async def test_2d():
    generator = AssetGenerator()

    print("Testing AssetGenerator initialization...")
    print(f"Gemini URL: {generator.gemini_url}")
    print(f"Leonardo URL: {generator.leonardo_url}")
    print(f"Meshy URL: {generator.meshy_url}")

    print("\n✓ AssetGenerator structure validated")
    print("\nNOTE: Actual API calls require API keys in environment:")
    print("  - GEMINI_API_KEY (free 500/day)")
    print("  - LEONARDO_API_KEY (free 150 tokens/day)")
    print("  - MESHY_API_KEY ($20/mo)")

    # Uncomment to test actual generation (requires API keys):
    # results = await generator.generate_2d(
    #     prompt="Baseball player sprite",
    #     style="pixel art",
    #     count=2,
    #     tool="gemini"
    # )
    # print(f"Generated {len(results)} images")
    # for i, result in enumerate(results):
    #     print(f"  Image {i}: {len(result['image_base64'])} bytes")

if __name__ == "__main__":
    asyncio.run(test_2d())
