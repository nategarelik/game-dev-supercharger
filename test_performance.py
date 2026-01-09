import asyncio
import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "tools"))
sys.path.insert(0, str(Path(__file__).parent / "mcp-server"))

from performance_validator import PerformanceValidator
from performance_report import generate_markdown_report

async def test_validation():
    print("Testing Performance Validation...")
    validator = PerformanceValidator()
    result = await validator.validate(platform="mobile", target_fps=60)

    print("Validation Result:")
    print(f"Status: {result['summary']}")
    print(f"Issues: {len(result['issues'])}")

    report = generate_markdown_report(result)
    print("\nMarkdown Report:")
    print(report)

if __name__ == "__main__":
    asyncio.run(test_validation())
