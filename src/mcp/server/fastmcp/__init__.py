"""FastMCP - A more ergonomic interface for MCP servers."""

from importlib.metadata import version, PackageNotFoundError

from mcp.types import Icon

from .server import Context, FastMCP
from .utilities.types import Audio, Image

try:
    __version__ = version("mcp")
except PackageNotFoundError:
    # Package metadata not found (e.g. running from source/Bazel)
    __version__ = "0.0.0-dev"
__all__ = ["FastMCP", "Context", "Image", "Audio", "Icon"]
