# Copyright 2026 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Entry point for the MCP server."""

from ads_mcp.coordinator import mcp

# The following imports are necessary to register the tools with the `mcp`
# object, even though they are not directly used in this file.
# The `# noqa: F401` comment tells the linter to ignore the "unused import"
# warning.
from ads_mcp.tools import search, core, get_resource_metadata  # noqa: F401
from ads_mcp.resources import (
    discovery,
    metrics,
    release_notes,
    segments,
)  # noqa: F401


import os
from dotenv import load_dotenv


def run_server() -> None:
    load_dotenv()  # Load variables from .env file
    _CLIENT_ID = os.environ.get("GOOGLE_ADS_MCP_OAUTH_CLIENT_ID")
    _CLIENT_SECRET = os.environ.get("GOOGLE_ADS_MCP_OAUTH_CLIENT_SECRET")

    print(f"DEBUG: Found Client ID: {'Yes' if _CLIENT_ID else 'No'}")
    
    port = int(os.environ.get("PORT", 8000))
    is_web_env = "PORT" in os.environ

    if is_web_env or (_CLIENT_ID and _CLIENT_SECRET):
        transport = "streamable-http"
        print(f"DEBUG: Starting in {transport} mode on port {port}")
        if not _CLIENT_ID or not _CLIENT_SECRET:
            print("WARNING: Starting in HTTP mode without OAuth credentials.")
        mcp.run(transport=transport, host="0.0.0.0", port=port)
    else:
        print("DEBUG: Starting in stdio mode (No credentials found and no PORT set)")
        mcp.run()


if __name__ == "__main__":
    run_server()
