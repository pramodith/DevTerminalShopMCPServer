from mcp.server.fastmcp import FastMCP
from tools.terminal_shop_tools import get_coffee_products, run_order_workflow


def main():
    # Create an MCP server instance
    server = FastMCP(
        name="TerminalShop", instructions="An MCP server for ordering coffee products"
    )

    # Register the tools
    server.add_tool(get_coffee_products)
    server.add_tool(run_order_workflow)
    server.run()


if __name__ == "__main__":
    main()
