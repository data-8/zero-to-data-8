# Frequently Asked Questions (FAQ)

The following sections contain some frequently asked questions around deploying
Data 8 with JupyterHub. If you've got a question that isn't answered, feel free
to [open an issue on the z2d8 github repository](https://github.com/data-8/zero-to-data-8/issues).

## How can I deploy a JupyterHub on hardware that isn't listed in this guide?

These guides focus on deploying JupyterHub on large cloud providers such as
Microsoft, Google, and Amazon. However, many organizations prefer to deploy on
something other than this (e.g. their own local hardware).

You can deploy a
JupyterHub on any hardware, though it must run Kubernetes. Setting up Kubernetes
is not trivial, and so we recommend cloud providers because they simplify this
process significantly. If there's a specific provider or setup that you *think*
should be officially documented, please reach out and we can discuss!

## How can I adapt the Data 8 setup for a different course?

If you'd like to deploy a course _other_ than Data 8 (or a small delta from it),
you can use most of the same steps to do so. The JupyterHub deployment is the same,
and the Docker image we use for user sessions should fit many data science course
needs. If you'd like to adapt or modify parts of the textbook or labs, please reach
out to the Data 8 team so that we can discuss how to do this most effectively.

For a more in-depth guide on customizing a JupyterHub (e.g. to install an environment
that isn't covered by the Data 8 Docker image), see the [Zero to JupterHub](https://z2jh.jupyter.org)
guide. For a more generic jekyll-based textbook template, see the
[Textbooks with Jekyll](https://github.com/choldgraf/jupyter-book)
template repository.

## How can I contribute back to Data 8 materials?

If you feel that there are changes / improvements that should be made to
the Data 8 material, feel free to open an issue on the
[Data 8 textbook page](https://github.com/data-8/textbook). Alternatively
you are always welcome to fork the repository and make a pull-request!
