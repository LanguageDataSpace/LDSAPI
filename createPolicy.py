from ldsclient import LDSClient

import json

ldsclient = LDSClient();

offer = ldsclient.post("/connector1/api/v1/contract", "./payloads/contract-offer.json");

print(offer)

