#!/usr/bin/env python3
"""
Example script showing how to run the fal.ai MCP server with uvx.
"""

import subprocess
import sys
import os

def run_with_uvx():
    """Run the MCP server using uvx."""
    
    # Check if FAL_KEY is set
    if not os.getenv("FAL_KEY"):
        print("Error: FAL_KEY environment variable not set.")
        print("Please set it with: export FAL_KEY='your-api-key-here'")
        sys.exit(1)
    
    # Check if uvx is available
    try:
        subprocess.run(["uvx", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: uvx is not installed or not in PATH.")
        print("Please install uv first: https://docs.astral.sh/uv/getting-started/installation/")
        sys.exit(1)
    
    print("Running fal.ai MCP server with uvx...")
    print("Press Ctrl+C to stop the server.")
    
    try:
        # Run the server with uvx
        subprocess.run([
            "uvx",
            "--from", ".",
            "--with", "fastmcp",
            "--with", "httpx", 
            "--with", "aiofiles",
            "python", "main.py"
        ], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_with_uvx()