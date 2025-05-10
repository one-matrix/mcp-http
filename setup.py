from setuptools import setup, find_packages

setup(
    name="mcp—http",
    version="0.1.0",
    description="A MCP HTTP server",
    author="one-matrix",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "fastmcp[cli]>=2.3.1",
        "httpx>=0.28.1",
    ],
    python_requires=">=3.9",
    url="https://github.com/one-matrix/mcp-http",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
