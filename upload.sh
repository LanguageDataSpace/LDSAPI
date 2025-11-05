#!/bin/bash

source .env 

username=$1
password=$2
instance=$3
storagepath=$4
file=$5
clnt=$6


echo "username:"$username
echo "password:"$password
echo "instance:"$instance

cmd="curl --location --request POST 'https://${ADDRESS}/auth/realms/${instance}/protocol/openid-connect/token' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'client_id=${clnt}' --data-urlencode 'grant_type=password' --data-urlencode 'username=$username' --data-urlencode 'password=$password'"

echo $cmd
RESULT=`eval $cmd`
echo $RESULT

echo "\n"
echo "* Recovery of the token"
TOKEN=`echo $RESULT | sed 's/.*access_token":"//g' | sed 's/".*//g'`
echo $TOKEN > token.txt

#$cat token.txt

endpoint=https://${ADDRESS}/${storagepath}/hosted/
echo $endpoint

cmd="curl -X PUT -vvvvv --header 'Content-Type:application/octet-stream'  --header 'Authorization: Bearer ${TOKEN}' -T $file $endpoint"
echo $cmd
RESULT=`eval $cmd`
echo $RESULT



