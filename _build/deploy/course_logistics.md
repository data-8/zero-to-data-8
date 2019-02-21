---
redirect_from:
  - "deploy/course-logistics"
title: 'Wisdom and tips for course logistics'
prev_page:
  url: /deploy/connect_labs_and_homework
  title: 'Set up your course labs and homework'
next_page:
  url: /deploy/deploy_locally
  title: 'Demo the textbook locally'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Course Logistics

Data 8 has several moving parts in terms of course makeup and the
technical pieces that make it possible. In this section, we'll describe
some strategies that have worked well for Data 8. They should not be
taken as strict rules, but as guidelines that worked well for us. Feel
free to take a different approach!

## Administering JupyterHub

JupyterHub provides an "administrator" interface that lets you see high-level
information about the JupyterHub deployment, and allows administrators
to perform some common actions on people's running notebook servers.

### Finding the Admin page

To find the Admin page, you should look in the top-left of the page while
in the "Control panel".

If you're in your live Jupyter notebook session, click "Control Panel" in the
top right. Then click "Admin" in the top left.

If you're just logging in, then you should already see "Admin" in the top
left.

### Using the Admin page

The Admin page lists all of the users currently authenticated with the
JupyterHub. It also gives information about activity for each user and
exposes some options for you to oversee their work. In particular:

![Admin page](images/admin_page.png)

* **Add Users** - Allows you to manually add new users to the JupyterHub.
* **Stop server** - Allows you to stop a student's server (useful if something is stuck)
* **Start server** - Allows you to start a student's server (usually done just after stopping their server)
* **Access server** - Allows you to browse the user's directory so that you can see their work. Useful for debugging.
* **Edit/Delete** - Allows you to edit the user's information, or delete them from record
* **Stop All / Shutdown Hub** - Shuts down all user sessions or turns off the JupyterHub. *Only do this if you really know what you're doing!*

## Troubleshooting and debugging

The following sections cover some common troubleshooting problems that
arise, and some things the Data 8 team has learned in solving them.

### Troubleshooting JupyterHub sessions

- **If the student can't log in**, suggest that they open a new
  private browsing window in their browser, try to log in, and give
  the course staff a screenshot of the screens where it got stuck.
  You can also suggest they try a different browser.  That will often
  narrow down whether the issue is something related to their
  browser or cookies etc., or whether it is on the server end.

- **If the student can log into Jupyterhub but their notebook is stuck**
  (e.g., it is not responding), first try restarting their
  kernel: try `Restart Kernel` & `Re-run All` in the top
  menu.

  If it is still stuck, find the cell it is stuck on (should be the first
  cell with no output; it will have a `[*]` next to it).  That is the one that is
  causing problems.  See if it has an infinite loop or a very long-running
  computation.

  Finally, check the memory usage in the upper-right corner
  of the webpage, to see if they have used all available memory.  If the
  student has written code that takes too much time or memory, advise
  them on how to write more efficient code.

- **If a user's session is inexplicably stuck**, try stopping and restarting their server
  on JupyterHub as an administrator. To do so, go to the Administrator page
  when logged in under and administrator account by clicking on the button
  to the top-right. Find the running server you'd like to restart and manually
  do so from this page. See the section above for more information on how
  to do this.

### Common student confusion

- **Running cells in a non-linear fashion** A common student error
  is to run cells in a different order than
  they appear in the notebook.  It is common for cells run "out of order" to
  cause confusion. It's good practice to recommend they
  clear all cells and run them one by one from the top.
  A helpful way to do that quickly is to use `Restart Kernel & Re-run All`,
  then check the output from the cells to make sure everything is
  still correct.

- **Saving student work**. While Jupyter periodically saves the state of
  the Notebook over time, this occasionally doesn't happen as often as students
  expect. Remind students to `Checkpoint & Save` every so often,
  especially before submitting their assignment.
