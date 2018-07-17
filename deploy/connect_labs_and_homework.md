# Connecting Data 8 Labs and Homework

Now that our JupyterHub has the Data 8 computing environment, it's time to
connect it with the course materials for the class (e.g., lectures, labs, and homeworks).
This section covers how to get your own copies of the course labs and
homeworks, so that you can modify them and distribute as you wish. We'll
cover how to connect with the Data 8 textbook in the next section.

## Distributing course content

This section covers a few tips on how to distribute content for your Data 8
course.

### Interact links

The primary way that material is distributed in Data 8 is via "interact links". These are links that,
when clicked, will automatically pull new material into a students' file system on your JupyterHub, and then
direct them to this new content in a live session.

The tool that you use to do this is called [nbgitpuller](https://github.com/data-8/nbgitpuller),
which is pre-installed in the Docker image for the course. This means you can create interact links
without needing to install anything new. For example, the following link should pull in
the [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks) from Jake van der Plas:

`http://{{ YOUR-HUB-IP }}/hub/user-redirect/git-pull?repo=https://github.com/jakevdp/PythonDataScienceHandbook&branch=master&subPath=notebooks`

In the following sections we'll cover how interact links can be used with each type of Data 8
content in order to distribute materials to your students.

### Course syllabus page

You may use whatever technology you prefer for managing your course and
distributing content. However, we recommend setting up a syllabus page that
is used for distributing interact links and course materials. For an example,
see the structure of the Spring 2018 course syllabus:

http://data8.org/sp18/

It has a structure like this:

| Date          | Topic | Lecture  | Reading | Assignment
| ------------- | ----- | -------  | ------- | ----------
| 2018-01-09 | Cause and Effect | [Slides](http://data8.org/materials-sp18/lec/lec02PDF.pdf), [Video](https://www.youtube.com/watch?v=oF9rA2PYG6A) | [Chapter 2](https://www.inferentialthinking.com/chapters/02/causality-and-experiments.html) | [Homework 01](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp18&subPath=materials/sp18/hw/hw01/hw01.ipynb)
| 2018-01-22 | Tables | [Demos](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp18&subPath=lec/lec03.ipynb), [Slides](http://data8.org/materials-sp18/lec/lec03PDF.pdf), [Video](https://www.youtube.com/watch?v=NLw4egmXBHM) | [Chapter 3](https://www.inferentialthinking.com/chapters/03/programming-in-python.html)| |
| 2018-01-24 | Data Types | [Demos](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp18&subPath=lec/lec04.ipynb), [Slides](http://data8.org/materials-sp18/lec/lec04PDF.pdf), [Video](https://www.youtube.com/watch?v=O3AAJs7dx-c) | [Chapters 4](https://www.inferentialthinking.com/chapters/04/data-types.html), [5](https://www.inferentialthinking.com/chapters/05/sequences.html)| [Lab 02: Types and Sequences](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp18&subPath=materials/sp18/lab/lab02/lab02.ipynb)

Each row is a class, and each column is a type of material you can distribute.
Links either point to pages on the course textbook (at inferentialthinking.com)
or interact links that connect students with the course JupyterHub to
distribute homeworks and labs.

## Labs

Alongside the textbook are several computational labs that let students interact with the
ideas covered in class. They can all be run interactively in the Data 8 environment (the same
environment that we've used in your JupyterHub).

The latest links to the labs can be found in the course page for the current
semester. For example, the Spring 2018 course is found here:

http://data8.org/sp18/

These materials are freely available on the semester course repository.
There is a new repository created for each semester of the course, as the materials
tend to evolve over time. For example, here is the repository for the Spring 2018 course:

https://github.com/data-8/materials-sp18

you can find the labs for this repository here:

https://github.com/data-8/materials-sp18/tree/master/materials/sp18/lab


### Customizing your own copies of the labs

All labs should already be runnable on the environment that the Data 8 Docker image serves.
The Data 8 materials are shared by adding
"interact links" to the following syllabus page:

http://data8.org/sp18/

We recommend forking and customizing your own version of the labs, so that you can ensure the
content is the right match for your course. To do this, perform the following steps:

1. Fork the repository for the course you want to run. (e.g., `https://github.com/data-8/materials-sp18/`)
2. Clone your repository to your machine

       git clone https://github.com/<YOUR-USERNAME>/materials-sp18/

3. Make modifications to the labs as you see fit, push them to GitHub
4. Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
5. Create your interact links so they point to *your* version of the labs. For example,

       http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{ YOUR-ORG }}/materials-sp18&subPath=materials/sp18/lab/lab02/lab02.ipynb

## Homework

Homework in Data 8 is used for course grading as well as to guide students through the
material. The homework uses a package called OKpy for auto-grading student homework. This can be
used in two primary ways:

1. Grading is performed locally (on the students own computer) in order to give live feedback
   to the code that students write.
2. Grading is performed with the OKpy servers. This requires an account with OKpy, and is
   used by Data 8 to handle "official" grades for the course.

At the moment, we recommend using only #1 for your course.

The latest links to the homeworks can be found in the course page for the current
semester. For example, the Spring 2018 course is found here:

http://data8.org/sp18/

These materials are freely available on the semester course repository.
There is a new repository created for each semester of the course, as the materials
tend to evolve over time. For example, here is the repository for the Spring 2018 course:

https://github.com/data-8/materials-sp18

you can find the homeworks for this repository here:

https://github.com/data-8/materials-sp18/tree/master/materials/sp18/hw


### Grading course homework

Grading in Data 8 is performed with the [OKpy package](https://okpy.org/). This is a course
management tool that allows you to both collect and grade notebooks, take
attendance, and manage many other course tasks.

If you prefer a more light-weight solution, we recommend looking into [gradememaybe](https://github.com/data-8/gradememaybe).
This package replicates the auto-grading function of OKpy, without the other aspects
of course management. It is useful if you *only* wish to use the tool for giving interactive
student feedback and for grading assignments, and do not wish to use the OK servers for this.

`gradememaybe` works with the same API that `OKpy` uses, meaning that using one package
or another should require no change in the code itself. The only difference is that
`gradememaybe` will not send any course material to the OKpy servers.

> **Note:** `gradememaybe` and `OKpy` should not both be installed at the same time. If one
  is installed, the other should be uninstalled.

### Customizing your own copies of the homework

To customize the Data 8 homework for your course, take the following steps:

1. Fork and clone the Data 8 materials for the semester of your choice (see above section on labs).
2. Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
3. Create your interact links so they point to *your* version of the homeworks. For example,

       http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{ YOUR-USERNAME }}/materials-sp18/materials/sp18/hw/hw07/hw07.ipynb

## Next step

Now that you've prepared materials for your course and JupyterHub, it's
time to [connect with the course textbook](connect_website_and_textbook.md)
