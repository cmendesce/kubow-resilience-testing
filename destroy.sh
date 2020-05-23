#!/usr/bin/env bash
set -e

kubectl delete -f locust
kubectl delete -f kube-znn
kubectl delete -f nginx-ingress
kubectl delete -f metrics-server
kubectl delete -f prometheus
kubectl delete -f kube-state-metrics
