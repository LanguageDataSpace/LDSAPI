from ldsclient import LDSClient

import json

ldsutils = LDSClient();

# list files from local storage
files = ldsutils.get("/connector3/api/v1/storage/get_local_data");
print(files)

# list storages
storages = ldsutils.get("/connector3/api/v1/storage");
print(storages)







