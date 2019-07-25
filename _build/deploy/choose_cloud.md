---
redirect_from:
  - "deploy/choose-cloud"
title: 'Choose where to deploy your JupyterHub'
prev_page:
  url: /deploy/README
  title: 'Deploying Data 8'
next_page:
  url: /deploy/setup_jupyterhub
  title: 'Deploy your JupyterHub'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Choosing where your JupyterHub will run

## Should I deploy on my hardware or in the cloud?

The first thing you'll decide is *where* your JupyterHub will run. The first
question to ask is "will I run my JupyterHub on my own hardware, or will I
run it in the cloud?" Running a JupyterHub in the cloud is usually simpler,
particularly if you're working with limited technical resources. Managing
infrastructure (especially in a reliable, performant way) is a lot of work,
and best-left to people who are experts at this.

Fortunately, there are an increasing number of options to use infrastructure that *other* people manage.
The trick is in deciding *how much* they manage to give yourself the right
balance of control and flexibility. We'll cover this in the following
sections.

(however, note that you can still [demo the course environment locally](deploy_locally.html))


## Choosing a cloud provider and service

Cloud providers (e.g. Microsoft Azure, Google Cloud, Amazon Web Services, or Digital Ocean) are where you'll
run your JupyterHub. These companies basically own really large computers, and what
you do is purchase some resources on those computers to run whatever you'd like (in this
case, a JupyterHub). Data 8 chooses to use cloud infrastructure and tools that are open-source
and that are not specific to any one cloud provider. For information on why Data 8
uses an open-source strategy, check out [Data 8's approach to open source](../tech/considerations.html#open-source-strategy).

However, you'll have a few different options for deploying infrastructure in the cloud, and this page
aims to disambiguate these options.

With that in mind, here are a few of the most-common options for choosing your cloud resources.

* **Use vanilla computational resources and run JupyterHub yourself**. In this case, you ask the
  cloud provider for some resources, and they give you a blank slate that you can do anything
  with. This is the most-common approach to deploying JupyterHub (and the approach that this
  guide assumes).

  * **Pros**: You have flexibility in customizing your JupyterHub exactly as you wish. You also
    have the ability to easily switch to other cloud providers because the setup process will
    be very similar for each, and the workflows that you share with your students are most-likely
    to be portable to other data science environments.
  * **Cons**: There is more manual setup and maintenance for you to perform. Because the resources
    are a blank slate, you'll need to take the steps to set everything up.
* **Use a "template" deployment to deploy a vanilla JupyterHub**. Another possibility is that
  the cloud provider has given you a single-button option to automatically deploy a JupyterHub
  that you can then customize. In this case you still need to set up the JupyterHub with the
  environment and services you want, but the initial JupyterHub creation and some degree of
  cloud resource management has been done for you.

  * **Pros**: The pros for this are similar to the "vanilla computational resources" point above, with
    the tradeoff that your JupyterHub will be faster and easier to initially deploy.
  * **Cons**: You'll be more dependent on the cloud vendor for their templatized solution
    (however, as the JupyterHub is relatively vanilla, you'll likely be able to deploy the same
    setup somewhere else with minimal extra effort). You'll also still need to maintain the JupyterHub
    over time.

* **Use a "template" deployment to deploy a more complex JupyterHub setup**. In addition to deploying
  a vanilla JupyterHub, some cloud vendors give you a "push-button" option to deploy a specific
  customization of a JupyterHub for a particular use-case (like education). These are more complex
  deployments than a "vanilla" templatized JupyterHub, and often come with integrations with
  vendor-specific services.

  * **Pros**: You can get to a running JupyterHub for your specific use-case more quickly.
  * **Cons**: You have less flexibility over deploying and customizing this JupyterHub. In addition,
    you can less-easily move your infrastructure to a different cloud provider because you are
    used to a vendor-specific workflow, especially if the deployment uses vendor-specific services.

* **Use a cloud provider's hosted notebook service**. The final option is that you
  use a fully-managed service of a cloud provider, such as the Google Collaboratory or Microsoft
  Azure Notebooks. These often look and behave like Jupyter Notebooks, though they are often
  built on some proprietary technology from these companies.

  * **Pros**: You can get a Jupyter-like experience extremely quickly. In addition, these services are
    often "free" (at least initially).
  * **Cons**: This greatly increases your dependence on a single cloud provider, and the interface +
    infrastructure that they provide. These environments are generally less-customizable and don't
    integrate as easily into services, tools, and course infrastructure that you use.
    Depending on how customized the interface is, it may not be the same as the default open-source
    software in the Jupyter ecosystem, which may confuse students. Finally, although these
    services may be free now at basic usage, they may not continue this way in the future, and
    will often ask you to pay once you need more resources (at which point you may wish you could
    switch to a different cloud provider that may be cheaper).

## Is there a particular cloud provider that you recommend?

Not really - ultimately, the choice of cloud infrastructure is your own, and different options will be appropriate
for different situations. We recommend using the following rubric to decide which cloud provider to
use: **Which provider makes it the easiest and cheapest to get a vanilla JupyterHub that
is highly customizable?** Data 8 has been run on every major cloud provider, and we intentionally
switch providers every few semesters in order to avoid depending too much on a single vendor's services.

## Where to get help?

If all of this sounds daunting to you, there are a few places that you can try to get help. Here
are a few suggestions.

* **Find a community around you who is interested in these topics**. Many universities either have
  technical support or individuals who know about these kinds of things. Try reaching out to them,
  ask if they're willing to help you deploy a JupyterHub for your course, or to help teach you
  how to do this.
* **Connect with the JupyterHub community**. Because Jupyter is an open project and community,
  it's quite friendly to interact with! There are several places where you can connect with members
  of the Jupyter community, such as [the Jupyter Community Forum](https://discourse.jupyter.org)
  or the [JupyterHub team repository](https://github.com/jupyterhub/team-compass).
* **Don't hesitate to ask**. Ultimately, deploying your own Data 8 infrastructure is likely
  a new undertaking. If you have questions, or are unsure of the best approach, don't hesitate
  to ask questions of those around you, or those in the broader Jupyter community.

Once you've chosen a cloud provider, your next step is to deploy your own JupyterHub! We'll
cover how to do this in the next section.
