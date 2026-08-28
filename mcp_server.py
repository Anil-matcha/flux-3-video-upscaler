import json
from mcp.server.fastmcp import FastMCP
from flux3_video_upscaler_api import Flux3VideoUpscalerAPI

# Initialize FastMCP server
mcp = FastMCP("FLUX 3 Video Upscaler API Server")

# Helper to get API client
def get_api():
    return Flux3VideoUpscalerAPI()

@mcp.tool()
def upscale_video(video_url: str, prompt: str = None, upscale_factor: float = 2, creativity: int = 0) -> str:
    """
    Upscale an existing video beyond its native resolution using FLUX 3 Video Upscaler.

    :param video_url: URL of the source video to upscale.
    :param prompt: Optional text describing the desired enhancement direction, detail style, or visual refinement.
    :param upscale_factor: Multiplier controlling output resolution scaling (1-4, default 2).
    :param creativity: 0 = Precise ($1.43/run), 1 = Creative ($2.00/run). Default 0.
    """
    api = get_api()
    result = api.upscale_video(video_url, prompt=prompt, upscale_factor=upscale_factor, creativity=creativity)
    return json.dumps(result, indent=2)

@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image or video) to MuAPI for use in generation tasks.

    :param file_path: Local path to the file.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.

    :param request_id: The ID returned from a generation tool call.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run()
