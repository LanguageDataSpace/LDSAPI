# LDS Connector API

This repository contains scripts/examples for interacting with the REST API of the LDS Connector.
It is split into two parts, the first is for acting as a provider of assets/offers and the second is for consumers.

## Act as an LDS provider 

We assume that we have already created at the Connector IAM (Keycloak) a user ```all_roles```
with password ```all_roles```. The user ```all_roles``` is assigned all available roles.


**Get access token** 

We have to log-in (programmatically via the Keycloak REST) and acquire an access token that will be used in all subsequent API calls. 
We can do that by running the following script that saves the access token (token.txt).

```
$ bash getAccessToken.sh all_roles all_roles
```

Output:
```
username:all_roles
password:all_roles
instance:LDS3
curl --location --request POST 'https://ldssetupdev.ilsp.gr/auth/realms/LDS3/protocol/openid-connect/token' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'client_id=connector-3-ui' --data-urlencode 'grant_type=password' --data-urlencode 'username=all_roles' --data-urlencode 'password=all_roles'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2858  100  2776  100    82   4939    145 --:--:-- --:--:-- --:--:--  5085
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMWXJZMHNaYTRHeTl1RnZBekQxNy1LMGx2bzdhbDBVeTFmU1FnS25rUnhFIn0.eyJleHAiOjE3NjI0MzU5NzgsImlhdCI6MTc2MjQxNzk3OCwianRpIjoiZDgzZGUxNTAtYzAwYS00YjU1LTg2OTktNDg0NTI4MGFkMTJmIiwiaXNzIjoiaHR0cHM6Ly9sZHNzZXR1cGRldi5pbHNwLmdyL2F1dGgvcmVhbG1zL0xEUzMiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMmQ4N2EwYmYtMjI2ZC00NWZiLWFhMjYtNjc5ZmYyODhlNTE0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29ubmVjdG9yLTMtdWkiLCJzZXNzaW9uX3N0YXRlIjoiNDZkNjVlN2ItMjRmYi00ODYyLWFiNzgtNjVjYTBkNWJmOGY0IiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL2xkc3NldHVwZGV2Lmlsc3AuZ3IiLCJodHRwOi8vZWxnLWZyb250Lmlsc3AuZ3I6MzAwMi8qIiwiaHR0cDovL2VsZy1mcm9udC5pbHNwLmdyOjMwMDIiLCJodHRwOi8vbG9jYWxob3N0OjMwMDAvKiIsImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGF0YV9tYW5hZ2VyIiwiZGF0YV9hY3F1aXNpdGlvbl9tYW5hZ2VyIiwiZGVmYXVsdC1yb2xlcy1sZHMzIiwiYnVzaW5lc3NfYW5hbHl0aWNzX2FuZF9yZXBvcnRpbmciLCJkZWZhdWx0LXJvbGVzLWxkcyIsIm9mZmxpbmVfYWNjZXNzIiwiZGF0YV91c2VyIiwiY29ubmVjdG9yX2FkbWluIiwibGVnYWxfYWRtaW4iLCJmaW5hbmNpYWxfYWRtaW4iLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRhdGFfc2FsZXNfbWFuYWdlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjQ2ZDY1ZTdiLTI0ZmItNDg2Mi1hYjc4LTY1Y2EwZDViZjhmNCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiYWxsX3JvbGVzIGFsbF9yb2xlcyIsInByZWZlcnJlZF91c2VybmFtZSI6ImFsbF9yb2xlcyIsImdpdmVuX25hbWUiOiJhbGxfcm9sZXMiLCJmYW1pbHlfbmFtZSI6ImFsbF9yb2xlcyIsImVtYWlsIjoidGVzdEB0ZXN0In0.ZXkONZFmZ_FFhh1SrIspCbRXkH05taO09sJUo2Bfh83MpePjw994rp2GiLfb0-bunvK6hDzC4kI2Mug_WSjP4bil9CQiPSwmA44EjX98mIcG5Xilqfc2q42PZde-CXBCD0jqd_aWZoUrCN_gIXVxnJPNKiSS_hcg95aNUT4L93bJoDQLJpfXe9FVl4XDQINKN5VKx2oVOdmkPxsqBJwGmgp3KoclzJimqMYJ6hZVTjYXSFQ32oK28nZomTsi7IZ758I1x18RP8KuRHOQstFOjP4ine6A4qGTqp99oBcz_coDv5GUkClcoWdEdpUrg8Cg-3Yl5A8Z4f40H6Gmsivkqg","expires_in":18000,"refresh_expires_in":1800,"refresh_token":"eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJkZWVmMTc1My0wNzU3LTRiMzMtOWRkYS0zNWQxNTk1YWE4MmUifQ.eyJleHAiOjE3NjI0MTk3NzgsImlhdCI6MTc2MjQxNzk3OCwianRpIjoiYjgxMjM3NGYtNDk4Zi00YTM5LWFlNTgtZDBmNWMwZmFjMmZlIiwiaXNzIjoiaHR0cHM6Ly9sZHNzZXR1cGRldi5pbHNwLmdyL2F1dGgvcmVhbG1zL0xEUzMiLCJhdWQiOiJodHRwczovL2xkc3NldHVwZGV2Lmlsc3AuZ3IvYXV0aC9yZWFsbXMvTERTMyIsInN1YiI6IjJkODdhMGJmLTIyNmQtNDVmYi1hYTI2LTY3OWZmMjg4ZTUxNCIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJjb25uZWN0b3ItMy11aSIsInNlc3Npb25fc3RhdGUiOiI0NmQ2NWU3Yi0yNGZiLTQ4NjItYWI3OC02NWNhMGQ1YmY4ZjQiLCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJzaWQiOiI0NmQ2NWU3Yi0yNGZiLTQ4NjItYWI3OC02NWNhMGQ1YmY4ZjQifQ.-EoS9U-exuvBkv8UvPiNMeWPw9pbx54y4zsiMccCsahh_cMEiPCjAAcvSc-woCaBapXJG5EKX5DPYCThW0cE6g","token_type":"Bearer","not-before-policy":0,"session_state":"46d65e7b-24fb-4862-ab78-65ca0d5bf8f4","scope":"profile email"}
\n
```

**List existing assets** 

Then we can list the existing assets and get the number of them.

```
$ python getAssets.py
```

**Upload asset actual data** 

Let's insert an asset. Before that we need to upload the actual data to the built-in local storage.

```
$ bash uploadToEDC3.sh all_roles all_roles ./sample.zip
```

**Check that it was uploaded** 

Lets' check that data were uploaded
```
$ python getLocalDatasets.py
```

**Create an asset** 

Now we are ready to create an asset. Keep the asset id it will be needed when we will create an offer.

```
$ python createAsset.py
```

**List assets again** 

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




