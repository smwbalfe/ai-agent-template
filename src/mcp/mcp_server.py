from fastmcp import FastMCP

mcp = FastMCP("simple-mcp")

@mcp.tool()
async def hello(name: str) -> str:
    return f"Hello {name}!"

if __name__ == "__main__":
    mcp.run()