#!/usr/bin/env python3
import os
import platform
import socket

print("[PYTHON] Redline Diagnostics")
print("System:", platform.system(), platform.release())
print("Hostname:", socket.gethostname())
print("User:", os.getenv("USER", "unknown"))
print("Status: online")
