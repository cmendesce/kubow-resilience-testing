#!/usr/bin/env bash
set -e

SERVICE_ACCOUNT=admin-user

SECRET=$(kubectl get serviceaccount ${SERVICE_ACCOUNT} -o json | jq -Mr '.secrets[].name | select(contains("token"))')

TOKEN=$(kubectl get secret ${SECRET} -o json | jq -Mr '.data.token' | base64 -d)

curl localhost:8081/api/v1/namespaces/default/pods --header "Authorization: Bearer $TOKEN"