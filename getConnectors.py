from ldsclient import LDSClient

import json

ldsclient = LDSClient();

# Get the list of connectors in LDS (not yet in Swagger documentation)
connectors = ldsclient.get("/connector3/api/v1/get_participant_list/")
print(connectors)





