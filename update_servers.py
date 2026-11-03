
import json
import urllib.request
from pathlib import Path

OFFICIAL_URL = (
    "https://raw.githubusercontent.com/"
    "SideStore/anisette-servers/main/servers.json"
)

LOCAL_FILE = Path(__file__).parent / "servers.json"

# Read current personal server list
with LOCAL_FILE.open("r", encoding="utf-8") as f:
    local_data = json.load(f)

# Fetch official server list
with urllib.request.urlopen(OFFICIAL_URL) as response:
    official_data = json.load(response)

# Keep personal servers
personal_servers = [
    server for server in local_data["servers"]
    if server["name"] == "STJL's Server"
]

# Avoid duplicate addresses
personal_addresses = {
    server["address"] for server in personal_servers
}

official_servers = [
    server for server in official_data["servers"]
    if server["address"] not in personal_addresses
]

# Merge: personal server first, official servers afterwards
local_data["servers"] = personal_servers + official_servers

# Preserve existing cache field
with LOCAL_FILE.open("w", encoding="utf-8") as f:
    json.dump(local_data, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Updated successfully!")
print(f"Personal servers: {len(personal_servers)}")
print(f"Official servers: {len(official_servers)}")
print(f"Total servers: {len(local_data['servers'])}")
