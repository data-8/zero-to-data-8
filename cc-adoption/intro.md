# Community College(and smaller institutions) Adoption

Under [Cloudbank](https://www.cloudbank.org/) and with funding from [NSF](https://www.nsf.gov/), we are offering a resources to teach Data Science courses including the full set of materials used to teach Data-8 at Berkeley.

There are a series of steps needed to acquire the materials and solutions as well as to gain access to the compute needed for your students and finally, access to our automatic grading system.

You can expect the following:
- The Jupyter Notebooks for labs, homeworks, and projects
- The solutions to all the Jupyter Notebooks
- Lecture Slides and Videos of each lecture
- Worksheets(and solutions) used in the discussion/lab sessions
- A Canvas template customized to use the JupyterHub for your institution
- Access to a JupyterHub instance for your institution configured to your campus Single Sign-on or options
- Access to a grading service that will grade your students notebooks and return the grades in an CSV file

Your institution may need documentation related to privacy(HECVAT) and accessibility(VPAT):
- Here is a [HECVAT](https://docs.google.com/spreadsheets/d/18_Q1b0tisNkQeyj1ibEuvq2Nq7DIF99v/edit?gid=1214776280#gid=1214776280) outlining what student information is needed(just an email address) and how it is protected.
- Accessibility is on-going effort at UC Berkeley and within the Jupyter Community:
    - This [document](https://jupyter-accessibility.readthedocs.io/en/latest/resources/JupyterLab-a11y-statement.html) outlines the current state of Jupyter with regards to accessibility
    - An [extension](https://a11y.datahub.berkeley.edu/) to JupyterHub is being created assess the accessibility of notebooks

**Step 1:**  Privacy Agreement and General Information

We ask that anyone using these materials do not distribute solutions. We also need a GitHub username in order to give you access to the solutions, if you do not have one please create one [here](https://github.com)

Then, complete this [form](https://forms.gle/3gbJQcQNKkYfbW2S7)

**Step 2:** Create a copy of the student materials for yourself

[Screen Recording](https://drive.google.com/file/d/1OODEHdngTajW_kRKTMrVZw9nS4_iiZrq/view?usp=drive_link)

After you have created a GitHub username, please login and then "Fork" this [repo](https://github.com/data-8/materials-sp22)


**Step 3:** Institutional Information for Jupyterhub

We need a few pieces of information about your institution in order to configure the computing environment for your students. Please complete this [form](https://forms.gle/aj2KVirKRFMcQGzd6)

**Step 4:** Accepting the GitHub Repository Invitations

You are going to be added to the materials-sp22-private solutions and resources repository as well as the Otter Service Standalone GitHub Organization used to grade your students notebooks.

You can accept the invitations by clicking each of these links:
- Solutions Repository: [materials-sp22-private](https://github.com/data-8/materials-sp22-private)
- Automatic Grading System(Otter Service Standalone): [otter-service-stdalone](https://github.com/orgs/otter-service-stdalone)

**Step 5:** Canvas Shell and Course Website

Here is a [screen recording](https://drive.google.com/file/d/1rBG97FUwMdV3QQas7znuH8pud-KC8yPM/view?usp=drive_link) of what you need to do to configure the Canvas shell we have set up for you.

You can download the Canvas template [here](https://drive.google.com/file/d/167mhYuq3msva3TO3agFr2jVlPMuzcusw/view?usp=drive_link)

We can help you with this process as well.

This [week-to-week layout](https://www.data8.org/materials-sp22/demo.html) mirrors the Canvas Course layout as well. It is a good resource to get an overview of the course as well explore alternative platforms to render Jupyter Notebooks.

**Step 6:** The Student Workflow

[Screen Recording](https://drive.google.com/file/d/1flQlOZ6ViM0S7S0k0-ZLFZsFNY5ZXMON/view?usp=drive_link)

Here is a summary of the student workflow depicted in the recording:
- Log into your Canvas course/course web page.
- Click on the link for the homework, lab or project
- Another tab opens, and the notebook they have chosen renders in Jupyter Notebook
- The student works through the notebook checking their answers as they go.
- When finished, the student downloads the notebook using the "export" cell at the bottom.
- The downloaded files are uploaded to the correct Canvas assignment or where ever you normally have work submitted.

**Step 7:** Instructor Grading Workflow

[Screen Recording](https://drive.google.com/drive/u/1/folders/1pQ78moc2b9Cl7NXD49N_HJIrwZjXHnt8)

- Student Assignments: After the students have submitted their work, you download all the assignments onto your machine
- Solutions: Log into the GitHub repo, [materials-sp22-private](https://github.com/data-8/materials-sp22-private), navigate to the autograder_zips folder and find the autograder.zip file of the assignment you are grading, download it.
- Automatic Grading: Log into [grader.datahub.berkeley.edu](https://grader.datahub.berkeley.edu) with your GitHub username, and follow instructions in the screen recording above.
- If you would like to test run the grader you can use these archives:
    - [Sample HW 08 Submissions (hw-8-submissions.zip)](hw-8-submissions.zip)
    - [HW 08 Solution file (autograder.zip)](autograder.zip)
