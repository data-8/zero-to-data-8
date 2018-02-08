# The Data 8 Tech Stack @ Berkeley

Creating a data science course from first-principles requires considerable
advances in the technology available to instructors. In creating Data 8, the
development team has worked closely with members of the open-source community,
and has contributed to or spun off many open source projects. The goal driving
development of technology for Data 8 is to *develop an open platform of which
Berkeley happens to be the first user.*

As such, most of these components are freely available to the educational community, and we welcome
others to adopt these tools for their own uses and become contributors to
these projects over time.

The following is an outline of the technical pieces that go into running Data 8.
It is broken down by activity / need so that it might be most useful for others
hoping to accomplish the same goals.

## Managing computational resources
* JupyterHub
* Kubernetes (platform agnostic)
* Zero-To-JupyterHub: JupyterHub + Kubernetes
* Cloud provider:
    * Currently Azure
    * Have also used Google Cloud and bare metal
* User identity via Google OAuth since Berkeley is a G Suite customer ~~CalNet identification~~
* Docker containers for user environment
* User storage
    * Manually provisioned NFS on Azure. Azure File will be a possibility soon.
    * On GCE, users each had their own disk. This was very expensive.

## Administering and managing the cluster
* Admin access: JupyterHub admin panel
* Deployments are managed with GitHub, Travis CI. Instructors and GSIs can upgrade components and redeploy.
* Students report problems in Piazza. Instructors and GSI raise concerns if necessary to infrastructure staff in Slack.
* Scaling: reduces cloud costs
* Reproducibility: all components are versioned so that the stack can be easily redeployed.

## Managing course content
* Materials interface: Jupyter notebooks
* Content distribution: nbgitpuller + interact links in online syllabus
* Course content storage: GitHub
* Textbook: Gitbook (https://www.inferentialthinking.com)
* Interactivity: notbeook widgets

## Course management
* Grading: OKpy + OKpy service
* Student interactions: Piazza, live chats during class
* Couse outline etc: website via github pages (data8.org)

## Software used in code
* Programming language: Python 3+
* `datascience`, Numpy, Scipy, Folium, Matplotlib
* Environment: miniconda

## Student Workflow
Student clicks on the link …
    * Creates/Starts Jupyter instance
    * Authenticates. Can use home institutional account (e.g. via OAuth) or other
    * Clones/Pulls content into student’s authenticated instance
    * Notebook instance appears in the browser
    * Backed by persistent storage
