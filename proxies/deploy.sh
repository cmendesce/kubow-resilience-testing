#!/usr/bin/env bash
set -e

echo ".... deleting current configuration ...."

kubectl delete -f . --ignore-not-found=true
kubectl delete -f abort/ --ignore-not-found=true
kubectl delete -f delay/ --ignore-not-found=true
kubectl delete -f normal/ --ignore-not-found=true

echo ".... applying [$1] configuration ...."

kubectl apply -f ./$1
kubectl apply -f .
