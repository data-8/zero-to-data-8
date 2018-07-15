# Deploy Data 8 for your course

This section covers how to set up Data 8 from scratch. It gives a broad overview
of technical pieces at play, but is to-the-point in terms of setting
things up. For information about the motivations and decisions surrounding the
Data 8 class, see the other components of this guide.

## Tools you'll use

Setting up your own Data 8 course repository will require using a few pieces
of technology and skills. Here's a short list of each, and what they'll be
used for.

* [Kubernetes](https://kubernetes.io/) is used to orchestrate all of the cloud
  resources that serve user sessions.
* [JupyterHub](https://z2jh.jupyter.org) is the software that manage user
  accounts and creates interactive sessions for users.
* [Jekyll](https://jekyllrb.com/) is used to host your course content online.
  It uses the [ruby language](https://www.ruby-lang.org/en/) to create your
  site.
* [Git](https://git-scm.com/) and [GitHub](https://github.com) are used to
  host the textbook for the course, and control revisions of all course
  materials. It's also where you can host your course template online.
