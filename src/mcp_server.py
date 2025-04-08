from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import Settings
from tools.terminal_shop_tools import (
    get_coffee_products,
    run_order_workflow,
    create_address,
    get_all_orders
)


def main():
    # Create an MCP server instance
    server = FastMCP(
        name="TerminalShop",
        instructions="An MCP server for ordering coffee products",
        settings=Settings(log_level="DEBUG", debug=True),
    )

    # Register the tools
    server.add_tool(get_coffee_products)
    server.add_tool(create_address)
    server.add_tool(run_order_workflow)
    server.add_tool(get_all_orders)

    server.run()


if __name__ == "__main__":
    main()
