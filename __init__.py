"""
fal.ai MCP Server

A Model Context Protocol (MCP) server for interacting with fal.ai models and services.
"""

__version__ = "1.0.0"

from .main import create_server, main

__all__ = ["create_server", "main"]