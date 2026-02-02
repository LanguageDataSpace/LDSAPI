from ldsclient import LDSClient

import json

ldsclient = LDSClient();

# list files from local storage
files = ldsclient.get("/api/v1/storage/get_local_data");
print(files)

# list storages
storages = ldsclient.get("/api/v1/storage");
print(storages)







