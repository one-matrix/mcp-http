source .venv/bin/activate


uv pip install . --system

http-mcp-server --port 9000
uv pip install  pydantic-settings

debug
mcp dev src/mcp_http/server.py 

delop:
uv pip install wheel twine
python -m build --wheel --outdir dist/
twine upload dist/mcp_http-0.1.0-py3-none-any.whl

cline
{
  "mcpServers": {
    "get_temperature": {
      "command": "uv",
      "args": [
        "--directory",
        "/src/mcp_http/",
        "run",
        "server.py"
      ],
      "disabled": false,
      "autoApprove": []
    },
  }
}