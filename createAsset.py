from ldsclient import LDSClient

import json

ldsclient = LDSClient();

asset = ldsclient.post("/connector3/api/v1/assets", "./payloads/asset-jsonLDS.json");

print(asset)

