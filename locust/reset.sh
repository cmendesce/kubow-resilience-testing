kubectl delete -f ./locust/attacked-host-cfg.yaml
kubectl delete -f ./locust/master-dep.yaml
kubectl delete -f ./locust/slave-dep.yaml
kubectl delete -f ./locust/locustfile-cfg.yaml

kubectl apply -f ./locust