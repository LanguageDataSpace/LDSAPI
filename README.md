# LDS Connector API


## Provider

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


