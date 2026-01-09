"""Asset generation via AI tools"""

import asyncio
import httpx
import base64
from typing import Dict, Any, List
import sys
from pathlib import Path

# Add config to path
sys.path.insert(0, str(Path(__file__).parent.parent / "mcp-server"))
from config import GEMINI_API_KEY, LEONARDO_API_KEY, MESHY_API_KEY

class AssetGenerator:
    """Generate 2D and 3D assets using AI tools"""

    def __init__(self):
        self.gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image-preview:generateImage"
        self.leonardo_url = "https://cloud.leonardo.ai/api/rest/v1/generations"
        self.meshy_url = "https://api.meshy.ai/v1/text-to-3d"

    async def generate_2d(
        self,
        prompt: str,
        style: str,
        count: int = 4,
        tool: str = "gemini"
    ) -> List[Dict[str, Any]]:
        """Generate 2D assets"""

        if tool == "gemini":
            return await self._generate_gemini(prompt, style, count)
        elif tool == "leonardo":
            return await self._generate_leonardo(prompt, style, count)
        elif tool == "flux":
            return await self._generate_flux(prompt, style, count)
        else:
            raise ValueError(f"Unknown 2D tool: {tool}")

    async def _generate_gemini(self, prompt: str, style: str, count: int) -> List[Dict[str, Any]]:
        """Generate via Gemini 2.5 Flash (free tier: 500/day)"""

        full_prompt = f"{prompt}. Art style: {style}. High quality game asset."

        results = []
        async with httpx.AsyncClient(timeout=60.0) as client:
            for i in range(count):
                response = await client.post(
                    f"{self.gemini_url}?key={GEMINI_API_KEY}",
                    json={
                        "prompt": full_prompt,
                        "numberOfImages": 1,
                        "aspectRatio": "1:1",
                        "safetySettings": [{"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}]
                    }
                )

                if response.status_code == 200:
                    data = response.json()
                    image_data = data.get("images", [{}])[0].get("image", "")
                    results.append({
                        "tool": "gemini",
                        "prompt": full_prompt,
                        "image_base64": image_data,
                        "index": i
                    })

        return results

    async def _generate_leonardo(self, prompt: str, style: str, count: int) -> List[Dict[str, Any]]:
        """Generate via Leonardo.ai (free: 150 tokens/day)"""

        model_id = "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3"  # Leonardo Phoenix

        full_prompt = f"{prompt}. Style: {style}. Game asset, clean background."

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                self.leonardo_url,
                headers={"Authorization": f"Bearer {LEONARDO_API_KEY}"},
                json={
                    "prompt": full_prompt,
                    "modelId": model_id,
                    "num_images": count,
                    "width": 512,
                    "height": 512,
                }
            )

            if response.status_code == 200:
                data = response.json()
                generation_id = data["sdGenerationJob"]["generationId"]

                # Poll for completion
                await asyncio.sleep(10)

                status_response = await client.get(
                    f"{self.leonardo_url}/{generation_id}",
                    headers={"Authorization": f"Bearer {LEONARDO_API_KEY}"}
                )

                images = status_response.json().get("generations_by_pk", {}).get("generated_images", [])

                return [
                    {
                        "tool": "leonardo",
                        "prompt": full_prompt,
                        "image_url": img["url"],
                        "index": i
                    }
                    for i, img in enumerate(images)
                ]

        return []

    async def _generate_flux(self, prompt: str, style: str, count: int) -> List[Dict[str, Any]]:
        """Generate via FLUX on HuggingFace (free)"""

        hf_url = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"

        full_prompt = f"{prompt}. {style} style. Game asset."

        results = []
        async with httpx.AsyncClient(timeout=60.0) as client:
            for i in range(count):
                response = await client.post(
                    hf_url,
                    headers={"Authorization": "Bearer YOUR_HF_TOKEN"},
                    json={"inputs": full_prompt}
                )

                if response.status_code == 200:
                    image_bytes = response.content
                    image_base64 = base64.b64encode(image_bytes).decode()
                    results.append({
                        "tool": "flux",
                        "prompt": full_prompt,
                        "image_base64": image_base64,
                        "index": i
                    })

        return results

    async def generate_3d(
        self,
        prompt: str,
        type: str = "text_to_3d",
        tool: str = "meshy"
    ) -> Dict[str, Any]:
        """Generate 3D model"""

        if tool == "meshy":
            return await self._generate_meshy(prompt, type)
        elif tool == "hunyuan3d":
            return await self._generate_hunyuan(prompt, type)
        else:
            raise ValueError(f"Unknown 3D tool: {tool}")

    async def _generate_meshy(self, prompt: str, type: str) -> Dict[str, Any]:
        """Generate via Meshy Pro"""

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                self.meshy_url,
                headers={"Authorization": f"Bearer {MESHY_API_KEY}"},
                json={
                    "mode": type,
                    "prompt": prompt,
                    "art_style": "realistic",
                    "negative_prompt": "low quality, low resolution"
                }
            )

            if response.status_code == 200:
                data = response.json()
                task_id = data["result"]

                # Poll for completion
                for _ in range(30):
                    await asyncio.sleep(10)

                    status_response = await client.get(
                        f"{self.meshy_url}/{task_id}",
                        headers={"Authorization": f"Bearer {MESHY_API_KEY}"}
                    )

                    status_data = status_response.json()
                    if status_data["status"] == "SUCCEEDED":
                        return {
                            "tool": "meshy",
                            "prompt": prompt,
                            "model_url": status_data["model_urls"]["glb"],
                            "thumbnail_url": status_data["thumbnail_url"]
                        }

                return {"error": "Timeout waiting for model generation"}

            return {"error": f"Failed to start generation: {response.status_code}"}

    async def _generate_hunyuan(self, prompt: str, type: str) -> Dict[str, Any]:
        """Generate via Hunyuan3D (local, requires GPU)"""
        # This would shell out to local Hunyuan3D installation
        return {"error": "Hunyuan3D requires local GPU setup"}
