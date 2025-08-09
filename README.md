# fal.ai MCP Server

A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

## Features

- List all available fal.ai models
- Search for specific models by keywords
- Get model schemas
- Generate content using any fal.ai model
- Support for both direct and queued model execution
- Queue management (status checking, getting results, cancelling requests)
- File upload to fal.ai CDN

## Requirements

- Python 3.10+
- A fal.ai API key

## Installation

### Using uvx (Recommended)

The easiest way to use this MCP server is with `uvx`, which handles all dependencies automatically:

```bash
# Set your fal.ai API key
export FAL_KEY="YOUR_FAL_API_KEY_HERE"

# Run directly with uvx (from GitHub)
uvx --from git+https://github.com/halr9000/mcp-fal.git --with fastmcp --with httpx --with aiofiles python main.py

# Or clone and run locally
git clone https://github.com/halr9000/mcp-fal.git
cd mcp-fal
uvx --from . --with fastmcp --with httpx --with aiofiles python main.py
```

### Traditional Installation

1. Clone this repository:

```bash
git clone https://github.com/halr9000/mcp-fal.git
cd mcp-fal
```

2. Install the package:

```bash
pip install -e .
```

3. Set your fal.ai API key as an environment variable:

```bash
export FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

## Usage

### Using with uvx in MCP Configuration

Add this to your MCP client configuration (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "fal-ai": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/halr9000/mcp-fal.git",
        "--with", "fastmcp",
        "--with", "httpx",
        "--with", "aiofiles",
        "python", "main.py"
      ],
      "env": {
        "FAL_KEY": "YOUR_FAL_API_KEY_HERE"
      }
    }
  }
}
```

### Development Mode

You can run the server in development mode with:

```bash
fastmcp dev main.py
```

This will launch the MCP Inspector web interface where you can test the tools interactively.

### Installing in Claude Desktop with FastMCP

To use the server with Claude Desktop using FastMCP:

```bash
fastmcp install claude-desktop main.py --env FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

### Running Directly

You can also run the server directly:

```bash
python main.py
```

## API Reference

### Tools

- `models(page=None, total=None)` - List available models with optional pagination
- `search(keywords)` - Search for models by keywords
- `schema(model_id)` - Get OpenAPI schema for a specific model
- `generate(model, parameters, queue=False)` - Generate content using a model
- `result(url)` - Get result from a queued request
- `status(url)` - Check status of a queued request
- `cancel(url)` - Cancel a queued request
- `upload(path` - Upload a file to fal.ai CDN

## License

[MIT](LICENSE)
