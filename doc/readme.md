source .venv/bin/activate


uv pip install . --system

http-mcp-server --port 9000
uv pip install  pydantic-settings

debug
mcp dev src/mcp_http/server.py 

delop:
uv pip install wheel twine
uv pip install build

python -m build --wheel --outdir dist/
twine upload dist/mcp_http-0.1.3-py3-none-any.whl

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

{
  "mcpServers": {
    "mcp-http": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/LIYUAN/Documents/Project/mcp-http/src/mcp_http/",
        "run",
        "server.py"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}

在src/mcp_http 目录下建一个__main__.py ，优化项目。使得这样可以运行运行 uvx src/mcp_http

python -m mcp_server_everything_search

python -m mcp_http
uvx src/mcp_http

uvx --from git+https://github.com/one-matrix/mcp-http mcp_http

uvx --from mcp-http mcp_http

uv pip install . --system

uvx mcp-http

uvx mcp_http


issue
uvx mcp_http
/Users/LIYUAN/.cache/uv/archive-v0/TdzJUF32lUDlCjAsI5iUO/bin/mcp_http: line 2: realpath: command not found
/Users/LIYUAN/.cache/uv/archive-v0/TdzJUF32lUDlCjAsI5iUO/bin/mcp_http: line 2: /Users/LIYUAN/Documents/Project/mcp-http/python: No such file or directory
/Users/LIYUAN/.cache/uv/archive-v0/TdzJUF32lUDlCjAsI5iUO/bin/mcp_http: line 2: exec: /Users/LIYUAN/Documents/Project/mcp-http/python: cannot execute: No such file or directory

fix
mac： brew install coreutils
