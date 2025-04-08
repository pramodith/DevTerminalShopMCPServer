# PizzaMCP - Terminal Coffee Shop

A terminal-based coffee ordering system built with Python using MCP (Machine Control Protocol) server. This application allows users to browse coffee products, place orders, and manage shipping information through a simple terminal interface.

## Features

- Browse available coffee products with descriptions and prices
- Manage shipping addresses
- Secure credit card processing
- Order tracking with unique order IDs
- Interactive terminal-based user interface

## Prerequisites

- Python 3.x
- Terminal Shop Client
- FastMCP Server

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PizzaMCP.git
cd PizzaMCP
```

2. Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv sync
```

## Usage

1. Start the MCP server:
```bash
python src/mcp_server.py
or
uv --directory PATH_TO_SRC run mcp_server.py
```

2. The server will guide you through:
   - Browsing available coffee products
   - Entering shipping information
   - Processing payment
   - Confirming your order

## Project Structure

- `src/`
  - `mcp_server.py` - Main server implementation
  - `utils.py` - Utility functions for Terminal Shop operations
  - `tools/`
    - `terminal_shop_tools.py` - Core shopping functionality

## Environment Variables

Create a `.env` file in the root directory with:
```
TERMINAL_SHOP_API_KEY=your_api_key
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
