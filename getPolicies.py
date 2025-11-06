from ldsclient import LDSClient

import json

ldsclient = LDSClient();

policies = ldsclient.get("/connector3/es/policies/search?terms__policyClassification=publication+policy")
print("Access/Publication policies")
#print(policies)

policies = ldsclient.get("/connector3/es/policies/search?terms__policyClassification=contract+policy")
print("Contract policies")
print(policies)

