# Connect your hub with the course materials

> My hub IP: 104.197.203.241

Now that our JupyterHub has the Data 8 computing environment, it's time to
connect it with the course materials for the class (e.g., lectures, labs, and homeworks).

## Course materials

This section covers the location and structure of all course materials
used in Data 8

### The Data 8 textbook

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

### Data 8 labs

Alongside the textbook are several computational labs that operationalize the
ideas covered in class and give students a chance to explore on their own.
They can all be run interactively in the Data 8 environment (the same
environment that we've used in your JupyterHub).

The latest links to the labs can be found in the course page for the current
semester. For example, the Spring 2018 course is found here:

http://data8.org/sp18/

These materials are freely available on the semester course repository.
There is a new one created for each semester of the course, as the materials
tend to evolve over time. Here is the repository for the Spring 2018 course:

https://github.com/data-8/materials-sp18

### Homeworks

- **TODO: add homework section, need to figure out how to handle grading**



## Interact links

The primary way that material is distributed in Data 8 is via "interact links". These are links that,
when clicked, will automatically pull new material into a students' file system on the DataHub, and then
direct them to this new content in a live session.

The tool that you'll use to do this is called [nbgitpuller](https://github.com/data-8/nbgitpuller),
which is pre-installed in the Docker image for the course. This means you can create interact links
without needing to install anything new. For example, clicking the following link should pull in
the [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks) from Jake van der Plas:

`http://{{ your-hub-ip }}/hub/user-redirect/git-pull?repo=https://github.com/jakevdp/PythonDataScienceHandbook&branch=master&subPath=notebooks`

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
* Run the interact link renaming script (which is in *this* repository):

  `python rename_interact_links.py <new-hub-ip>`

  The value in `<new-hub-ip>` should be the full URL (including `http://`)
  of your JupyterHub.
* This will over-write all links in the textbook. Confirm that this has
  worked by clicking on one of the renamed links. It should direct you
  to the content on **your JupyterHub**.
* Commit the changes that have been made in your fork.

### Interact links for the Data 8 labs

Creating interact links for the Data 8 labs works the same way as it
does for the textbook. All labs should already be runnable on the
environment that the Data 8 Docker image serves.

In this case, you simply need to look up the links that are hosted on
the [Data 8 semester materials page](http://data8.org/sp18/) and
replace the Berkeley DataHub address with the address for your
hub. For example, the following interact link should open a lab from
week 2 on **your JupyterHub**:

`http://{{ your-hub-ip }}/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp18&subPath=materials/sp18/lab/lab02/lab02.ipynb`

### Interact links for homeworks

* **TODO: Add section on scraping the OKpy server stuff out of the homeworks. We can either add a helper script, or create a public versions of the homeworks with this stuff scraped out.**
