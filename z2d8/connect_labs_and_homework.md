# Connecting Data 8 Labs and Homework

This section covers how to get your own copies of the course labs and
homeworks, so that you can modify them and distribute as you wish.

Note that the course website template has a section for the course syllabus
in the file `syllabus.md`. You can update the markdown table in this file
in order to provide links to new homeworks and labs.

## Interact links

The primary way that material is distributed in Data 8 is via "interact links". These are links that,
when clicked, will automatically pull new material into a students' file system on the DataHub, and then
direct them to this new content in a live session.

The tool that you use to do this is called [nbgitpuller](https://github.com/data-8/nbgitpuller),
which is pre-installed in the Docker image for the course. This means you can create interact links
without needing to install anything new. For example, clicking the following link should pull in
the [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks) from Jake van der Plas:

`http://{{ YOUR-HUB-IP }}/hub/user-redirect/git-pull?repo=https://github.com/jakevdp/PythonDataScienceHandbook&branch=master&subPath=notebooks`

In the following sections we'll cover how interact links can be used with each type of Data 8
content in order to distribute materials to your students.

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

We have created a similar page in `syllabus.md` that you can use to append new
links to for your course.

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

### Customizing your own copies of the homework

To customize the Data 8 homework for your course, take the following steps:

1. Fork and clone the Data 8 materials for the semester of your choice (see above section on labs).
2. In the homeworks, remove all references to OKpy **server**. This means removing a
   particular line from homeworks before sharing them with your students.

   We have provided a [script to do this automatically](https://github.com/choldgraf/dsep_stack/blob/master/z2d8/scripts/remove_okpy_from_data8.py).
   To use it, download the script and navigate to its folder, then run:

       python remove_okpy_from_data8.py path/to/course_materials/folder`

   This will create a new version of the homeworks in the output folder
   after removing the relevant references to the OKpy servers.

3. Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
4. Create your interact links so they point to *your* version of the homeworks. For example,

       http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{ YOUR-USERNAME }}/materials/sp18/hw/hw07/hw07.ipynb
