# Data 8 at Berkeley

Creating a data science course from first-principles requires considerable
advances in the technology available to instructors. In creating Data 8, the
development team has worked closely with members of the open-source community,
and has contributed to or spun off many open source projects. The goal driving
development of technology for Data 8 is to *develop an open platform of which
Berkeley happens to be the first user.*

Managing a class of 1400 students doing non-trivial computational work is a big technical challenge. This page details many of
the technical guiding principles and solutions that the Data 8 team has adhered to and implemented.

## Open source strategy

A core goal of the Data 8 project is to use an entirely open stack to use in our course. As such, most of these components are freely available to the educational community, and we welcome
others to adopt these tools for their own uses and become contributors to
these projects over time. We
chose this approach for a few main reasons:

* **Using an open stack gives us freedom to deploy Data 8 anywhere.** By running on entirely open
  tools we can ensure that Data 8 is not tied to a specific proprietary tool, or a single
  vendor's offering. We believe that this flexibility and choice benefits us (even if it
  occasionally means passing on vendor-specific options that would save us time in the short-term).
* **Using an open stack means we don't have to re-invent the wheel.** One of the benefits
  of using open tools is that many useful tools *already exist* and we would rather piggy-back
  off of the work of others than re-invent the wheel ourselves. For this reason, we prefer to
  find open source tools and leverage them in data 8, rather than start from scratch.
* **Using an open stack lets us contribute back.** Finally, Data 8 also uses its resources to
  *contribute back* to the open source projects that we utilize. For example, many improvements
  to JupyterHub, Jupyter Notebooks, and JupyterLab have been made by the team working on
  Data 8. As many of these projects are already developed by universities and other organizations
  dedicated to the public good, this is an opportunity for us to give back to the community
  that makes courses like data 8 possible.

## Desired Workflow

The instructor first creates a piece of course material they want students to be able to use.
They push the latest version of this material to GitHub, then send students a link that
they can click in order to interact with the material.

The student then clicks on the link, which triggers the following actions:

* The DataHub authenticates the user (either asking them to sign in, or discovering that their local computer already has credentials to proceed).
* The DataHub creates and starts a Jupyter instance for the user (or directs the user to a pre-existing environment from a previous session)
* The student's persistent storage volume is linked to their Jupyter instance
* The DataHub clones or pulls the content specified by the link into student’s instance
* The student is then directed to a live notebook instance in the browser. It contains the content specified in the link and can be immediately interacted with.
* While doing the assignment, the student is able to check their answers against public autograder tests.
* After completing the assignment, the student submits their notebook to an autograder for grading. 

## Technical Priorities in Data 8

