from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)-> int:
    """__summary__
    Add two numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int)-> int:
    """
    Multipy  two numbers
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
