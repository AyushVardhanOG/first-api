from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime, timezone

class Handler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/status":
            self._send_json({"message": "Hello, world!"})
        elif self.path == "/status":
            self._send_json({"status": "ok", "time": datetime.now(timezone.utc).isoformat()})
        else:
            self._send_json({"error": "not found"}, status=404)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()