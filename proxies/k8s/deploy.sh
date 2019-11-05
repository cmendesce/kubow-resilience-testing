#!/usr/bin/env bash
set -e

echo "deleting current configuration..."

kubectl delete -f . --ignore-not-found=true
kubectl delete configmap/k8s-envoy-config --ignore-not-found=true

kubectl delete -f ./delay --ignore-not-found=true
kubectl delete -f ./circuit-breaker --ignore-not-found=true
kubectl delete -f ./abort --ignore-not-found=true

echo "applying $1 configuration"

kubectl apply -f .
kubectl apply -f ./$1