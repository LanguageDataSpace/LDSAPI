from ldsclient import LDSClient

import json

ldsclient = LDSClient();

assets = ldsclient.get("/connector3/api/v1/assets?offset=0&limit=200");

print(assets)

with open("assets.json", "w") as file:
    json.dump(assets, file, indent=4)

# Parse JSON into a Python dictionary
parsed = json.loads(assets)

# get data
data = parsed.get("data", [])

# Get the number of items in "data"
count = len(data)

print("number of assets:" + str(count))



