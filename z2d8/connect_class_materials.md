# Connect your hub with the course materials

Now that our JupyterHub has the Data 8 computing environment, it's time to
connect it with the course materials for the class (e.g., lectures, labs, and homeworks).

## Interact links

The primary way that material is distributed in Data 8 is via "interact links". These are links that,
when clicked, will automatically pull new material into a students' file system on the DataHub, and then
direct them to this new content in a live session.

The tool that you use to do this is called [nbgitpuller](https://github.com/data-8/nbgitpuller),
which is pre-installed in the Docker image for the course. This means you can create interact links
without needing to install anything new. For example, clicking the following link should pull in
the [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks) from Jake van der Plas:

`http://{{ your-hub-ip }}/hub/user-redirect/git-pull?repo=https://github.com/jakevdp/PythonDataScienceHandbook&branch=master&subPath=notebooks`

In the following sections we'll cover how interact links can be used with each type of Data 8
content in order to distribute materials to your students.

## The textbook

The entire Data 8 textbook is available freely online. It is hosted
at https://inferentialthinking.com, and the raw materials can be found at https://github.com/data-8/textbook.
The textbook contains a combination of narrative and computational material,
and is meant to teach students the ideas surrounding data science while
getting their hands dirty and learning interactively.

You may use this textbook in your own version of Data 8, as well as the
materials surrounding it such as labs and homeworks. There is some
cleanup you'll need to do in order to adapt the materials for your course
(such as pointing links to your JupyterHub instead of the Berkeley hub).
We'll cover these below.

### Interact links for the Data 8 textbook

You can create an interact link for the data 8 textbook like so:

`http://{{ your-hub-ip }}/hub/user-redirect/git-pull?repo=https://github.com/data-8/textbook&branch=gh-pages&subPath=notebooks/Numbers.ipynb`

Clicking this link will pull in the latest version of the material for
the textbook, and direct users to the `notebooks/Numbers.ipynb` notebook.

Note that there are many embedded links in the Data 8 textbook already.
Currently these point to a website called `mybinder.org`, which lets you
run custom computational environments for free. However, this site does not
have any authentication or persistent user storage.

If you'd like the textbook interact links to point to your own JupyterHub,
you'll need to change the links that the "interact" buttons point to. We've
included a helper script to do this automatically in this repository. To use
it, follow these steps:

* Fork the [data 8 textbook](https://github.com/data-8/textbook).
* Clone this fork to your computer
* Open to the `convert_notebooks_partial.py` script
* Navigate to the section of code titled "**Using custom interact links**"
* Follow the instructions to add the URLs for your JupyterHub
* Run `make notebooks` to generate HTML you can use with your course site.

This HTML can be used with whatever platform you wish to host your textbook.

## Labs

Alongside the textbook are several computational labs that operationalize the
ideas covered in class and give students a chance to explore on their own.
They can all be run interactively in the Data 8 environment (the same
environment that we've used in your JupyterHub).

The latest links to the labs can be found in the course page for the current
semester. For example, the Spring 2018 course is found here:

http://data8.org/sp18/

These materials are freely available on the semester course repository.
There is a new one created for each semester of the course, as the materials
tend to evolve over time. For example, here is the repository for the Spring 2018 course:

https://github.com/data-8/materials-sp18

you can find the labs for this repository here:

https://github.com/data-8/materials-sp18/tree/master/materials/sp18/lab


### Customizing your own copies of the labs

All labs should already be runnable on the environment that the Data 8 Docker image serves.
You can share the URLs for various Data 8 course materials (homeworks, labs, etc)
with whatever method you prefer. For example, the Data 8 materials are shared with updates
to the following page:

We recommend forking and creating your own version of the labs, so that you can ensure the
content is the right match for your course. To do this, perform the following steps:

* Fork the repository for the course you want to run. (e.g., `https://github.com/data-8/materials-sp18/`)
* Clone your repository to your machine (e.g., `git clone https://github.com/<YOUR-USERNAME>/materials-sp18/`)
* Make modifications to the labs as you see fit
* Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
* Create your interact links so they point to *your* version of the labs. For example,
  
  `http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{YOUR-USERNAME}}/materials-sp18&subPath=materials/sp18/lab/lab02/lab02.ipynb`


## Homework

Homework in Data 8 is used both for course grading, as well as to guide students through the
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
There is a new one created for each semester of the course, as the materials
tend to evolve over time. For example, here is the repository for the Spring 2018 course:

https://github.com/data-8/materials-sp18

you can find the homeworks for this repository here:

https://github.com/data-8/materials-sp18/tree/master/materials/sp18/hw

### Customizing your own copies of the homework

To customize the Data 8 homework for your course, take the following steps:

* Fork and clone the Data 8 materials for the semester of your choice (see above section on labs).
* In the homeworks, remove all references to OKpy **server**. This means removing a
  particular line from homeworks before sharing them with your students.

  We have provided a script to do this automatically. It is located in
  `dsep_stack/z2d8/scripts`. To use it, navigate to this folder, then run:
  
  `python remove_okpy_server_code.py path/to/input_notebook.ipynb path/to/output_notebook.ipynb`

  This will create a notebook at the output path after removing the relevant references
  to the OKpy servers.
* Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
* Create your interact links so they point to *your* version of the homeworks. For example,
  
  `http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{YOUR-USERNAME}}/materials/sp18/hw/hw07/hw07.ipynb`


