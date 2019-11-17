#!/usr/bin/env bash
set -e


kubectl apply -f namespaces.yaml
kubectl apply -f admin-user.yaml

kubectl apply -f locust/
kubectl apply -f kube-znn/
kubectl apply -f metrics-server/
kubectl apply -f prometheus/
kubectl apply -f kube-state-metrics/
kubectl apply -f ambassador/

kubectl apply -f kubow/

# kubectl delete -f kube-znn/
# kubectl delete -f metrics-server/
# kubectl delete -f prometheus/
# kubectl delete -f kubow/