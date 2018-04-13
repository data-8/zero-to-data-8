# Setting up your Kubernetes Cluster

The JupyterHub for Data 8 uses an open-source technology called
[Kubernetes](https://kubernetes.io/)
to manage all of the resources in the cloud. Kubernetes is rapidly gaining
popularity, and should soon be easily-deployable
on all of the major cloud providers.

There are a few resources out there for setting up Kubernetes on most major
cloud providers. The JupyterHub team has provided one-such resource,
called [Zero to JupyterHub](https://z2jh.jupyter.org).

Before you move on to any of the next steps in _Zero to Data 8_, you should
follow the section of Zero to JupyterHub that is relevant to the cloud
provider you're using. You'll need to complete the following steps (which are linked
in the Z2JH guide, but listed below for clarity):

* [Initialize Kubernetes on your cloud provider](https://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
  so that we can run kubernetes to set up JupyterHub.
* [Set up Helm](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html), a way to quickly install applications (like JupyterHub) using Kubernetes.
* [Install JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-jupyterhub.html),
  which gives us a fully-functional (though bare-bones) JupyterHub installation!

Once you've followed these steps, you should have a JupyterHub available at a
public address. The remainder of this guide will focus on customizing the
environment that this JupyterHub serves in order to work with the Data 8
course materials.