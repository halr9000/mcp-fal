"""
fal.ai MCP Server : Main entry point

This module sets up and runs the fal.ai MCP server,
providing tools to interact with fal.ai models and services.
"""

import sys
from fastmcp import FastMCP
from api.models import register_model_tools
from api.generate import register_generation_tools
from api.storage import register_storage_tools
from api.config import get_api_key, SERVER_NAME, SERVER_DESCRIPTION, SERVER_VERSION, SERVER_DEPENDENCIES

def create_server():
    """Create and configure the FastMCP server."""
    mcp = FastMCP(
        name=SERVER_NAME,
        dependencies=SERVER_DEPENDENCIES
    )
    
    register_model_tools(mcp)
    register_generation_tools(mcp)
    register_storage_tools(mcp)
    
    return mcp

def main():
    """Main entry point for the MCP server."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="fal.ai MCP Server - A Model Context Protocol server for fal.ai"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"fal-ai-mcp-server {SERVER_VERSION}"
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="Transport protocol to use (default: stdio)"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to when using http transport (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to when using http transport (default: 8000)"
    )
    
    args = parser.parse_args()
    
    try:
        # Validate API key is available
        get_api_key()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Please set the FAL_KEY environment variable with your fal.ai API key.", file=sys.stderr)
        sys.exit(1)
    
    try:
        mcp = create_server()
        
        if args.transport == "http":
            print(f"Starting fal.ai MCP server on http://{args.host}:{args.port}/mcp", file=sys.stderr)
            mcp.run(transport="http", host=args.host, port=args.port)
        else:
            print("Starting fal.ai MCP server with stdio transport", file=sys.stderr)
            mcp.run()
            
    except KeyboardInterrupt:
        print("\nServer stopped by user.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        sys.exit(1)

# Create the server instance for uvx compatibility
mcp = create_server()

if __name__ == "__main__":
    main()