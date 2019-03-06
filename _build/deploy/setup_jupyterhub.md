---
redirect_from:
  - "deploy/setup-jupyterhub"
title: 'Deploy your JupyterHub'
prev_page:
  url: /deploy/README
  title: 'Deploying Data 8'
next_page:
  url: /deploy/customize_hub_environment
  title: 'Customize the JupyterHub environment for Data 8'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Deploying JupyterHub

JupyterHub gives each of your students access to their own
computational environment. They'll have their own storage and their
own workspaces so they can interact with course material. This section
covers how to set up a JupyterHub that runs the environment needed for
Data 8.

## Deploying JupyterHub in the cloud

There are two recommended methods for running a JupyterHub for your course.
Which one you choose depends on the size and computational demands for the course.
To run the code in Data 8, students do not need high-powered environments.

Once you've either of the sections below, you should have a JupyterHub available at a
public address. The remainder of this guide will focus on customizing the
environment that this JupyterHub serves in order to work with the Data 8
course materials.

### Deploy JupyterHub on a single VM (<= 50 students)

For courses of 50 or less students we recommend
[*The Littlest JupyterHub**](https://the-littlest-jupyterhub.readthedocs.io/en/latest/),
a short guide for deploying JupyterHub on a virtual machine (VM).
Follow the instructions on the link above to deploy a JupyterHub with a publicly-accessible
IP address.

### Deploy JupyterHub on Kubernetes (> 50 students)

For courses of more than 50 students we recommend the
[**Zero to JupyterHub for Kubernetes**](https://zero-to-jupyterhub.readthedocs.io/en/latest/) guide.
This uses open-source technology called [Kubernetes](https://kubernetes.io/)
managing resources in the cloud. It is more complex, but much more scalable than
running JupyterHub on a single VM. This is what Data 8 uses at Berkeley.
Kubernetes is rapidly gaining popularity, and should soon be easily-deployable
on all of the major cloud providers.

To set up JupyterHub on Kubernetes, follow the section of
Zero to JupyterHub that is relevant to the cloud
provider you're using. You'll need to complete the following steps (which are linked
in the Z2JH guide, but listed below for clarity):

* [Initialize Kubernetes on your cloud provider](https://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
  so that we can run kubernetes to set up JupyterHub.
* [Set up Helm](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html), a way to quickly install applications (like JupyterHub) using Kubernetes.
* [Install JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-jupyterhub.html),
  which gives us a fully-functional (though bare-bones) JupyterHub installation!


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


## How much will this cost?

There are many factors that go into assessing how much it will cost to deploy
Data 8 for your course. The biggest of these are CPU and RAM that each student
has available.  For details on how choices of hardware affect the cost of the
deployment, we recommend checking out the [Zero to JupyterHub deployment costs guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/cost.html).


## A note on the rest of this guide

Note that while we're shown two options for deploying JupyterHub above,
the rest of this guide will focus on **Deploying JupyterHub with Kubernetes**.
This is because running a JupyterHub on Kubernetes is more complex,
and warrants more guidance. However, if you are deploying a JupyterHub on a single VM
with "The Littlest JupyterHub", you can follow along to determine the environment
needed to run your course.

## Next step
Now that we have a running JupyterHub, the next step is
to [customize your JupyterHub environment](customize_hub_environment).
