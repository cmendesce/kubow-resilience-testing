#!/usr/bin/env bash
set -e

# kubectl apply -f locust
# kubectl apply -f load-testing
kubectl apply -f kube-znn
kubectl apply -f nginxc-ingress
kubectl apply -f metrics-server
kubectl apply -f prometheus
kubectl apply -f kube-state-metrics
# kubectl apply -f pynn
