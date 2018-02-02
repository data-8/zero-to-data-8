# The Data 8 Tech Stack @ Berkeley

## Philosophy
The goal is to develop and run an open platform of which Berkeley happens to be the first user.

## Components

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
