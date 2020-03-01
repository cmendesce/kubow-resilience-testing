#!/usr/bin/env bash
set -e

kubectl apply -f admin-user.yaml

kubectl apply -f locust/
kubectl apply -f kube-znn/
kubectl apply -f metrics-server/
kubectl apply -f prometheus/
kubectl apply -f kube-state-metrics/
kubectl apply -f kubow/