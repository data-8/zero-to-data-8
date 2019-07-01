# Choosing where your JupyterHub will run

## Should I deploy on my hardware or in the cloud?

The first thing you'll decide is *where* your JupyterHub will run. The first
question to ask is "will I run my JupyterHub on my own hardware, or will I
run it in the cloud?" Running a JupyterHub on your own hardware is your best
option if you have some technical support for doing so. If you're working with
limited technical resources, running a JupyterHub in the cloud is usually simpler.
The rest of this guide assumes you'd like to run a JupyterHub in the cloud.

(however, note that you can still [demo the course environment locally](deploy_locally.html))

## Choosing a cloud provider and service

Cloud providers (e.g. Microsoft Azure, Google Cloud, or Digital Ocean) are where you'll
run your JupyterHub. These companies basically own really large computers, and what
you do is purchase some resources on those computers to run whatever you'd like (in this
case, a JupyterHub). However, there are often a few different kinds of offerings that
cloud providers provide, with various pros and cons.

> **An aside on using free hosted services vs. creating your own deployments**. Many cloud
  providers offer a "free" and customized notebook service for basic usage. While these are
  appealing on their surface, they provide a number of challenges down the road, such as
  getting your students used to the vendor-specific interface rather than an open-source version.
  The Jupyter Project (and the Data 8 approach) aims to maximize your choice and flexibility in
  how and where you deploy Jupyter environments on shared infrastructure, and for this reason
  we do not recommend using most fully-managed "free" services.

With that in mind, here are a few of the most-common options for choosing your cloud resources.

* **You purchase computational resources and set up yourself**. The recommmened approach. In this case, you ask the
  cloud provider for some resources, and they give you a blank slate that you can do anything
  with. This is the most-common approach to deploying JupyterHub (along with
  following this guide to do the actual set-up).

  * **Pros**: You have flexibility in customizing your JupyterHub exactly as you wish. You also
    have the ability to easily switch to other cloud providers because the setup process will
    be very similar for each.
  * **Cons**: There is more manual setup and maintenance for you to perform. Because the resources
    are a blank slate, you'll need to take the steps to set everything up.
* **You use a "push-button" deployment to deploy specific resources**. Another possibility is that
  the cloud provider has given you a single-button option to automatically deploy
  some resources on their cloud. For example, some providers let you quickly deploy a JupyterHub
  that you then customize. Others let you deploy an entirely customized distribution of JupyterHub
  that theoretically "works out of the box".

  * **Pros**: You can get to a running JupyterHub more quickly.
  * **Cons**: You have less flexibility over deploying and customizing this JupyterHub. In addition,
    you can less-easily move your infrastructure to a different cloud provider because you are
    used to a vendor-specific workflow.
* **You use a JupyterHub-like hosted service of a cloud provider**. The final option is that you
  use a fully-managed service of a cloud provider, such as the Google Collaboratory, or Microsoft
  Azure Notebooks. These often look and behave like Jupyter Notebooks, though they are often
  built on some proprietary technology from these companies. This should be your least-preferable
  option because it increases your dependence on a single cloud provider.

  * **Pros**: You can get a Jupyter-like experience extremely quickly. In addition, these services are
    often "free" (at least initially).
  * **Cons**: This greatly increases your dependence on a single cloud provider, and the interface +
    infrastructure that they provide. In addition, using a vendor-specific service often confuses
    students in the long-term because the environments are not the same as the default open-source
    software in the Jupyter ecosystem.

Ultimately, the choice of cloud infrastructure is your own, and different options will be appropriate
for different situations. Hopefully these resources help you navigate this space and understand
the benefits and pitfalls of your choices.

Once you've chosen a cloud provider, your next step is to deploy your own JupyterHub! We'll
cover how to do this in the next section.
