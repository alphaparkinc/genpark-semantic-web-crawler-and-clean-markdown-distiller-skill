"""MCP server for Semantic Web Crawler & Clean Markdown Distiller."""
import sys
import json
from client import CleanMarkdownDistiller

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "distill_html_to_markdown",
                "description": "Converts raw HTML into clean LLM-ready Markdown and extracts links",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "html": {"type": "string"},
                        "source_url": {"type": "string"}
                    },
                    "required": ["html"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "distill_html_to_markdown":
            args = params.get("arguments", {})
            res = CleanMarkdownDistiller.distill_html_to_markdown(
                args.get("html", ""),
                args.get("source_url", "https://example.com")
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
