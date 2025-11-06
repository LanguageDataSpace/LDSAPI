from ldsclient import LDSClient

import json

ldsclient = LDSClient();

# retrieves the contract definition
offer = ldsclient.get("/connector3/api/v1/contract/48841f36-d95b-43ef-b65f-ad46ffbec21c");

print(offer)

# retrieves the metadata description
offer = ldsclient.get("/connector3/es/offers/48841f36-d95b-43ef-b65f-ad46ffbec21c");

print(offer)