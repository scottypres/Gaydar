#!/usr/bin/env python3
"""Serve the Gaydar app and expose audio-list.json listing audio files in root."""
import http.server
import json
import os
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO_EXTS = {".mp3", ".wav", ".ogg", ".m4a", ".aac", ".flac", ".opus", ".webm"}
PORT = int(os.environ.get("PORT", "8000"))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.split("?")[0] == "/audio-list.json":
            files = sorted(
                p.name for p in ROOT.iterdir()
                if p.is_file() and p.suffix.lower() in AUDIO_EXTS
            )
            body = json.dumps(files).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()


if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Gaydar running at http://localhost:{PORT}")
        httpd.serve_forever()
