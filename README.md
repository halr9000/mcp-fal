# fal.ai MCP Server

A Model Context Protocol (MCP) server that lets MCP-compatible clients list, inspect, and run fal.ai models via stdio. Use it to integrate fal.ai’s serverless GPU inference into tools like Claude Desktop, Cursor, Windsurf, VSCode (Cline), and more.

## What is fal.ai (overview)

fal.ai is a serverless platform for running and fine‑tuning generative AI models on managed GPU infrastructure. It provides production‑grade REST and WebSocket APIs, streaming outputs, batch/queued processing, SDKs for Python/JS, autoscaling, and global GPU fleets (A100/H100 and more) for low‑latency inference of image, video, audio, 3D, and speech models.

- See: https://fal.ai
- Why enterprises choose fal.ai (uptime, latency, scaling): https://notablecap.com/blog/why-we-invested-in-fal-ai
- Case studies and ecosystem examples: https://www.tigrisdata.com/blog/case-study-falai/ and https://getdeploying.com/fal-ai

## Purpose of this MCP server

This server exposes convenience tools to your MCP client for:

- **List/Search models** and retrieve model schemas.
- **Run generation** with synchronous or queued execution, plus queue status/result helpers.
- **Upload files** to the fal.ai CDN for model inputs.

See tool reference below for exact names and parameters.

## Prerequisites

- **Python** 3.10+
- **uv** (package manager/runner): https://docs.astral.sh/uv/
- **FAL_KEY** environment variable (your fal.ai API key)

On Windows (PowerShell):
```powershell
$env:FAL_KEY = "YOUR_FAL_API_KEY_HERE"
```

On macOS/Linux (bash/zsh):
```bash
export FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

## Run with uvx (no local install)

- **This repo (example)**
```bash
uvx --from git+https://github.com/halr9000/mcp-fal@main mcp-fal
```
## Configure common MCP clients

Below is a minimal configuration that launches this server via uvx and passes your FAL_KEY. 

- **Claude Desktop** (Windows: `%AppData%/Claude/claude_desktop_config.json`, macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "fal.ai": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/halr9000/mcp-fal@main",
        "mcp-fal"
      ],
      "env": { "FAL_KEY": "YOUR_FAL_API_KEY_HERE" }
    }
  }
}
```

- **Cursor** (`~/.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "fal.ai": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/halr9000/mcp-fal@main",
        "mcp-fal"
      ],
      "env": { "FAL_KEY": "YOUR_FAL_API_KEY_HERE" }
    }
  }
}
```

- **Windsurf** (`~/.codeium/windsurf/mcp_config.json`)
```json
{
  "mcpServers": {
    "fal.ai": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/halr9000/mcp-fal@main",
        "mcp-fal"
      ],
      "env": { "FAL_KEY": "YOUR_FAL_API_KEY_HERE" }
    }
  }
}
```

## Local development (clone & run)

```bash
git clone https://github.com/halr9000/mcp-fal.git
cd mcp-fal
uv sync
uv run mcp-fal
```

Or run the inspector during development:
```bash
uv run -s inspect
```

Run directly from the local path with uvx (no venv activation):
```bash
uvx ./
# or explicitly
uvx ./mcp-fal
```

## Tools reference

- **`models(page=None, total=None)`** — list available models (optional pagination)
- **`search(keywords)`** — search for models by keyword(s)
- **`schema(model_id)`** — fetch OpenAPI schema for a model
- **`generate(model, parameters, queue=False)`** — run a model (sync or queued)
- **`status(url)` / `result(url)` / `cancel(url)`** — manage queued requests
- **`upload(path)`** — upload a file to fal.ai CDN

## License

[MIT](LICENSE)