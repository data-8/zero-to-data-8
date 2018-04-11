# Setting up your Kubernetes Cluster

The JupyterHub for Data 8 uses an open-source technology called Kubernetes
to manage all of the resources in the cloud. Kubernetes is rapidly gaining
popularity, and will soon be easily-deployable
on all of the major cloud providers.

This section describes how to set up a bare-bones Kubernetes cluster on
the Google Kubernetes Engine.

Many of these steps are slightly modified versions of the [Zero to JupyterHub](https://z2jh.jupyter.org) guide.

## Prepare your Google account

* **TODO: Discuss setting up the Google account / tools. Can we just link to Z2JH here?**

## Create your Cluster

Now it's time to create your cluster.

* **TODO: Can we just link to Z2JH here? Or alternatively provide a helper script.**

```
gcloud container clusters create data-8 \
    --num-nodes=3 \
    --machine-type=n1-standard-2 \
    --zone=us-central1-b \
    --cluster-version=1.8.7-gke.1
```

```
kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user={{YOUR-EMAIL-ADDRESS-HERE}}
```


```
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > install-helm.bash
bash install-helm.bash --version v2.6.2
```

```
kubectl --namespace kube-system create serviceaccount tiller
```

```
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```

### Install helm

```
helm init --service-account tiller
```

```
helm version
```

```
kubectl --namespace=kube-system patch deployment tiller-deploy --type=json --patch='[{"op": "add", "path": "/spec/template/spec/containers/0/command", "value": ["/tiller", "--listen=localhost:44134"]}]'
```


### Set up JupyterHub

```
openssl rand -hex 32
```

Add the above to the `config.yaml` file

```
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update
```

```
helm install jupyterhub/jupyterhub \
    --version=v0.6 \
    --name=data8 \
    --namespace=data8 \
    -f config.yaml
```


```
kubectl --namespace=data8 get svc
```
