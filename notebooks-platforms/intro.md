# Data 8 Notebooks in Various Forms

The following are the notebooks used in Data 8 but created for different platforms in the case you are not using a JupyterHub instance. The first line contains a normal set of notebooks with all the data files in the distribution. The second set, marked "-no-footprint", is the exact same notebooks but the data files used in the notebooks are loaded via a URL instead of being stored with the notebooks themselves.

**CodeSpaces:** 
[CodeSpaces](https://github.com/features/codespaces/) is a GitHub programming environment that can be used for Jupyter Notebook rendering.  We have links set up to open in CodeSpace on the demonstration page of the materials-fds repository.
- [materials-fds Demo Page](https://www.data8.org/materials-fds/demo.html)


**Colab:** 
[Colab](https://colab.research.google.com/) is the Google-created Jupyter Notebook rendering platform. In order to use Otter Grader with Colab, you need to have the student mount their Google Drive; these notebooks mount the Google Drive for the student.
- [materials-fds-colab](https://github.com/data-8/materials-fds-colab)
- [materials-fds-colab-no-footprint](https://github.com/data-8/materials-fds-colab-no-footprint)

**Jupyterlite:** 
[Jupyterlite](https://jupyterlite.readthedocs.io/en/stable/) is a relatively new notebook rendering system that works in your local browser -- no server needed, no authentication, and no cost. There are downsides, for one, the student needs to save the notebook regularly to the computer or else it is stored in the browser's cache - if the cache were to be cleared they would lose their work.

Instructions for using Jupyterlite are in the README file for each repository.
- [materials-fds-jupyterlite](https://github.com/data-8/materials-fds-jupyterlite)
- [materials-fds-jupyterlite-no-footprint](https://github.com/data-8/materials-fds-jupyterlite-no-footprint)

**Binder:**
[Binder](https://mybinder.readthedocs.io/en/latest/index.html) is a community-driven Jupyter Notebook rendering service. It has some limits including memory, time of inactivity and no long-term storage. 

- [materials-fds-binder](https://github.com/data-8/materials-fds-binder)
- [materials-fds-binder-no-footprint](https://github.com/data-8/materials-fds-binder-no-footprint)

**Otterless (No autograding - just clean Jupyter Notebooks)**
We removed all the otter-grader cells from the notebooks for those who are not interested in automatic grading.
- [materials-fds-otterless](https://github.com/data-8/materials-fds-otterless/)