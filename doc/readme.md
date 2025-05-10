source .venv/bin/activate


uv pip install . --system

http-mcp-server --port 9000
uv pip install  pydantic-settings

debug
mcp dev server.py

