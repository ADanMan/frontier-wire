#!/usr/bin/env python3
"""Minimal MCP server for frontier-wire. Stdlib only, stdio JSON-RPC (newline-delimited)."""
import json
import re
import sys
import urllib.request

BASE = "https://adanman.github.io/frontier-wire"
TIMEOUT = 15

TOOLS = [
    {
        "name": "get_latest_edition",
        "description": "Fetch the latest frontier-wire edition as markdown text.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "get_feed",
        "description": "Fetch the frontier-wire feed.json contents as text.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "search_articles",
        "description": "Search frontier-wire llms-full.txt article chunks for a query string (up to 5 matches).",
        "inputSchema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
]


def fetch(url):
    with urllib.request.urlopen(url, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def tool_get_latest_edition(_args):
    return fetch(f"{BASE}/latest.md")


def tool_get_feed(_args):
    return fetch(f"{BASE}/feed.json")


def tool_search_articles(args):
    query = args.get("query", "")
    text = fetch(f"{BASE}/llms-full.txt")
    chunks = re.split(r"----- ", text)
    matches = [c for c in chunks if query.lower() in c.lower()]
    if not matches:
        return "No matches."
    trimmed = [m[:1200] for m in matches[:5]]
    return "\n\n---\n\n".join(trimmed)


DISPATCH = {
    "get_latest_edition": tool_get_latest_edition,
    "get_feed": tool_get_feed,
    "search_articles": tool_search_articles,
}


def rpc_result(msg_id, result):
    return {"jsonrpc": "2.0", "id": msg_id, "result": result}


def rpc_error(msg_id, code, message):
    return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}}


def handle_initialize(msg_id, params):
    protocol_version = (params or {}).get("protocolVersion", "2024-11-05")
    return rpc_result(msg_id, {
        "protocolVersion": protocol_version,
        "capabilities": {"tools": {}},
        "serverInfo": {"name": "frontier-wire", "version": "0.1.0"},
    })


def handle_tools_list(msg_id, _params):
    return rpc_result(msg_id, {"tools": TOOLS})


def handle_tools_call(msg_id, params):
    name = (params or {}).get("name")
    args = (params or {}).get("arguments", {}) or {}
    fn = DISPATCH.get(name)
    if fn is None:
        return rpc_error(msg_id, -32601, f"Unknown tool: {name}")
    try:
        text = fn(args)
        return rpc_result(msg_id, {"content": [{"type": "text", "text": text}], "isError": False})
    except Exception as exc:  # noqa: BLE001 - report failure to caller instead of crashing
        return rpc_result(msg_id, {
            "content": [{"type": "text", "text": f"Error: {exc}"}],
            "isError": True,
        })


def handle_message(msg):
    method = msg.get("method")
    msg_id = msg.get("id")

    if method == "initialize":
        return handle_initialize(msg_id, msg.get("params"))
    if method == "notifications/initialized":
        return None  # notification, no response
    if method == "tools/list":
        return handle_tools_list(msg_id, msg.get("params"))
    if method == "tools/call":
        return handle_tools_call(msg_id, msg.get("params"))
    if msg_id is None:
        return None  # unknown notification, ignore
    return rpc_error(msg_id, -32601, f"Method not found: {method}")


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as exc:
            sys.stdout.write(json.dumps(rpc_error(None, -32700, f"Parse error: {exc}")) + "\n")
            sys.stdout.flush()
            continue

        response = handle_message(msg)
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
