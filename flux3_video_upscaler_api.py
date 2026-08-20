import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Flux3VideoUpscalerAPI:
    def __init__(self, api_key=None):
        """
        Initialize the FLUX 3 Video Upscaler API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")

        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def upscale_video(self, video_url, target_resolution="1080p"):
        """
        Submits a FLUX 3 Video Upscaler task.

        FLUX 3 Video Upscaler raises FLUX 3 (or any) video output beyond its
        native generation resolution, sharpening detail while preserving
        motion coherence and native audio sync. FLUX 3 Video launches capped
        at 720p ahead of a planned 1080p+ rollout, so this endpoint is
        designed to bridge that gap.

        :param video_url: URL of the source video to upscale.
        :param target_resolution: Target resolution ('1080p', '2k', or '4k').
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/flux-3-video-upscaler"
        payload = {
            "video_url": video_url,
            "target_resolution": target_resolution,
        }
        return self._post_request(endpoint, payload)

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a file (image or video) to MuAPI for use in generation tasks.

        :param file_path: Path to the local file to upload.
        :return: JSON response from MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"

        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }

        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)

        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=300):
        """
        Waits for the generation task to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")

            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Generation failed: {result.get('error')}")

            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for generation to complete.")


if __name__ == "__main__":
    # Example usage for FLUX 3 Video Upscaler
    try:
        api = Flux3VideoUpscalerAPI()
        video_url = "https://example.com/clip-720p.mp4"

        print(f"Submitting FLUX 3 Video Upscaler task for: {video_url}")
        submission = api.upscale_video(video_url=video_url, target_resolution="4k")
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")

        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Output: {result.get('outputs', [result.get('url')])}")

    except Exception as e:
        print(f"Error: {e}")
