from ldsclient import LDSClient

import json

ldsclient = LDSClient();

offer = ldsclient.post("/connector3/api/v1/contract", "./payloads/contract-offer.json");

print(offer)
