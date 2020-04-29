# OkPy

[OkPy](https://okpy.github.io/documentation/) is one of Berkeley's original autograding solutions, originally developed for Python scripts in [CS 61A](https://cs61a.org) and since adapted for use with Jupyter Notebooks. Like most autograders, it supports in-notebook checks and server-based autograding hosted on [okpy.org](https://okpy.org).

## Assignment Workflow

The first step in autograding is creating an assignment and tests. [Jassign](https://github.com/okpy/jassign) is a tool that simplifies this process by allowing instructors to create a master notebook that includes questions, solutions, and public and hidden tests, which are then parsed into the correct test files and notebook versions (one solutions notebook and one sanitized student notebook). 

After you have created the notebook, continue by making an assignment on [okpy.org](https://okpy.org) and generating a `.ok` file that is used to configure the autograding client. The `.ok` file is placed in a public GitHub repo with the student notebook and any support files (e.g. data files), which students will pull into their JupyterHub accounts to work on.

Grading code is then performed automatically on OkPy when a student submits. Autograders default to timing out after 300 seconds, although this is configurable. It is also possible to create custom integrations with the OkPy server to incorporate it into existing workflows.

## Student's View

The general workflow for students when using OkPy is as follows:

1. Run an authentication cell that sends them to the OkPy website to authenticate with Google and provides them an API key which is put into the notebook
2. Work through an assignment, running check cells as needed
3. Run a submit cell that sends the notebook to OkPy

One advantage here is that this experience is (almost) entirely within the notebook and students don't need to worry about donwloading and uploading files.
