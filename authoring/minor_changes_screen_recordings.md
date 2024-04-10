# Minor Changes to existing Otterized Notebooks

Many of the users of Data 8 want to make minor changes to existing notebooks. These changes might include minor changes to problems, changes to numbers used to calculate answers, and possibly even adding questions and datasets.

This screen recording moves through the steps it takes to make these changes and publish the notebooks for your class.

This recording and instructions below assumes a couple of pieces:
- You have already created a private(for instructor materials) and public(for students) repositories in GitHub. (If you have not done this, there is a screen recording [here](./authoring_screen_recordings.md) explaining how.)
- This also assumes you have access to a JupyterHub or python environment where all the packages are installed, including otter-grader version 4.4.1
- This also assumes you are not changing the name of the assignment so that any nbgitpuller links you have created for students are still going to work.

[Screen Recording (11 min)](https://drive.google.com/file/d/1OsC-iE0_1HXy-y3CXEUWZcb7IGboHbXZ/view?usp=sharing)


Summary of Instructions illustrated in recording:
- Download the private repository containing all the raw notebooks for editing
- Log into your hub: https://xxx.cloudbank.2i2c.cloud
- Switch to the lab view: https://.../tree --> https://.../lab
- Create a folder on the hub to put the notebook and files you are working with in - e.g hw03
- Drag the files you need from your computer related in this example to hw03 into the folder you created on the hub
- Edit hw03.ipynb
- Open a Terminal: Verify the otter-grader version: otter --version
- If you don't have otter-grader 4.4.1 install it: pip install otter-grader==4.4.1
- Run otter assign: otter assign hw03.ipynb ../dist-hw03
- Transfer the student notebook to the public repo via upload to GitHub
- Transfer the changed raw notebook back up to private repo in GitHub
- Decide where to store the autograder.zip:
    - leave on the hub
    - download to your computer
    - or save to the private repo 