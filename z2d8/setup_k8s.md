# Setting up your Kubernetes Cluster

The JupyterHub for Data 8 uses an open-source technology called
[Kubernetes](https://kubernetes.io/)
to manage all of the resources in the cloud. Kubernetes is rapidly gaining
popularity, and should soon be easily-deployable
on all of the major cloud providers.

There are a few resources out there for setting up Kubernetes on most major
cloud providers. The JupyterHub team has provided one-such resource,
called [Zero to JupyterHub](https://z2jh.jupyter.org).

## What kind of hardware should I use?

One of the first things you'll need to do when setting up Kubernetes is to choose the kind
of machines on which you'll run the course infrastructure. There are a lot of choices here -
do you want fewer machines with a lot of RAM? Do you want machines with really fast CPUs? For
example, here's a list of [all google cloud machine types](https://cloud.google.com/compute/docs/machine-types)
that you could pick from.

There is no single correct answer to what kind of machines you need for your class. However,
we've found that RAM is often the biggest bottleneck for a course like Data 8. We recommend
choosing machines that have a larger amount of RAM (and using fewer of them in the course, since
each machine will be able to fit more students on it).

## Instructions to set up Kubernetes

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

The next step is to [customize your JupyterHub environment](customize_hub_environment.md).
