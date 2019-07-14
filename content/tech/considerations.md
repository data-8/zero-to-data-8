# Technical Considerations

Data 8 teaches a mixture of analytics and programming to nearly 1400 undergraduates, and makes no
strong assumptions about their background in either of these fields. Managing a class this size
doing non-trivial computational work is a big technical challenge. This page details many of
the guiding principles and priorities that the Data 8 team considered in solving these problems with
technology.

## Open source strategy

A core goal of the Data 8 project is to use an entirely open stack to use in our course. We
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

So what do we mean when we say "open stack"? Open source tools are inter-woven with the Data 8
mission. We'll cover several of the main pieces of this stack in the sections below.

### Python - an open language

Data 8 uses Python for all of its course material. This is because its both extremely popular
as well as open source. Being an open source language means that anybody can use the language,
contribute to it, or even modify it if they wish. The language isn't "owned" by anybody, which
we believe is an important foundation to use for introducing students to data science.

### The Scipy stack - an open source ecosystem

On top of the Python language is a thriving community of libraries and tools for scientific
computing. These are largely developed and driven by an open community of developers, many
of whom are researchers and educators at universities. Utilizing an open stack allows us to
leverage the combined expertise of thousands of members of the open source community. For
example, the `datascience` package utilizes functions in NumPy (a tool for linear algebra),
SciPy (a set of tools for scientific tasks), Pandas (a tool for dealing with tabular data),
and Matplotlib (a tool for visualization).

### Jupyter Notebooks - an open source interface

The interface that all students use is called the Jupyter Notebook interface. Jupyter Notebooks
are an open source tool built by the Jupyter Project, another open project. They are a de-facto
standard across both academic research as well as industry. We wanted to use notebooks both because
they were quite useful for interactive computing and as a tool for communication, but also because
they are free, usable by anybody, developed by an open community, and used across many institutions
and organizations.

### JupyterHub and Kubernetes - open infrastructure for the cloud

Finally, all of the course infrastructure that Data 8 uses runs on JupyterHub and Kubernetes. These
are both open source projects for managing user sessions as well as orchestrating computational
resources in the cloud. We decided to run our course on open infrastructure because it gives us
the freedom to run Data 8 on any cloud provider, and lessens the likelihood that we will become
dependent on a single cloud vendor to run the course. It also allowed us to improve these tools,
allowing other organizations to deploy JupyterHub for teaching Data 8 on whatever cloud resources
they'd prefer. For example JupyterHub runs on both large, scalable cloud infrastructure like
Kubernetes, but also on much smaller-scale infrastructure such as a single machine, which gives
others more flexibility in how and where they want to run their data 8 infrastructure.

## Major hurdles

The following are major hurdles that we encountered when running and designing Data 8.

* **Standardizing environments is hard**. Anyone who has taught a bootcamp knows the pain involved in getting a room of 20 students with the same functioning environment. Data 8 has nearly two orders of magnitude more students. For an introduction class, requiring students to set up their own environment is a huge distraction and dis-equalizer.
* **Avoiding cloud lock-in**. There are many options for interacting with the cloud, but most are bespoke interfaces that pair with a *product* you eventually pay for (e.g. https://aws.amazon.com/education/). We didn't want Data 8 to depend on a specific provider, interface, or other set of packages.
* **Be platform-agnostic**. Most data analytics classes have similar problems (e.g., managing a kernel in the cloud) even if the tools they use are quite different (e.g., R vs. Python). Data 8 intentionally used tools that were platform-agnostic (e.g., tools in the Jupyter project) to make course infrastructure useful for many different topics.
* **Use open-source tools.** While there are many proprietary options for managing classrooms and technical resources, they are not as generalizable and serve as hurdles to wider adoption of material.
* **Development/Operations skills are not common**. Scaling class to large size requires technical + personnel that aren't always common in academia

## Priorities / Solutions

* **Use the cloud** - By utilizing cloud resources, the course material is available to all students regardless of the hardware available to them.
* **Be cloud agnostic** - We want to give students and instructors the ability to work on whatever platform they like. As such, we chose tools that were open-source and cloud-agnostic.
* **Shield students from complex APIs** - The world of data analytics has a diverse ecosystem of packages, each with their own API and quirks. We attempted to shield students from this diversity to focus on the fundamentals, and assume students will dig into specific APIs in subsequent courses.
* **Use diverse real-world / compelling data** -
* **Keep costs down** - Broader adoption of the course at Berkeley and beyond will only happen if costs are reasonably low. We shoot for a few dollars per student, per month.
* **Handle dynamic activity** - Students tend to operate in bursts of activity (e.g., during class or 30 minutes before the homework is due). We needed dynamic cloud infrastructure that could handle many patterns of activity.
* **Meet peak demand** - Moments of maximal cloud usage (e.g., during a test) are moments when the cloud *must be functional*.
* **Do all of the above with a small team** - The Data 8 model is not scalable if it requires a dedicated team of tech-savvy staff. While some technical skills are required, we wanted most course operations to be handled by a small team of undergraduates (usually Data 8 alumni).

## Desired Student Workflow

From a student's perspective, this is the workflow that we wanted them to have access to:

The instructor creates a piece of course material they want students to be able to use.
They push the latest version of this material to GitHub, then send students a link that
they can click in order to interact with the material.

The student clicks on the link, which triggers the following actions:

* The DataHub authenticates the user (either asking them to sign in, or discovering that their local computer already has credentials to proceed).
* The DataHub creates and starts a Jupyter instance for the user (or directs the user to a pre-existing environment from a previous session)
* The student's persistent storage volume is linked to their Jupyter instance
* The DataHub clones or pulls the content specified by the link into student’s instance
* The student is then directed to a live notebook instance in the browser. It contains the content specified in the link and can be immediately interacted with.
