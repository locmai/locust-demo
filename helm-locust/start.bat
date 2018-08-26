helm del locust --purge
helm install . --name locust --set worker.replicaCount=20