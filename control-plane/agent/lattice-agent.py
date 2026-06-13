#!/usr/bin/env python3

import json
import socket
import subprocess
import shutil
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except Exception:
        return "unknown"


def get_metrics():
    hostname = socket.gethostname()
    ip = run("hostname -I | awk '{print $1}'")
    uptime = run("uptime -p")
    kernel = run("uname -r")
    temp = run("vcgencmd measure_temp 2>/dev/null || echo unknown")
    nvme = run("nvme list | grep 'Samsung SSD 980' || echo not_detected")

    total, used, free = shutil.disk_usage("/")

    return {
        "hostname": hostname,
        "ip": ip,
        "uptime": uptime,
        "kernel": kernel,
        "temperature": temp,
        "root_disk": {
            "total_gb": round(total / (1024**3), 2),
            "used_gb": round(used / (1024**3), 2),
            "free_gb": round(free / (1024**3), 2),
        },
        "nvme": nvme,
        "timestamp": int(time.time()),
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            return

        if self.path == "/metrics.json":
            data = json.dumps(get_metrics(), indent=2).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)
            return

        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8088), Handler)
    print("lattice-agent listening on port 8088")
    server.serve_forever()
