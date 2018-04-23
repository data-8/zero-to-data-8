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

`http://{{ YOUR-HUB-IP }}/hub/user-redirect/git-pull?repo=https://github.com/jakevdp/PythonDataScienceHandbook&branch=master&subPath=notebooks`

In the following sections we'll cover how interact links can be used with each type of Data 8
content in order to distribute materials to your students.

## The textbook

The entire Data 8 textbook is available freely online. It is hosted
at https://inferentialthinking.com, and the raw materials can be found at https://github.com/data-8/textbook.
The textbook contains a combination of narrative and computational material,
and is meant to teach students the ideas surrounding data science while
learning interactively.

You may use this textbook in your own version of Data 8, as well as the
materials surrounding it such as labs and homeworks. There is some
cleanup you'll need to do in order to adapt the materials for your course
(such as pointing links to your JupyterHub instead of the Berkeley hub).
We'll cover these below.

### Making your own version of the textbook and interact links

Note that there are many embedded links in the Data 8 textbook that point
to interactive materials. These point to a website called `mybinder.org`, which lets you
run custom computational environments for free. However, this site does not
have any authentication or persistent user storage.

To create your own version of the data 8 textbook, take the following steps:

* Fork the [data 8 textbook](https://github.com/data-8/textbook).
* Clone this fork to your computer
* Make any edits you wish to the textbook. If you'd like to make large edits
  or derivatives of the content, please reach out to the Data 8 team first.

You can then create an interact link for the data 8 textbook like so:

`http://{{ YOUR-HUB-IP }}/hub/user-redirect/git-pull?repo=https://github.com/{{ YOUR-ORG }}/textbook&branch=gh-pages&subPath=notebooks/Numbers.ipynb`

Clicking this link will pull in the latest version of the material for
your copy of the textbook, and direct users to the `notebooks/Numbers.ipynb` notebook.

### Customizing the interact links in your textbook

If you'd like the textbook interact links to point to your own JupyterHub,
you'll need to run a helper script to do this automatically in your repository.
To use it, follow these steps:

* Navigate to the root of the repository for your version of the Data 8 textbook
* Open the `convert_notebooks_to_html_partial.py` script
* Navigate to the section of code titled "**Using custom interact links**"
* Follow the instructions to add the URLs for your JupyterHub

When you build the HTML for your textbook (see next section), the interact buttons
will now point to your JupyterHub.

### Generating the HTML to host your textbook online

After your content and interact links are finalized, you must finally convert
your notebooks into HTML files that can be hosted online. To do this, take the following
steps:

* Navigate to the root of the repository for your version of the Data 8 textbook
* Run `make notebooks` to generate HTML you can use with your course site.
* An HTML version will be created for each notebook, and placed in `notebooks-html`
* These are meant to be hosted online with GitBook.

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
You can share the URLs for various Data 8 course materials (homeworks, labs, etc)
with whatever method you prefer. For example, the Data 8 materials are shared by adding
"interact links" to the following syllabus page:

http://data8.org/sp18/

We recommend forking and customizing your own version of the labs, so that you can ensure the
content is the right match for your course. To do this, perform the following steps:

* Fork the repository for the course you want to run. (e.g., `https://github.com/data-8/materials-sp18/`)
* Clone your repository to your machine (e.g., `git clone https://github.com/<YOUR-USERNAME>/materials-sp18/`)
* Make modifications to the labs as you see fit, push them to GitHub
* Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
* Create your interact links so they point to *your* version of the labs. For example,
  
  `http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{ YOUR-ORG }}/materials-sp18&subPath=materials/sp18/lab/lab02/lab02.ipynb`

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
There is a new repository created for each semester of the course, as the materials
tend to evolve over time. For example, here is the repository for the Spring 2018 course:

https://github.com/data-8/materials-sp18

you can find the homeworks for this repository here:

https://github.com/data-8/materials-sp18/tree/master/materials/sp18/hw

### Customizing your own copies of the homework

To customize the Data 8 homework for your course, take the following steps:

* Fork and clone the Data 8 materials for the semester of your choice (see above section on labs).
* In the homeworks, remove all references to OKpy **server**. This means removing a
  particular line from homeworks before sharing them with your students.

  We have provided a [script to do this automatically](https://github.com/choldgraf/dsep_stack/blob/master/z2d8/scripts/remove_okpy_from_data8.py).
  To use it, download the script and navigate to its folder, then run:
  
  `python remove_okpy_from_data8.py path/to/course_materials/folder path/to/output/folder`

  This will create a new version of the homeworks in the output folder
  after removing the relevant references to the OKpy servers.

* Ensure that you have a JupyterHub running the Data 8 environment (if not, [follow these instructions](customize_hub_environment.html))
* Create your interact links so they point to *your* version of the homeworks. For example,
  
  `http://{{ YOUR-HUB-URL }}/hub/user-redirect/git-sync?repo=https://github.com/{{ YOUR-USERNAME }}/materials/sp18/hw/hw07/hw07.ipynb`


