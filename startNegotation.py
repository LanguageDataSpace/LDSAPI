from ldsclient import LDSClient

import json

ldsclient = LDSClient();

negotiation = ldsclient.post("/connector3/api/v1/contract_negotiations", "./payloads/negotiation.json");

print(negotiation)

# ./payloads/negotiation.json
# contains a lot of information. You can retrieve this info by calling
# /connector3/api/v1/retrieve_dataset/display/
# with
# {"catalog":"https://ldssetupdev.ilsp.gr/connector1","id":"e6baa89f-2e40-44aa-baa6-52f748cf1dc8"}
# as payload
