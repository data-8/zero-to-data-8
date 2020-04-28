# Otter Grader

[Otter](https://otter-grader.readthedocs.io) is a light-weight scalable autograding tool that allows instructors to customize their grading methodology. It is a command line tool divded into four tools that span the assignment generation and grading process: Otter Assign, Otter Generate, Otter Check, and Otter Grade.

## Otter Tools

* **Otter Assign** is a fork of [OkPy's jassign](https://github.com/okpy/jassign) that allows instructors to create a master notebook containing questions, solutions, and tests and parses them into autograder and students distribution versions. It fully integrates with the other Otter tools, e.g. allowing instructors to generate an autograding file for Gradescope as a part of the Assign process.
* **Otter Generate** is a tool for creating the zipfile required to use Otter to grade assignments on Gradescope's autograding platform. It allows instructors to collect tests and any support files necessary (e.g. data files) into an autograder that grades students' submissions when they upload to Gradescope. Instructors can configure the grading process and the visibility of results, including setting seeds for each cell that is executed to ensure the same results are reached by students' code.
* **Otter Check** is the student-facing component of Otter and is comprised of an IPython API `otter.Notebook` and a command line script checker that execute tests against a student's work and let them know whether or not they're passing any tests distributed with the notebook. It also allows students to generate PDFs of their submissions that can be submitted with or instead of the Jupyter Notebook file to make grading e.g. written questions easier.
* **Otter Grader** is the core original functionality of Otter that allows instructors to grade student submissions locally in sandboxed Docker containers. This tool supports submission export formats from LMS's like Gradescope and Canvas and returns to instructors a CSV of grades for each submission and, optionally, a generated and fitlerable PDF of each submission for manual grading.

## Instructor Workflow

Because of the various ways in which Otter can be used, the workflow is very customizable and allows instructors to do whatever works best for them. In this section, we outline two of the more common workflows.

### Otter + Gradescope

In this workflow, the instructor starts by using Otter Assign to create a master notebook and the Otter Generate integration to simultaneously generate a zipfile to upload to Gradescope. The instructor then creates the Gradescope assignment, uploads this zipfile to create the autograder, and distributes the student notebook however they prefer. Students can run through public tests in the notebook and, when they are ready to submit, download their notebook (and possibly a PDF) and upload these files to Gradescope. Gradescope grades these on submission and instructors can also grade questions manually.

### Otter Locally

This workflow is very similar to the previous version, except without Gradescope. Instructors create a distribution of an assignment with Otter Assign and distribute it to students in some form or fashion. Students then submit their finished work to instructors through a channel of their choice and instructors collect these files locally and grade them using Otter Grade.
