from mcp.server.fastmcp import FastMCP

mcp = FastMCP("example-server")

@mcp.tool(
    annotations={
        "title": "Calculate Sum",
        "readOnlyHint": True,
        "openWorldHint": False
    }
)
async def calculate_sum(a: float, b: float) -> str:
    """Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
    """
    result = a + b
    return str(result)