* **Standardize student environments** - Anyone who has taught a bootcamp knows the pain involved in getting a room of 20 students with the same functioning environment. Data 8 has nearly two orders of magnitude more students. For an introduction class, requiring students to set up their own environment is a huge distraction and dis-equalizer.
* **Use the cloud** - By utilizing cloud resources, the course material is available to all students regardless of the hardware available to them.
* **Be cloud agnostic** - There are many options for interacting with the cloud, but most are bespoke interfaces that pair with a *product* you eventually pay for (e.g. https://aws.amazon.com/education/). We didn't want Data 8 to depend on a specific provider, interface, or other set of packages. We want to give students and instructors the ability to work on whatever platform they like. As such, we chose tools that were open-source and cloud-agnostic.
* **Keep costs down** - Broader adoption of the course at Berkeley and beyond will only happen if costs are reasonably low. We shoot for a few dollars per student, per month.
* **Handle dynamic activity** - Students tend to operate in bursts of activity (e.g., during class or 30 minutes before the homework is due). We needed dynamic cloud infrastructure that could handle many patterns of activity.
* **Meet peak demand** - Moments of maximal cloud usage (e.g., during lecture) are moments when the cloud *must be functional*.
* **Do all of the above with a small team** - The Data 8 model is not scalable if it requires a dedicated team of tech-savvy staff. While some technical skills are required, we wanted most course operations to be handled by a small team of undergraduates (usually Data 8 alumni).

## Technologies Implemented in Data 8

The following is an outline of the technical pieces that go into running Data 8.
It is broken down by activity / need so that it might be most useful for others
hoping to accomplish the same goals.

### Managing cloud resources

The core technical piece of Data 8 is the **DataHub**, a server running in the cloud
that serves live computational environments for all of the students in the class.
In Data 8, *students can work entirely from the DataHub*, running in the cloud.

Managing these resources primarily utilizes the following pieces of open-source technology:

* **Managing cloud resources** - [Kubernetes](https://kubernetes.io/) is the underlying technology that manages the resources on our cloud provider. It is open-source, and is supported by most major cloud providers (it also works on your own hardware). By relying on Kubernetes, Data 8 has been able to switch cloud providers nearly each semester with minimal disruption to the class.

* **Managing user sessions** - [JupyterHub](https://github.com/jupyterhub/jupyterhub) is used to manage user sessions in the cloud. It manages user authentication and serves them an environment in which they can do their work. JupyterHub also integrates nicely with Kubernetes via the **JupyterHub Helm Chart**. To learn more about deploying JupyterHub on Kubernetes, see the [Zero to JupyterHub Guide](https://z2jh.jupyter.org)

* **Authentication** - **Canvas OAuth** is used by DataHub to handle the actual authentication process. JupyterHub supports a number of options for authentication, and because Berkeley uses Canvas as its LMS, this was the simplest way to authenticate users. Previously, DataHub used Google OAuth for authentication.

* **Managing the user's software** - We use **Docker images** created specifically for Data 8. They contain all of the software dependencies needed to run all of the course material as well as to interact with JupyterHub. JupyterHub can be configured to serve users a Docker image from the cloud, and any updates to this image will automatically propagate to new user sessions. [Here is a list of all DSEP Docker Images](https://hub.docker.com/u/berkeleydsep/).

* **User Long-term Storage** - Students need their work to persist over time, and the storage options for students depend on the cloud provider that is being used for a given semester. JupyterHub for Kubernetes can be configured to plug in to many different kinds of file systems. The authentication process will determine whether a long-term file storage system already exists for a user and, if so, will automatically mount it to a user's session when they connect.

### Administering and managing the cluster

<!--- Link admin Access page -->
* **Admin access to the DataHub** - The Data 8 team often required access to a high-level view of the DataHub, as well as access to commands that created/destroyed user sessions. This is provided by the **Admin Panel** of JupyterHub, which allows a subset of users to control operations of the DataHub resources.

<!--- Link updating JH page-->
* **Deploying and updating the DataHub** - While the DataHub is a complicated piece of technology, running it, maintaining it, and updating it should be doable by people without strong technical operations skills. Data 8 uses GitHub repositories to store all configuration scripts for the DataHub, and uses Travis Continuous Integration to automatically-deploy changes to the configuration. As a result, updating the cluster is as simple as changing a configuration file and waiting for the changes to propagate.

<!--- Update?-->
* **Scaling cloud resources** - An **autoscaler** is used to ensure that Data 8 is only requesting the cloud resources that it needs. Kubernetes makes it easy to scale up/down relatively quickly. This is configured with a script that is cloud-specific for now, but will become possible using only Kubernetes in the future.

* **Versioning and reproducibility** - It is important that we know the *exact* state of the DataHub at any moment in time, and can recreate that state in the future. We use Git and best-practices in package management (e.g., explicitly versioning all components) to ensure that the DataHub configuration can be deployed elsewhere without difficulty.

### Software used in code 
<!--- Link Otter page-->
* **Grading** - Grading in Data 8 is carried out with a service called [OKpy](https://okpy.org/), but we typically recommend using Otter Grader due to its ease of adoptability. This is a collection of scripts and services that allow students to check their work within the Jupyter Notebook. Students also submit their assignment to a centralized server for grading or to a Learning Management System.

* **Programming language** - The programming language of choice for Data 8 is Python 3. This is because Python is a generic, user-friendly, and well-designed language that is broadly useful in data science. It is the most popular language for high-level data analytics, and has a rich ecosystem of packages for interactive data analysis. Additionally, Python is also open source.

* **The SciPy staack and handling the Python environment** - On top of the Python language is a thriving community of libraries and tools for scientific
computing. The `datascience` package utilizes functions in NumPy (a tool for linear algebra), SciPy (a set of tools for scientific tasks), Pandas (a tool for dealing with tabular data), and Matplotlib (a tool for visualization). Student environments in Python are managed with `miniconda`, a package from Anaconda that makes it easy to create user environments, as well as install / remove / update particular Python packages.

* **Jupyter Notebooks** - are a de-facto
standard across both academic research as well as industry in data science. We wanted to use notebooks both because
they were quite useful for interactive computing and as a tool for communication, but also because
they are free, usable by anybody, and developed by an open community.

