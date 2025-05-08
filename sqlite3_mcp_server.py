import sqlite3

from mcp.server.fastmcp import FastMCP

# Create an object of FastMCP
mcp = FastMCP("SQLite Explorer")

# Resource: available at schema://main endpoint
@mcp.resource("schema://main")
def get_schema() -> str:
    """Provide the database schema as a resource"""
    conn = sqlite3.connect("Products.db")
    schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table'").fetchall()
    return "\n".join(sql[0] for sql in schema if sql[0])

# Tool: used to perform some action server side
@mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL queries safely"""
    try:
        conn = sqlite3.connect("Products.db")   # Connect to Products.db if exists or create new Products.db database
        print("Database connection successful!")
    except Exception as e:
        return f"Error: {str(e)}"
    try:
        result = conn.execute(sql).fetchall()
        return "\n".join(str(row) for row in result)
    except Exception as e:
        return f"Error: {str(e)}"