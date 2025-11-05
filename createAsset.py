from ldsclient import LDSClient

import json

ldsutils = LDSClient();

asset = ldsutils.post("/connector3/api/v1/assets", "./asset-jsonLDS.json");

print(asset)

