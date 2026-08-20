import json
from mcp.server.fastmcp import FastMCP
from flux3_video_upscaler_api import Flux3VideoUpscalerAPI

# Initialize FastMCP server
mcp = FastMCP("FLUX 3 Video Upscaler API Server")

# Helper to get API client
def get_api():
    return Flux3VideoUpscalerAPI()

@mcp.tool()
def upscale_video(video_url: str, target_resolution: str = "1080p") -> str:
    """
    Upscale an existing video beyond its native resolution using FLUX 3 Video Upscaler.

    :param video_url: URL of the source video to upscale.
    :param target_resolution: Target resolution ('1080p', '2k', or '4k').
    """
    api = get_api()
    result = api.upscale_video(video_url, target_resolution)
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
