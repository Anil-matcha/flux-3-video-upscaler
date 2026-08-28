# FLUX 3 Video Upscaler API: Python Wrapper for Black Forest Labs' Beyond-Native-Resolution Video Upscaling

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=flux-3-video-upscaler-api)

[![PyPI version](https://img.shields.io/pypi/v/flux-3-video-upscaler-api.svg)](https://pypi.org/project/flux-3-video-upscaler-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/flux-3-video-upscaler.svg)](https://github.com/Anil-matcha/flux-3-video-upscaler/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python wrapper for **FLUX 3 Video Upscaler** — a live endpoint that raises FLUX 3 (or any) video output beyond its native generation resolution, delivered via [muapi.ai](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-upscaler-api). FLUX 3 Video launches capped at 720p/1080p, and this endpoint sharpens detail and raises resolution while preserving motion coherence and native audio sync — no re-generation required.

> **Status: Live.** `flux-3-video-upscaler` is live on MuAPI now. Pricing: **$1.43/run** at `creativity=0` (Precise) and **$2.00/run** at `creativity=1` (Creative), scaling with input video duration. [Get an API key](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-upscaler-api) to start using it.

## Related Projects

- [Flux-3-Dev-API](https://github.com/Anil-matcha/Flux-3-Dev-API) — Python SDK for FLUX 3 Dev, plus the full FLUX 3 image/video family
- [flux-3-video-edit](https://github.com/Anil-matcha/flux-3-video-edit) — Python SDK for FLUX 3's instruction-driven video editing mode
- [flux-3-omni](https://github.com/Anil-matcha/flux-3-omni) — Python SDK for FLUX 3's multi-reference Omni Reference mode
- [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) — Python wrapper focused on FLUX 3 Text-to-Video and Image-to-Video
- [awesome-flux-3-api-prompts](https://github.com/Anil-matcha/awesome-flux-3-api-prompts) — FLUX 3 API guide, prompt engineering, and a curated prompt library
- [flux-3-comfyui](https://github.com/Anil-matcha/flux-3-comfyui) — ComfyUI custom nodes for the FLUX 3 API
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — open-source, self-hosted AI image & video generation studio (200+ models)

## 🚀 Why FLUX 3 Video Upscaler?

FLUX 3 Video's initial general-availability release is capped at 720p resolution. **FLUX 3 Video Upscaler** is designed to bridge that gap:

- **Beyond-Native Resolution**: Deliver 1080p, 2K, or 4K output from a 720p FLUX 3 (or other) source clip.
- **Motion Coherence Preserved**: Sharpens detail without introducing warping or temporal artifacts.
- **Native Audio Sync Retained**: Upscaled output keeps the original clip's synchronized audio track intact.
- **Developer-First**: Simple Python SDK on top of MuAPI's unified infrastructure — no separate account or waitlist needed once you have a MuAPI key.

## 🌟 Key Features

- ✅ **FLUX 3 Video Upscaler**: Raise a video's resolution via `upscale_video()`.
- ✅ **File Upload**: Upload local videos directly using `upload_file()`.
- ✅ **MCP Server**: Use FLUX 3 Video Upscaler as a Model Context Protocol server for Claude Desktop, Cursor, and other MCP clients.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install flux-3-video-upscaler-api
```

### From Source
```bash
git clone https://github.com/Anil-matcha/flux-3-video-upscaler.git
cd flux-3-video-upscaler
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-upscaler-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 FLUX 3 Video Upscaler MCP Server

Use FLUX 3 Video Upscaler as an **MCP (Model Context Protocol)** server so AI clients (like Claude Desktop or Cursor) can directly invoke the upscaling tool.

### Running the MCP Server
1. Ensure `MUAPI_API_KEY` is set in your environment.
2. Run the server:
   ```bash
   python3 mcp_server.py
   ```
3. To test with the MCP Inspector:
   ```bash
   npx -y @modelcontextprotocol/inspector python3 mcp_server.py
   ```

---

## 💻 Quick Start (Python)

```python
from flux3_video_upscaler_api import Flux3VideoUpscalerAPI

# Initialize the client
api = Flux3VideoUpscalerAPI()

# Upscale an existing video clip
print("Submitting FLUX 3 Video Upscaler task...")
submission = api.upscale_video(
    video_url="https://example.com/clip-720p.mp4",
    upscale_factor=2,
    creativity=0
)

# Wait for completion
result = api.wait_for_completion(submission["request_id"])
print(f"Success! Output: {result['outputs'][0]}")
```

---

## 📡 API Endpoint & Reference

### FLUX 3 Video Upscaler
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-upscaler`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-video-upscaler" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "video_url": "https://example.com/clip-720p.mp4",
      "upscale_factor": 2,
      "creativity": 0
  }'
```

**Python SDK:**
```python
submission = api.upscale_video(
    video_url="https://example.com/clip-720p.mp4",
    upscale_factor=2,
    creativity=0,
)
result = api.wait_for_completion(submission["request_id"])
print(result["outputs"][0])
```

---

## 📖 Method Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `upscale_video` | `video_url`, `prompt` (optional), `upscale_factor` (1-4, default 2), `creativity` (0=Precise/1=Creative, default 0) | Upscale an existing video beyond its native resolution. $1.43/run at `creativity=0`, $2.00/run at `creativity=1`. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for a FLUX 3 Video Upscaler generation. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper that polls until the task completes. |

---

## 🔗 Official Resources
- **FLUX 3 Announcement (Black Forest Labs)**: [bfl.ai/models/flux-3](https://bfl.ai/models/flux-3)
- **Playground — FLUX 3 (all variants)**: [muapi.ai/flux-3](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-upscaler-api)
- **Playground — Video Upscaler (available today, other models)**: [muapi.ai/video-upscaler](https://muapi.ai/video-upscaler?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-upscaler-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-upscaler-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: FLUX 3 API, FLUX 3 Video Upscaler, FLUX 3 Video Upscaler API, Black Forest Labs FLUX 3, FLUX 3 Python SDK, FLUX 3 video upscaling, AI video upscaler API, AI video generation API, MuAPI, Python video upscaling SDK.
