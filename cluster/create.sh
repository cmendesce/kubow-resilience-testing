#!/usr/bin/env bash
set -e

export NAME=cmendes.k8s.local
export KOPS_STATE_STORE=s3://kops-k8s-clusters
export REGION=us-east-1
export ZONES=us-east-1a

kops create cluster $NAME \
  --zones $ZONES \
  --authorization RBAC \
  --master-size t3.medium \
  --master-volume-size 10 \
  --node-size t3.small \
  --node-count 3 \
  --node-volume-size 10 \
  --yes

for f in ig-*.yaml
do
	cat $f | kops create -f - --name $NAME
done