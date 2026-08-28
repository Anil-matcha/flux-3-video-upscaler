from setuptools import setup

setup(
    name="flux-3-video-upscaler-api",
    version="0.1.0",
    author="Anil Matcha",
    description="Python wrapper for Black Forest Labs' FLUX 3 Video Upscaler API -- upscale FLUX 3 (or any) video output beyond its native resolution.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["flux3_video_upscaler_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
