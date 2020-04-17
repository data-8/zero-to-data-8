# JupyterHub Overview

This section describes the process of configuring and deploying your own Jupyterhub. It gives an overview of how to make important design decisions, such as where to deploy your hub and what Hub size is needed. 

[**JupyterHub**](https://zero-to-jupyterhub.readthedocs.io/en/latest/) is a multi-user Hub that allows students to interact with their own computing environment. It makes it easy to spawn and manage multiple instances of a Jupyter notebook.

## Why JupyterHub?

Data 8 started with 60 students in Fall 2015, and now has 1350 students as of Spring 2020. The course operates on a scale and level of complexity that required several technological improvements to our current teaching toolset. The Data 8 team worked closely with various open-source projects in order to contribute to tools that are broadly useful.

All of the course infrastructure that Data 8 uses runs on JupyterHub and Kubernetes. These
are both open source projects for managing user sessions and orchestrating computational
resources in the cloud. We decided to run our course on an open infrastructure because it gives us
the freedom to run Data 8 on any cloud provider, and lessens the likelihood of becoming
dependent on a single cloud vendor to run the course. It also allowed us to improve these tools,
allowing other organizations to deploy JupyterHub for teaching Data 8 on whatever cloud resources
they'd prefer. For example JupyterHub runs on both large, scalable cloud infrastructure like
Kubernetes, but also on much smaller-scale infrastructure without Kubernetes, such as a single machine, which gives
others more flexibility in how and where they want to run their Data 8 infrastructure.
