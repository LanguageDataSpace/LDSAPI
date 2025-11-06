# LDS Connector API

This repository contains scripts/examples for interacting with the REST API of the LDS Connector.
It is split into two parts, the first is for acting as a provider of assets/offers and the second is for consumers.

## Act as an LDS provider 

We assume that we have already created at the Connector IAM (Keycloak) a user ```all_roles```
with password ```all_roles```. The user ```all_roles``` is assigned all available roles.


We have to log-in (programmatically via the Keycloak REST) and acquire an access token that will be used in all subsequent API calls. 
We can do that by running the following script that saves the access token (token.txt).

```
$ bash getAccessToken.sh all_roles all_roles
```

Then we can list the existing assets and get the number of them.

```
$ python getAssets.py
```

Let's insert an asset. Before that we need to upload the actual data to the built-in local storage.

```
$ bash uploadToEDC3.sh all_roles all_roles ./sample.zip
```

Lets' check that data were uploaded
```
$ python getLocalDatasets.py
```

Now we are ready to create an asset. Keep the asset id it will be needed when we will create an offer.

```
$ python createAsset.py
```

Let's do a quick check that we have one more asset 
```
$ python getAssets.py
```


## Act as an LDS consumer

Get the Connectors of the Data Space

```
$ python getConnectors.py
```

Get offers from a remote Connector
```
$ python getOffersFromARemoteConnector.py
```




