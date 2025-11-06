from ldsclient import LDSClient

import json

ldsclient = LDSClient();

remoteOffers = ldsclient.post("/connector3/api/v1/retrieve_catalogs/?page=1&size=1&sortField=name&sortOrder=asc"
                               "&merge=true", "./catalogs.json")
print(remoteOffers)




