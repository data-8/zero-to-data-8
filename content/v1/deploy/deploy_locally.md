# Deploying Data 8 locally

If you'd like to demo the Data 8 textbook locally, you can do so without requiring a JupyterHub.
To make the interact links connect with a local Jupyter session, follow these steps:

## Clone the Data 8 textbook repository to your computer

The Data 8 textbook contains the environment files that specify which packages are needed
to run the code in the textbook. We'll begin by grabbing the latest version of this repository.
Run this code:

    git clone https://github.com/data-8/textbook

This will create a new folder called `textbook/`.

## Download the Anaconda distribution

This will help you manage your environments and download packages needed for the textbook.
To do so, go to https://www.anaconda.com/download/ and pick the distribution that works for your
operating system. **Download the Python 3.X version**.

## Create a conda environment using the textbook repository

Next we'll create the environment needed to run the textbook. Navigate to the `textbook/` directory
that we created earlier. Then, from the root of this repository, run the following command:

    conda env create -f environment.yml

This will create a new conda environment called `textbook` with all of the packages you need to
run the textbook.

## Activate the newly-created conda environment

This will modify your "path" so that all of the packages in this environment are now accessible.

    conda activate textbook

You can confirm that this worked (on *nix systems) by running these commands and making sure that
`/envs/textbook` is a part of each path:

    which pip
    which jupyter

## Activate nbgitpuller

`nbgitpuller` is the tool that is used to pull in content to your Jupyter session with "interact"
links at the top of each notebook. To activate it, run this command:

    jupyter serverextension enable --py nbgitpuller --sys-prefix

## Start a Jupyter Notebook server

Next we'll start a Jupyter Notebook server, which will use `nbgitpuller` to pull in new content
when you click on "interact" links.

    jupyter notebook

**Make note of the URL on which the notebook server is running.** We'll need this in the next step.
It should be something like:

    localhost:8888

## Modify the textbook links to point to your local server

Finally, we'll modify the textbook links so that they work with your
local server. To do so, append `?hub=<your-server-url>` to the end of the textbook URLs.
For example:

    https://www.inferentialthinking.com/chapters/01/3/1/Literary_Characters?hub=http://localhost:8888

## Remove `/hub/user-redirect` from the interact links

If you'd like to interact with a page, copy the link for that page (it should begin with `http://localhost`)
and remove the section `/hub/user-redirect`. Now, when you visit this link, it will pull the corresponding
page into your local Jupyter session.