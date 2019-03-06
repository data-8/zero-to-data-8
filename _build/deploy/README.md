---
redirect_from:
  - "deploy/readme"
title: 'Deploying Data 8'
prev_page:
  url: /intro
  title: 'Home'
next_page:
  url: /deploy/setup_jupyterhub
  title: 'Deploy your JupyterHub'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Deploy Data 8 for your course

This section covers how to set up Data 8 from scratch. It gives a broad overview
of technical pieces at play, but is to-the-point in terms of setting
things up. For information about the motivations and decisions surrounding the
Data 8 class, see the other components of this guide.

## Tools you'll use

Setting up your own Data 8 course repository will require using a few pieces
of technology and skills. Here's a short list of each, and what they'll be
used for.


* [JupyterHub](https://z2jh.jupyter.org) is the software that manage user
  accounts and creates interactive sessions for users.
* [Git](https://git-scm.com/) and [GitHub](https://github.com) are used to
  host the textbook for the course, and control revisions of all course
  materials. It's also where you can host your course template online.
* [Kubernetes](https://kubernetes.io/) (optional, only if your course is
  > around 60 students) is used to orchestrate the cloud
  resources that serve user sessions.
