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
bash getAccessToken.sh all_roles all_roles
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
python getAssets.py
```
Output:

```
{"status":"SUCCESS","httpStatus":200,"message":"Assets found.
....}
number of assets:69
```

**Upload asset actual data** 

Let's insert an asset. Before that we need to upload the actual data to the built-in local storage.

```
bash uploadToEDC3.sh all_roles all_roles ./sample.zip
```

Output:
```
...
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.27.3
< Date: Thu, 06 Nov 2025 09:02:34 GMT
< Transfer-Encoding: chunked
< Connection: keep-alive
< x-amz-request-id: 4442587FB7D0A2F9
< ETag: "640357854d0ec6606457d9346552d3d7"
< Cache-Control: no-store, no-cache
<
{ [5 bytes data]
100   160    0     0  100   160      0    220 --:--:-- --:--:-- --:--:--   220
* Connection #0 to host ldssetupdev.ilsp.gr left intact

```

**Check that it was uploaded** 

Lets' check that data were uploaded
```
python getLocalDatasets.py
```

Output:
```
{"status":"SUCCESS","httpStatus":200,"message":"File list returned.","data":["oagl.zip","sampledata.zip","sample.zip"]}
...
```

**Create an asset** 

Now we are ready to create an asset. Keep the asset id it will be needed when we will create an offer.

```
python createAsset.py
```
Output:
```
{
  "status": "SUCCESS",
  "httpStatus": 200,
  "message": "Asset created",
  "data": {
    "@context": {
      "edc": "https://w3id.org/edc/v0.0.1/ns/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "dcatlds": "http://www.nlpli.gr/dcat-lds#",
      "dct": "http://purl.org/dc/terms/",
      "adms": "http://www.w3.org/ns/ adms#",
      "ms": "http://w3id.org/meta-share/meta-share/",
      "loc": "http://id.loc.gov/vocabulary/iso639-1/",
      "iana": "http://www.iana.org/assi gnments/media-types/application/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "@vocab": "https://w3id.org/edc/v0.0.1/ns/",
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "omtd": "http:/ /w3id.org/meta-share/omtd-share/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "euvoc_auth": "http://publications.europa.eu/resource/aut hority/",
      "schema": "https://schema.org/",
      "owl": "http://www.w3.org/2002/07/owl#",
      "lds": "https://lds.eu/",
      "skos": "http://www.w3.org/200 4/02/skos/core#",
      "dcmitype": "http://purl.org/dc/dcmitype/",
      "lexmeta": "http://w3id.org/meta-share/lexmeta#",
      "dpv": "https://w3id.org/d pv#",
      "it6": "http://data.europa.eu/it6/"
    },
    "@type": "IdResponse",
    "@id": "17597600-83cf-4120-ace1-6b3eb98ee75d",
    "createdAt": "1762420174082"
  }
}

```

**List assets again** 

Let's do a quick check that we have one more asset 
```
python getAssets.py
```
Output
```
...
```

**List publication and contract policies** 

```
python getPolicies.py
```
Output

```
Access/Publication policies
{"status":"SUCCESS","httpStatus":200,"message":"Search successful. ...}
...
Contract policies
{"status":"SUCCESS","httpStatus":200,"message":"Search successful. ...}
```

**Create offer** 

```
python createOffer.py
```

Output:

```
{
  "status": "SUCCESS",
  "httpStatus": 200,
  "message": "Contract definition created",
  "data": {
    "@context": {
      "edc": "https://w3id.org/edc/v0.0.1/ ns/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "dcatlds": "http://www.nlpli.gr/dcat-lds#",
      "dct": "http://purl.org/dc/terms/",
      "adms": "http:// www.w3.org/ns/adms#",
      "ms": "http://w3id.org/meta-share/meta-share/",
      "loc": "http://id.loc.gov/vocabulary/iso639-1/",
      "iana": "http://www .iana.org/assignments/media-types/application/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "rdfs": "http://www.w3.org/2000/0 1/rdf-schema#",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "@vocab": "https://w3id.org/edc/v0.0.1/ns/",
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "omtd": "http://w3id.org/meta-share/omtd-share/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "euvoc_auth": "http://publications.europa.e u/resource/authority/",
      "schema": "https://schema.org/",
      "owl": "http://www.w3.org/2002/07/owl#",
      "lds": "https://lds.eu/",
      "skos": "http:// www.w3.org/2004/02/skos/core#",
      "dcmitype": "http://purl.org/dc/dcmitype/",
      "lexmeta": "http://w3id.org/meta-share/lexmeta#",
      "dpv": "http s://w3id.org/dpv#",
      "it6": "http://data.europa.eu/it6/"
    },
    "@type": "IdResponse",
    "@id": "48841f36-d95b-43ef-b65f-ad46ffbec21c",
    "createdAt": "1762421698265"
  }
}
```

If you search the Connector you will find it

<img width="614" height="447" alt="image" src="https://github.com/user-attachments/assets/f866291f-648a-403b-89ba-3fec9dd2bd40" />

Let's do the same programmatically 

**Retrieve offer** 

```
python getOffer.py
```

Output:

```
{
"status": "SUCCESS",
"httpStatus": 200,
"message": "Offer doc found.",
"data": {
  "id": "48841f36-d95b-43ef-b65f-ad46ffbec21c",
  "accessPolicyId": "43285c5e-d0a2-4c8b-ac97-c1bd5aa8b857",
  "contractPolicyId": "14a7aa38-931a-47c4-b838-5f5e78abf104",
  "accessPolicyTitle": "No Restriction",
  "contractPolicyTitle": "Apache License, Version 2.0",
  "contractPolicyDescription": "Apache License\nVersion 2.0, January 2004\nhttp://www.apache.org/licenses/\n\nTERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n1. ....... License.\n",
  "contractPolicyLegalcode": "http://www.apache.org/licenses/LICENSE-2.0",
  "assetId": "17597600-83cf-4120-ace1-6b3eb98ee75d",
  "name": [
    {
      "value": "Asset1234567",
      "language": "en"
    }
  ],
  "description": [
    {
      "value": "Asset description 1234",
      "language": "en"
    }
  ],
  "policy": {
    "odrl:prohibition": {
      "odrl:action": {
        "@id": "https://dalicc.net/ns#promote"
      }
    },
    "odrl:obligation": [
      
    ],
    "@id": "NDg4NDFmMzYtZDk1Yi00M2VmLWI2NWYtYWQ0NmZmYmVjMjFj:MTc1OTc2MDAtODNjZi00MTIwLWFjZTEtNmIzZWI5OGVlNzVk:MTljZTNkODYtMTk4NC00ZTk3LWExYzMtNjk5OWY2NGMxZWQ2",
    "odrl:permission": [
      {
        "odrl:action": {
          "@id": "odrl:display"
        }
      },
      {
        "odrl:action": {
          "@id": "https://dalicc.net/ns#ChangeLicense"
        },
        "odrl:duty": {
          "odrl:action": {
            "@id": "https://dalicc.net/ns#compliantLicense"
          }
        }
      },
      {
        "odrl:action": {
          "@id": "odrl:present"
        }
      },
      {
        "odrl:action": {
          "@id": "odrl:reproduce"
        }
      },
      {
        "odrl:action": {
          "@id": "http://creativecommons.org/ns#CommercialUse"
        }
      },
      {
        "odrl:action": {
          "@id": "http://creativecommons.org/ns#DerivativeWorks"
        }
      },
      {
        "odrl:action": {
          "@id": "https://dalicc.net/ns#ModifiedWorks"
        }
      },
      {
        "odrl:action": {
          "@id": "https://dalicc.net/ns#chargeDistributionFee"
        }
      },
      {
        "odrl:action": {
          "@id": "odrl:distribute"
        },
        "odrl:duty": [
          {
            "odrl:action": {
              "@id": "http://creativecommons.org/ns#Attribution"
            }
          },
          {
            "odrl:action": {
              "@id": "http://creativecommons.org/ns#Notice"
            }
          }
        ]
      },
      {
        "odrl:action": {
          "@id": "odrl:modify"
        },
        "odrl:duty": [
          {
            "odrl:action": {
              "@id": "http://creativecommons.org/ns#Attribution"
            }
          },
          {
            "odrl:action": {
              "@id": "https://dalicc.net/ns#modificationNotice"
            }
          }
        ]
      },
      {
        "odrl:action": {
          "@id": "odrl:derive"
        },
        "odrl:duty": [
          {
            "odrl:action": {
              "@id": "https://dalicc.net/ns#modificationNotice"
            }
          },
          {
            "odrl:action": {
              "@id": "http://creativecommons.org/ns#Attribution"
            }
          }
        ]
      }
    ],
    "@type": "odrl:Offer"
  },
  "lrType": "Corpus",
  "mediaType": [
    "Text"
  ],
  "modelFunction": null,
  "keyword": [
    {
      "value": "keyword1",
      "language": "en"
    },
    {
      "value": "keyword2",
      "language": "en"
    },
    {
      "value": "keyword3",
      "language": "en"
    }
  ],
  "msLanguage": [
    {
      "languageCode": {
        "@id": "http://w3id.org/meta-share/bcp47/language_el"
      },
      "languageTag": "el"
    }
  ],
  "dctLanguage": [
    "Greek"
  ],
  "open": true,
  "createdAt": "1762421698265",
  "deletedAt": null,
  "deleted": false,
  "payAmount": 0.0,
  "sourceConnector": "Company C",
  "published": true
}
}
```

## Act as an LDS consumer

**Get the Connectors of the Data Space**
```
python getConnectors.py
```

Output:
```
{
  "status": "SUCCESS",
  "httpStatus": 200,
  "message": "Participants found",
  "data": [
    {
      "connectors": [
        {
          "id": 38,
          "name": "astros ai dev",
          "kc_id": " e2bee991-7c43-4172-8cf7-725827ad6d1b",
          "url": "https://snf-76746.ok-kno.grnetcloud.net/connector1"
        }
      ],
      "participant": "galanis AI"
    },
    {
      "connectors": [
        {
          "id": 2,
          "name": "Company B",
          "kc_id": "ed59216f-2989-495e-915d-e7ad51e93b16",
          "url": "https://ldssetupdev.ilsp.gr/connector2"
        }
      ],
      "participant": "Company B"
    },
    {
      "connectors": [
        {
          "id": 1,
          "name": "Company A",
          "kc_id": "9971988c-7f0c-41ce-8a3b-1625f4c13749",
          "url": "https:// ldssetupdev.ilsp.gr/connector1"
        }
      ],
      "participant": "Company A"
    }
  ]
}
```

**Get offers from a remote Connector**
```
python getOffersFromARemoteConnector.py
```

Output:
```
{
  "status": "SUCCESS",
  "httpStatus": 200,
  "message": "1/1 catalogues retrieved.",
  "data": {
    "merged": {
      "_shards": {
        "total": 2,
        "failed": 0,
        "skipped": 0,
        "successful": 2
      },
      "hits": {
        "total": {
          "relation": "eq",
          "value": 50
        },
        "hits": [
          {
            "_index": "offers",
            "_id": "75f5ba69-46fb-4af8-8379-94b897610c21",
            "_score": null,
            "matched_queries": [
              "Match all"
            ],
            "_source": {
              "id": "75f5ba69-46fb-4af8-8379-94b897610c21",
              "accessPolicyId": "4278bb8d-b17b-401e-a266-090538c9505f",
              "contractPolicyId": "a9d7864b-5428-4e23-b69f-a9a7e4f39c97",
              "contractPolicyTitle": "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International",
              "contractPolicyDescription": "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International\n\n Creative Commons Corporation (“Creative Commons”) is not a law firm and does not provide legal services or legal advice. Distribution of Creative Commons public licenses does not create a lawyer-client or other relationship. Creative Commons makes its licenses and related information available on an “as-is” basis. Creative Commons gives no warranties regarding its licenses, any material licensed under their terms and conditions, or any related information. Creative Commons disclaims all liability for damages resulting from their use to the fullest extent possible.\n\nUsing Creative Commons Public Licenses\n\nCreative Commons public licenses provide a standard set of terms and conditions that creators and other rights holders may use to share original works of authorship and other material subject to copyright and certain other rights specified in the public license below. The following considerations are for informational purposes only, are not exhaustive, and do not form part of our licenses.\n\nConsiderations for licensors: Our public licenses are intended for use by those authorized to give the public permission to use material in ways otherwise restricted by copyright and certain other rights. Our licenses are irrevocable. Licensors should read and understand the terms and conditions of the license they choose before applying it. Licensors should also secure all rights necessary before applying our licenses so that the public can reuse the material as expected. Licensors should clearly mark any material not subject to the license. This includes other CC-licensed material, or material used under an exception or limitation to copyright. More considerations for licensors.\n\nConsiderations for the public: By using one of our public licenses, a licensor grants the public permission to use the licensed material under specified terms and conditions. If the licensor’s permission is not necessary for any reason–for example, because of any applicable exception or limitation to copyright–then that use is not regulated by the license. Our licenses grant only permissions under copyright and certain other rights that a licensor has authority to grant. Use of the licensed material may still be restricted for other reasons, including because others have copyright or other rights in the material. A licensor may make special requests, such as asking that all changes be marked or described. Although not required by our licenses, you are encouraged to respect those requests where reasonable. More considerations for the public.\n\nCreative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License\n\nBy exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.\n\nSection 1 – Definitions.\n\n     a.\tAdapted Material means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.\n\n     b.\tAdapter's License means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.\n\n     c.\tBY-NC-SA Compatible License means a license listed at creativecommons.org/compatiblelicenses, approved by Creative Commons as essentially the equivalent of this Public License.\n\n     d.\tCopyright and Similar Rights means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.\n\n     e.\tEffective Technological Measures means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.\n\n     f.\tExceptions and Limitations means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.\n\n     g.\tLicense Elements means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution, NonCommercial, and ShareAlike.\n\n     h.\tLicensed Material means the artistic or literary work, database, or other material to which the Licensor applied this Public License.\n\n     i.\tLicensed Rights means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.\n\n     j.\tLicensor means the individual(s) or entity(ies) granting rights under this Public License.\n\n     k.\tNonCommercial means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.\n\n     l.\tShare means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.\n\n     m.\tSui Generis Database Rights means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.\n\n     n.\tYou means the individual or entity exercising the Licensed Rights under this Public License. Your has a corresponding meaning.\n\nSection 2 – Scope.\n\n     a.\tLicense grant.\n\n          1. Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n\n               A. reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and\n\n               B. produce, reproduce, and Share Adapted Material for NonCommercial purposes only.\n\n          2. Exceptions and Limitations. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.\n\n          3. Term. The term of this Public License is specified in Section 6(a).\n\n          4. Media and formats; technical modifications allowed. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.\n\n          5. Downstream recipients.\n\n               A. Offer from the Licensor – Licensed Material. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.\n\n               B. Additional offer from the Licensor – Adapted Material. Every recipient of Adapted Material from You automatically receives an offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.\n\n               C. No downstream restrictions. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.\n\n          6. No endorsement. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).\n\n     b.\tOther rights.\n\n          1. Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.\n\n          2. Patent and trademark rights are not licensed under this Public License.\n\n          3. To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.\n\nSection 3 – License Conditions.\n\nYour exercise of the Licensed Rights is expressly made subject to the following conditions.\n\n     a.\tAttribution.\n\n          1. If You Share the Licensed Material (including in modified form), You must:\n\n               A. retain the following if it is supplied by the Licensor with the Licensed Material:\n\n                    i.\tidentification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);\n\n                    ii.\ta copyright notice;\n\n                    iii. a notice that refers to this Public License;\n\n                    iv.\ta notice that refers to the disclaimer of warranties;\n\n                    v.\ta URI or hyperlink to the Licensed Material to the extent reasonably practicable;\n\n               B. indicate if You modified the Licensed Material and retain an indication of any previous modifications; and\n\n               C. indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.\n\n          2. You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.\n\n          3. If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.\n\n     b.\tShareAlike.In addition to the conditions in Section 3(a), if You Share Adapted Material You produce, the following conditions also apply.\n\n          1. The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.\n\n          2. You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.\n\n          3. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.\n\nSection 4 – Sui Generis Database Rights.\n\nWhere the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:\n\n     a.\tfor the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only;\n\n     b.\tif You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section 3(b); and\n\n     c.\tYou must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.\nFor the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n\nSection 5 – Disclaimer of Warranties and Limitation of Liability.\n\n     a.\tUnless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.\n\n     b.\tTo the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.\n\n     c.\tThe disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.\n\nSection 6 – Term and Termination.\n\n     a.\tThis Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.\n\n     b.\tWhere Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:\n\n          1.\tautomatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or\n\n          2.\tupon express reinstatement by the Licensor.\n\n     For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.\n\n     c.\tFor the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.\n\n     d.\tSections 1, 5, 6, 7, and 8 survive termination of this Public License.\n\nSection 7 – Other Terms and Conditions.\n\n     a.\tThe Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.\n\n     b.\tAny arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.\n\nSection 8 – Interpretation.\n\n     a.\tFor the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.\n\n     b.\tTo the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.\n\n     c.\tNo term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.\n\n     d.\tNothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.\n\nCreative Commons is not a party to its public licenses. Notwithstanding, Creative Commons may elect to apply one of its public licenses to material it publishes and in those instances will be considered the “Licensor.” Except for the limited purpose of indicating that material is shared under a Creative Commons public license or as otherwise permitted by the Creative Commons policies published at creativecommons.org/policies, Creative Commons does not authorize the use of the trademark “Creative Commons” or any other trademark or logo of Creative Commons without its prior written consent including, without limitation, in connection with any unauthorized modifications to any of its public licenses or any other arrangements, understandings, or agreements concerning use of licensed material. For the avoidance of doubt, this paragraph does not form part of the public licenses.\n\nCreative Commons may be contacted at creativecommons.org.\n",
              "contractPolicyLegalcode": "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
              "assetId": "e6baa89f-2e40-44aa-baa6-52f748cf1dc8",
              "name": [
                {
                  "value": "ABSITA dataset",
                  "language": "en"
                }
              ],
              "description": [
                {
                  "value": "The ABSITA dataset contains 4,121 reviews written in Italian and collected from the website booking.com. Reviews are annotated according to seven aspects: pulizia (cleanliness), comfort, servizi (amenities), staff, qualita-prezzo (value), wifi (wireless Internet connection) and posizione (location). For each aspect, the polarity (positive, negative) of its mention has been annotated. The positive and negative polarities are annotated independently, thus for each aspect four sentiment classes are possible: positive (positive=1, negative=0), negative (positive=0, negative=1), neutral (positive=0, negative=0), mixed (positive=1, negative=1).The dataset has been created and used in the context of the ABSITA task (http://sag.art.uniroma2.it/absita/), organised as part of EVALITA 2018 (http://www.evalita.it/2018).",
                  "language": "en"
                }
              ],
              "policy": {
                "odrl:prohibition": [
                  {
                    "odrl:action": {
                      "@id": "http://creativecommons.org/ns#CommercialUse"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "https://dalicc.net/ns#ChangeLicense"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "https://dalicc.net/ns#promote"
                    }
                  }
                ],
                "odrl:obligation": {
                  "odrl:action": {
                    "@id": "http://creativecommons.org/ns#ShareAlike"
                  }
                },
                "@type": "odrl:Offer",
                "@id": "NzVmNWJhNjktNDZmYi00YWY4LTgzNzktOTRiODk3NjEwYzIx:ZTZiYWE4OWYtMmU0MC00NGFhLWJhYTYtNTJmNzQ4Y2YxZGM4:MDAzODNjMmYtNDI3OS00ZDJlLWExMjUtMmM1NDRhZjM0NTJm",
                "odrl:permission": [
                  {
                    "odrl:action": {
                      "@id": "https://dalicc.net/ns#ModifiedWorks"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "odrl:derive"
                    },
                    "odrl:duty": [
                      {
                        "odrl:action": {
                          "@id": "http://creativecommons.org/ns#Attribution"
                        }
                      },
                      {
                        "odrl:action": {
                          "@id": "http://creativecommons.org/ns#Notice"
                        }
                      },
                      {
                        "odrl:action": {
                          "@id": "https://dalicc.net/ns#modificationNotice"
                        }
                      }
                    ]
                  },
                  {
                    "odrl:action": {
                      "@id": "http://creativecommons.org/ns#DerivativeWorks"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "odrl:reproduce"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "odrl:distribute"
                    },
                    "odrl:duty": [
                      {
                        "odrl:action": {
                          "@id": "http://creativecommons.org/ns#Attribution"
                        }
                      },
                      {
                        "odrl:action": {
                          "@id": "http://creativecommons.org/ns#Notice"
                        }
                      }
                    ]
                  },
                  {
                    "odrl:action": {
                      "@id": "odrl:display"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "odrl:present"
                    }
                  },
                  {
                    "odrl:action": {
                      "@id": "odrl:modify"
                    },
                    "odrl:duty": [
                      {
                        "odrl:action": {
                          "@id": "http://creativecommons.org/ns#Notice"
                        }
                      },
                      {
                        "odrl:action": {
                          "@id": "https://dalicc.net/ns#modificationNotice"
                        }
                      },
                      {
                        "odrl:action": {
                          "@id": "http://creativecommons.org/ns#Attribution"
                        }
                      }
                    ]
                  }
                ]
              },
              "lrType": "Corpus",
              "mediaType": [
                "Text"
              ],
              "keyword": [
                {
                  "value": "reviews",
                  "language": "en"
                },
                {
                  "value": "Italian language",
                  "language": "en"
                },
                {
                  "value": "aspect term",
                  "language": "en"
                },
                {
                  "value": "aspect-based sentiment analysis",
                  "language": "en"
                }
              ],
              "msLanguage": [
                {
                  "languageTag": "it",
                  "languageCode": {
                    "@id": "http://w3id.org/meta-share/bcp47/language_it"
                  }
                }
              ],
              "dctLanguage": [
                "Italian"
              ],
              "open": true,
              "createdAt": "1751976335394",
              "payAmount": 0.0,
              "sourceConnector": "Company A"
            },
            "sort": [
              "absita dataset"
            ]
          }
        ],
        "max_score": null
      },
      "took": 10,
      "timed_out": false,
      "aggregations": {
        "filter_open": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "true",
              "doc_count": 50
            }
          ]
        },
        "filter_modelFunction": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            
          ]
        },
        "filter_lrType": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "Corpus",
              "doc_count": 50
            }
          ]
        },
        "filter_keyword": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "dependency parsing",
              "doc_count": 2
            },
            {
              "key": "meme",
              "doc_count": 4
            },
            {
              "key": "speech corpus",
              "doc_count": 1
            },
            {
              "key": "part of speech",
              "doc_count": 1
            },
            {
              "key": "entity linking",
              "doc_count": 1
            },
            {
              "key": "electromagnetic articulograph",
              "doc_count": 1
            },
            {
              "key": "speech act",
              "doc_count": 1
            },
            {
              "key": "newspaper headlines",
              "doc_count": 1
            },
            {
              "key": "manually annotated corpus",
              "doc_count": 1
            },
            {
              "key": "personal diaries",
              "doc_count": 1
            },
            {
              "key": "parsing",
              "doc_count": 2
            },
            {
              "key": "audio dataset",
              "doc_count": 2
            },
            {
              "key": "automatic dating",
              "doc_count": 1
            },
            {
              "key": "audio corpus",
              "doc_count": 2
            },
            {
              "key": "speech recognition",
              "doc_count": 4
            },
            {
              "key": "diachrony",
              "doc_count": 2
            },
            {
              "key": "events",
              "doc_count": 2
            },
            {
              "key": "pos-tagged text",
              "doc_count": 1
            },
            {
              "key": "laws",
              "doc_count": 1
            },
            {
              "key": "subjectivity",
              "doc_count": 2
            },
            {
              "key": "Conversational agents",
              "doc_count": 1
            },
            {
              "key": "synonyms",
              "doc_count": 1
            },
            {
              "key": "style transfer",
              "doc_count": 1
            },
            {
              "key": "phone recognition",
              "doc_count": 1
            },
            {
              "key": "YouTube",
              "doc_count": 1
            },
            {
              "key": "temporal expressions",
              "doc_count": 1
            },
            {
              "key": "semantic change",
              "doc_count": 1
            },
            {
              "key": "faqs",
              "doc_count": 1
            },
            {
              "key": "information extraction",
              "doc_count": 2
            },
            {
              "key": "illocutionary force",
              "doc_count": 1
            },
            {
              "key": "news headlines",
              "doc_count": 1
            },
            {
              "key": "De Gasperi",
              "doc_count": 1
            },
            {
              "key": "temporal relations",
              "doc_count": 1
            },
            {
              "key": "style",
              "doc_count": 1
            },
            {
              "key": "speech transcripts",
              "doc_count": 1
            },
            {
              "key": "lemmatization",
              "doc_count": 1
            },
            {
              "key": "word sense",
              "doc_count": 2
            },
            {
              "key": "events clustering",
              "doc_count": 4
            },
            {
              "key": "Spoken language understanding",
              "doc_count": 1
            },
            {
              "key": "gender",
              "doc_count": 2
            },
            {
              "key": "annotated corpus",
              "doc_count": 1
            },
            {
              "key": "coreference resolution",
              "doc_count": 2
            },
            {
              "key": "automatic speech recognition",
              "doc_count": 2
            },
            {
              "key": "irony",
              "doc_count": 3
            },
            {
              "key": "figurative language",
              "doc_count": 1
            },
            {
              "key": "multilingual corpus",
              "doc_count": 1
            },
            {
              "key": "Italian language",
              "doc_count": 23
            },
            {
              "key": "prerequisite relations",
              "doc_count": 1
            },
            {
              "key": "social media language",
              "doc_count": 11
            },
            {
              "key": "aspect term",
              "doc_count": 2
            },
            {
              "key": "word sense disambiguation",
              "doc_count": 1
            },
            {
              "key": "event factuality",
              "doc_count": 1
            },
            {
              "key": "wikipedia",
              "doc_count": 2
            },
            {
              "key": "phonetic transcription",
              "doc_count": 1
            },
            {
              "key": "multilingual",
              "doc_count": 1
            },
            {
              "key": "anaphora resolution",
              "doc_count": 1
            },
            {
              "key": "question answering",
              "doc_count": 1
            },
            {
              "key": "named entitity corpus",
              "doc_count": 1
            },
            {
              "key": "natural language generation",
              "doc_count": 1
            },
            {
              "key": "transcriptions",
              "doc_count": 3
            },
            {
              "key": "Prerequisite Relation Learning",
              "doc_count": 1
            },
            {
              "key": "hate speech",
              "doc_count": 6
            },
            {
              "key": "lexical substitution",
              "doc_count": 1
            },
            {
              "key": "factuality",
              "doc_count": 2
            },
            {
              "key": "speech",
              "doc_count": 2
            },
            {
              "key": "Contextual stance detection",
              "doc_count": 4
            },
            {
              "key": "counterfactual",
              "doc_count": 1
            },
            {
              "key": "aggressiveness detection",
              "doc_count": 1
            },
            {
              "key": "misogyny detection",
              "doc_count": 2
            },
            {
              "key": "sarcasm",
              "doc_count": 1
            },
            {
              "key": "nominal utterance",
              "doc_count": 1
            },
            {
              "key": "coreference",
              "doc_count": 2
            },
            {
              "key": "Audio",
              "doc_count": 1
            },
            {
              "key": "domain-specific corpora",
              "doc_count": 1
            },
            {
              "key": "spoken language",
              "doc_count": 1
            },
            {
              "key": "emoji",
              "doc_count": 1
            },
            {
              "key": "clinical cases",
              "doc_count": 1
            },
            {
              "key": "customer review",
              "doc_count": 1
            },
            {
              "key": "Serbian",
              "doc_count": 1
            },
            {
              "key": "historical",
              "doc_count": 1
            },
            {
              "key": "corpus",
              "doc_count": 1
            },
            {
              "key": "dialogue system",
              "doc_count": 1
            },
            {
              "key": "part of speech tagging",
              "doc_count": 2
            },
            {
              "key": "tweets",
              "doc_count": 13
            },
            {
              "key": "news texts",
              "doc_count": 1
            },
            {
              "key": "Phone Recognition",
              "doc_count": 1
            },
            {
              "key": "reviews",
              "doc_count": 1
            },
            {
              "key": "noises",
              "doc_count": 1
            },
            {
              "key": "entity mentions",
              "doc_count": 1
            },
            {
              "key": "unintended bias",
              "doc_count": 1
            },
            {
              "key": "image",
              "doc_count": 4
            },
            {
              "key": "stereotypes",
              "doc_count": 1
            },
            {
              "key": "children writing",
              "doc_count": 1
            },
            {
              "key": "lexical semantics",
              "doc_count": 1
            },
            {
              "key": "text corpus",
              "doc_count": 1
            },
            {
              "key": "sentiment analysis",
              "doc_count": 6
            },
            {
              "key": "lexical change",
              "doc_count": 1
            },
            {
              "key": "question dialogs",
              "doc_count": 1
            },
            {
              "key": "Speech dataset",
              "doc_count": 1
            },
            {
              "key": "sentence acceptability",
              "doc_count": 1
            },
            {
              "key": "author profiling",
              "doc_count": 2
            },
            {
              "key": "Speech recognition",
              "doc_count": 1
            },
            {
              "key": "constituency parsing",
              "doc_count": 1
            },
            {
              "key": "summarization",
              "doc_count": 1
            },
            {
              "key": "Italian",
              "doc_count": 2
            },
            {
              "key": "Audio processing",
              "doc_count": 1
            },
            {
              "key": "sentiment polarity",
              "doc_count": 2
            },
            {
              "key": "age detection",
              "doc_count": 1
            },
            {
              "key": "language of children",
              "doc_count": 1
            },
            {
              "key": "deep learning",
              "doc_count": 1
            },
            {
              "key": "aspect-based sentiment analysis",
              "doc_count": 2
            },
            {
              "key": "dialogue",
              "doc_count": 1
            },
            {
              "key": "dating",
              "doc_count": 1
            },
            {
              "key": "social media",
              "doc_count": 4
            },
            {
              "key": "fairness",
              "doc_count": 1
            },
            {
              "key": "news",
              "doc_count": 4
            },
            {
              "key": "temporal information",
              "doc_count": 3
            },
            {
              "key": "textual entailment",
              "doc_count": 1
            },
            {
              "key": "certainty",
              "doc_count": 1
            },
            {
              "key": "forum",
              "doc_count": 1
            },
            {
              "key": "facebook comments",
              "doc_count": 2
            },
            {
              "key": "English",
              "doc_count": 1
            },
            {
              "key": "temporal processing",
              "doc_count": 1
            },
            {
              "key": "clinical entities",
              "doc_count": 1
            },
            {
              "key": "sentence complexity",
              "doc_count": 1
            },
            {
              "key": "syntax",
              "doc_count": 2
            },
            {
              "key": "stance",
              "doc_count": 4
            },
            {
              "key": "concept relations",
              "doc_count": 1
            }
          ]
        },
        "filter_contractPolicyLegalcode": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "https://creativecommons.org/licenses/by/4.0/legalcode",
              "doc_count": 2
            },
            {
              "key": "http://www.apache.org/licenses/LICENSE-2.0",
              "doc_count": 6
            },
            {
              "key": "https://creativecommons.org/publicdomain/zero/1.0/legalcode",
              "doc_count": 1
            },
            {
              "key": "https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode",
              "doc_count": 5
            },
            {
              "key": "https://creativecommons.org/licenses/by-nc/4.0/legalcode",
              "doc_count": 1
            },
            {
              "key": "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
              "doc_count": 35
            }
          ]
        },
        "filter_dctLanguage": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "german",
              "doc_count": 1
            },
            {
              "key": "catalan",
              "doc_count": 1
            },
            {
              "key": "spanish",
              "doc_count": 2
            },
            {
              "key": "no linguistic content",
              "doc_count": 1
            },
            {
              "key": "euvoc_auth:language/ast",
              "doc_count": 2
            },
            {
              "key": "english",
              "doc_count": 3
            },
            {
              "key": "portuguese",
              "doc_count": 1
            },
            {
              "key": "basque",
              "doc_count": 2
            },
            {
              "key": "italian",
              "doc_count": 41
            },
            {
              "key": "polish",
              "doc_count": 1
            },
            {
              "key": "galician",
              "doc_count": 1
            },
            {
              "key": "french",
              "doc_count": 2
            },
            {
              "key": "serbian",
              "doc_count": 3
            }
          ]
        },
        "filter_mediaType": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "Text",
              "doc_count": 48
            },
            {
              "key": "Numerical text",
              "doc_count": 4
            },
            {
              "key": "Image",
              "doc_count": 4
            },
            {
              "key": "Audio",
              "doc_count": 8
            }
          ]
        },
        "filter_sourceConnector": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "Company A",
              "doc_count": 50
            }
          ]
        }
      }
    }
  }
}
```

**Negotiate an offer**

```
python startNegotation.py
```

Output:
```
{"status":"FAILURE","httpStatus":302,"message":"This dataset has already been successfully negotiated for."}

```

