# Deploying JupyterHub

JupyterHub gives each of your students access to their own
computational environment. Each student will have their own account with their own storage and workspaces so they can interact with the course material. JupyterHub has made great improvements to scalability and reliability in recent years, and has adopted modern-day cloud deployment technology such as Kubernetes. This section
covers how to set up a JupyterHub that runs the environment needed for
Data 8.

## What distribution of JupyterHub should I use?

JupyterHub has a few "distributions" that make it easy to set up on a particular
kind of cloud infrastructure. Which one you choose will depend on your use case.
This section provides some information to help you decide.

There are two recommended methods for running a JupyterHub for your course: on a single VM or using Kubernetes clusters.
Which one you choose depends on the size and computational demands of the course.
To run the code in Data 8, students do not need high-powered environments.

Once you've followed either of the sections below, you should have a JupyterHub available at a
public address. The next section of this guide will focus on customizing the
environment that this JupyterHub serves in order to work with the Data 8
course materials.

### Deploy JupyterHub on a single VM ( <= 50 students)

For classes with 50 or fewer students we recommend
[**The Littlest JupyterHub**](https://the-littlest-jupyterhub.readthedocs.io/en/latest/), which deploys JupyterHub on a single virtual machine (VM). To set up The Littlest JupyterHub, follow the [installation guide](https://the-littlest-jupyterhub.readthedocs.io/en/latest/install/index.html) specific to the cloud provider you are using to deploy a JupyterHub with a publicly-accessible IP address. 

### Deploy JupyterHub on Kubernetes ( > 50 students)

For classes with more than 50 students we recommend the
[**Zero to JupyterHub for Kubernetes**](https://zero-to-jupyterhub.readthedocs.io/en/latest/) guide.
This method uses an open-source technology called [Kubernetes](https://kubernetes.io/)
to manage resources in the cloud. It is more complex, but much more scalable than
running JupyterHub on a single VM. This is what Data 8 uses at Berkeley.
Kubernetes are rapidly gaining popularity, and are generally easily-deployable
on all of the major cloud providers.

To set up JupyterHub on Kubernetes, follow the section of
Zero to JupyterHub that is relevant to the cloud
provider you are using. You will need to complete the following steps (which are linked
in the Z2JH guide, and are aslo listed below for clarity):

* [Initialize Kubernetes on your cloud provider](https://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
  so that we can run kubernetes to set up JupyterHub.
* [Set up Helm](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html), a way to quickly install applications (like JupyterHub) using Kubernetes.
* [Install JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-jupyterhub.html),
  which gives us a fully-functional (though bare-bones) JupyterHub installation!


## What kind of hardware should I use?

One of the first things you will need to do when setting up JupyterHub is to choose the kind
of machines on which you will run the course infrastructure. For the Littlest JupyterHub there are a lot of choices to be made. You will need to decide what kinds of compute, storage, and memory usage requirements you anticipate. For Kubernetes there is an added dimension of clusters to consider when provisioning multiple nodes. Do you want fewer machines with a lot of RAM? Do you want machines with really fast CPUs? For
example, here is a list of [all google cloud machine types](https://cloud.google.com/compute/docs/machine-types)
which you could pick from.

There is no single correct answer to what kind of machines you need for your class. However,
we have found that RAM is often the biggest bottleneck for a course like Data 8. With Kubernetes, we recommend
choosing machines which have a larger amount of RAM (and using fewer of them in the course, since
each machine will be able to accommodate more students).


<!--- Link Atharva JH guide when published -->
## How much will this cost?

There are many factors that go into assessing how much it will cost to deploy
Data 8 for your course. The biggest of these are CPU and RAM that each student
will need to have available. For details on how choices of hardware using Kubernetes affect the cost of the
deployment, we recommend checking out the [Zero to JupyterHub deployment costs guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/cost.html).


<!--- Remove when rest of guide includes TLJH -->
## A note on the rest of this guide

Note that while we have shown two options for deploying JupyterHub above,
the rest of this guide will focus on **deploying JupyterHub with Kubernetes**.
This is because running a JupyterHub on Kubernetes is more complex,
and warrants more guidance. However, if you are deploying a JupyterHub on a single VM
with The Littlest JupyterHub, you can follow along to determine the environment
needed to run your course.

## Next step
Now that we have a running JupyterHub, the next step is
to [customize your JupyterHub environment](customize_hub_environment).

```python

```
