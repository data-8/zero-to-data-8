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

## Managing cloud resources

The core technical piece of Data 8 is the **DataHub**, a server running in the cloud
that serves live computational environments for all of the students in the class.
In Data 8, *students can work entirely from the DataHub*, running in the cloud.

Managing these resources primarily utilizes the following pieces of open-source technology:

* **Managing cloud resources** - [Kubernetes](https://kubernetes.io/) is the underlying technology that manages the resources on our cloud provider. It is open-source, and is supported by most major cloud providers (it also works on your own hardware). By relying on Kubernetes, Data 8 has been able to switch cloud providers nearly each semester with minimal disruption to the class.
* **Managing user sessions** - [JupyterHub](https://github.com/jupyterhub/jupyterhub) is used to manage user sessions in the cloud. It manages user authentication and serves them an environment in which they can do their work. JupyterHub also integrates nicely with Kubernetes via the **JupyterHub Helm Chart**. To learn more about deploying JupyterHub on Kubernetes, see the [Zero to JupyterHub Guide](https://z2jh.jupyter.org)
* **Authentication** - **Google OAuth** is used by **JupyterHub** to handle the actual authentication process. JupyterHub supports a number of options for authentication, and because Berkeley uses Google's "GSuite" of tools, this was the simplest way to authenticate users.

* **Providing cloud resources** - All kinds of providers! A primary goal of Data 8 is to be flexible with respect to the actual computers running student sessions. This means not depending on any one particular cloud provider for the class. To date, Data 8 has been run on: Microsoft Azure, Google Cloud, as well as our own local hardware.

* **Managing the user's software** - We use **Docker images** created specifically for Data 8. They contain all of the software dependencies needed to run all of the course material as well as to interact with JupyterHub. JupyterHub can be configured to serve users a Docker image from the cloud, and any updates to this image will automatically propagate to new user sessions.

* **Distributing files and course materials** - Distributing lectures (in the form of Jupyter Notebooks), homeworks, and other data files are primarily done with [nbgitpuller](https://github.com/data-8/nbgitpuller), a package that integrates with Jupyter, and allows you to automatically download the contents of a git repository into a JupyterHub session. It accomplishes this with "interact links", which connect to the DataHub and instruct it to synchronize a git repository with the student's local filesystem. When students click an interact link, the latest version of the repository's contents are downloaded and the user is directed to the file that the interact link points to.

* **User Long-term Storage** - Students need their work to persist over time, and the storage options for students depend on the cloud provider that is being used for a given semester. JupyterHub for Kubernetes can be configured to plug in to many different kinds of file systems. The authentication process will determine whether a long-term file storage system already exists for a user and, if so, will automatically mount it to a user's session when they connect.

## Administering and managing the cluster
* **Admin access to the DataHub** - The Data 8 team often required access to a high-level view of the DataHub, as well as access to commands that created/destroyed user sessions. This is provided by the **Admin Panel** of JupyterHub, which allows a subset of users to control operations of the DataHub resources.
* **Deploying and updating the DataHub** - While the DataHub is a complicated piece of technology, running it, maintaining it, and updating it should be doable by people without strong technical operations skills. Data 8 uses GitHub repositories to store all configuration scripts for the DataHub, and uses Travis Continuous Integration to automatically-deploy changes to the configuration. As a result, updating the cluster is as simple as changing a configuration file and waiting for the changes to propagate.
* **Student communication and troubleshooting** - All inter-student and class communication is
handled with Piazza, a service for managing communication for courses. Students report technical or course problems in a dedicated Piazza room, and instructors / assistants / staff report technical problems to the infrastructure team.
* **Scaling cloud resources** - An **autoscaler** is used to ensure that Data 8 is only requesting the cloud resources that it needs. Kubernetes makes it easy to scale up/down relatively quickly. This is configured with a script that is cloud-specific for now, but will become possible using only Kubernetes in the future.
* **Versioning and reproducibility** - It is important that we know the *exact* state of the DataHub at any moment in time, and can recreate that state in the future. We use Git and best-practices in package management (e.g., explicitly versioning all components) to ensure that the DataHub configuration can be deployed elsewhere without difficulty.

## Managing course content
* **User interface for course material** - Teaching and student interaction is largely carried out with **Jupyter Notebooks**, a format that allows one to combine narrative and computational content in the same document. Jupyter Notebooks are *runnable*, meaning that students can edit them, interact with them, and generally explore with them *live* on the DataHub. They allow for interactive visualizations and immediate feedback, which are essential in the Data 8 teaching philosophy.
* **Course content storage** - All course content is stored on GitHub, a service that stores code repositories for free. Instructors update course content by pushing new notebooks to the course repository. For example, you can see the [GitHub repository for the Data 8 textbook](https://github.com/data-8/textbook)

* **Course textbook** - The primary textbook used in the course is a GitBook that is hosted on GitHub. Much of the textbook consists of Jupyter Notebooks that interweave the conceptual topic of each lesson with code and interactive content that lets students explore the code within the DataHub. You can find the repository for the textbook [here](https://github.com/data-8/textbook) and a live version of the textbook at [this website](https://inferentialthinking.com)

* **Interactivity and widgets** - The course often uses interactive visualizations and interfaces to let students explore particular concepts or analytic techniques. These are carried out with Jupyter Widgets, which make it easy to create simple interfaces that allow for interactive exploration without requiring students to write code.

## Course management
* **Grading** - Grading in Data 8 is carried out with a service called [OKpy](https://okpy.org/). This is a collection of scripts and services that allow students to check their work within the Jupyter Notebook and submit it to a centralized server for grading.
* **Course syllabus and outline** - The general course structure is written in Markdown, and hosted online with GitHub Pages, a free service for hosting websites that exist on GitHub repositories. You can find the code repository for the Data 8 website [here](https://github.com/data-8/data-8.github.io).

## Software used in code
* **Programming language** - The programming language of choice for Data 8 is Python 3. This is because Python is a generic, user-friendly, and well-designed language that is broadly useful in data science. It is the most popular language for high-level data analytics, and has a rich ecosystem of packages for interactive data analysis.
* **Primary data object and functions** - There are *many* packages for data analytics in Python, each with their own API and way of doing things. Data 8 wraps several of these packages into a single Python package focused on teaching datascience skills without getting into the weeds of the individual pieces of the Python ecosystem. This package is called `datascience`, and is hosted online in [this GitHub repository](https://github.com/data-8/datascience). The package is *not* meant as a replacement for subsequent components of the Python analytics ecosystem, and students are expected to use these more widely-used packages in subsequent courses.
* **Handling the Python environment** - Student environments in Python are managed with `miniconda`, a package from Anaconda that makes it easy to create user environments, as well as install / remove / update particular Python packages.
