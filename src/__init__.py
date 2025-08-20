# __init__.py
from .zwplayer_mcp_server import mcp

def main():
    """MCP zwplayer Server"""
    # Run server with streamable_http transport
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()