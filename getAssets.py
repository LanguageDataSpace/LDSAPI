from ldsclient import LDSClient

ldsutils = LDSClient();

assets = ldsutils.get("/connector3/api/v1/assets");

print(assets)
