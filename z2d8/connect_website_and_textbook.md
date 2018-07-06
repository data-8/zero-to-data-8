# Connect your hub with the course materials

Now that our JupyterHub has the Data 8 computing environment, it's time to
connect it with the course materials for the class (e.g., lectures, labs, and homeworks).

You'll create your own versions of the course materials used in Data 8, then
host them all in one place using a Jekyll website. We'll cover the textbook
in this section, and the homeworks/labs in the next section.

## The Data 8 Textbook

The [online Data 8 textbook](https://www.inferentialthinking.com/) is
built using a site generation engine called [Jekyll](https://jekyllrb.com/),
and hosted online with the free [GitHub Pages](https://pages.github.com/) service.

For a short explanation of the structure / relevant files / etc of the
Data 8 textbook, see the [Data 8 textbook readme](https://github.com/data-8/textbook/blob/gh-pages/README.md).

The following sections show you how to set up your course website.

### Prepare your computer

First off, take these step to prepare your computer for adapting the Data 8
materials:

1. Create a folder for your data 8 deployment. We'll deal with a few repositories
   for course content, so it's easiest if they all exist under one folder. Change
   directories into this folder. e.g.:

       cd data8/

2. Make sure that you have `git` installed on your computer.
3. If you'd like to preview changes to your site locally before pushing to GitHub,
   install Ruby and Jekyll by [following the Jekyll install instructions](https://jekyllrb.com/docs/installation/)

Now you're ready to set up your course material!

### Prepare your course textbook repository

You'll use a tool called Jekyll to host your course content. Jekyll is a static
website generator - meaning that you can use static files (like markdown) to
generate the HTML needed for a website. Jekyll is used by GitHub pages, which
means that you can automatically host a website online using GitHub and Jekyll.

To get your own version of this course site, take the following steps:

1. Fork the [data-8 textbook repository](https://github.com/data-8/textbook/) on github.
2. Clone this fork to your computer.

       git clone https://github.com/<YOUR-USERNAME>/textbook/

3. Change directories to the root of your data 8 template repository

       cd textbook

4. (optional) If you'd like to build the site locally before pushing to github,
   install the dependencies needed to build the site.

       bundle install

### Configure your course site for your JupyterHub

You should now have all of the dependencies needed to build your course site.

1. In the `textbook/` repository, there is a file called `_config.yml`.
   This contains the configuration for your course site. You can modify many things
   in here, such as the name and URL of your course website. Update all of
   the relevant fields for your course. In particular, see the following step...
2. Update the fields for your JupyterHub and textbook repository. These are the
   following fields:

     * `hub_url` is the URL for your JupyterHub. It should be a string.
     * `textbook_repo_org` is the organization for the textbook you'll be using. You should
       update this to `<YOUR-USERNAME>`.
     * `hub_type` determines whether interact links point to `mybinder.org`, a free web
       service to host temporary user sessions, or to the URL of a JupyterHub.
       Since you're hosting your course with a JupyterHub, set this parameter to "jupyterhub"

Update these fields, and you should then be ready to build the site.

#### Optional configuration fields

You may optionally change the following fields:

* `textbook_only` - setting this to "false" will include a generic course template along
  with your textbook. This lets you include information like a course syllabus, announcements,
  etc at a single URL. Only use this if you're relatively familiar with (or are willing to learn)
  how Jekyll websites work.
* `use_jupyterlab` - setting this to "true" will cause interact links to launch a JupyterLab session
  after being clicked. Make sure that you've got JupyterLab installed on your JupyterHub!

### Push changes to your site

Now that you've configured the site, take the following steps to see your changes in action.

1. Commit and push your changes to your fork of the repository.
2. Confirm that `gh-pages` site-building is enabled.

   From your GitHub repository, click `Settings` then scroll down to the
   `GitHub Pages` section. You should see the message `Your site is published at <YOUR-URL>`.
3. Go to the URL listed at `<YOUR-URL>` and you should see your live site.

## Preview your built site (optional)

You can also preview your built site using Jekyll on your computer.
To do this, take the following steps:

1. Ensure that Jekyll and Ruby are installed.
2. Ensure that your notebooks have been converted to markdown, there should be a
   collection of them in `_chapters`
3. Run the Jekyll site preview command:

       bundle exec jekyll serve

Jekyll will then build your course, and start a server that runs your course
content. Wait for the following text to appear:

    Server address: http://127.0.0.1:4000/

This is the location of your local demo for the course. Go to that URL in the
browser, and you should see a functioning course website. The textbook interact
links should point to the JupyterHub URL you've specified in `_config.yml`.

## Update your textbook with the latest version

If you believe that the Data 8 textbook has been modified, and you'd like to incorporate
these changes into your own version of the textbook, take the following steps:

1. Add the `data-8` repository as a "remote" on your local git repo:

       git remote add upstream https://github.com/data-8/textbook

   This will fetch the latest version of the `data-8` copy of the textbook.
   To update your local copy, you have two options:
  * **Pull in the latest changes from the remote repository** into your local `gh-pages` branch:

         git pull upstream gh-pages

    This will attempt to pull in all changes from the remote repository, and shouldn't be
    a problem as long as you haven't changed too much in your local repo.

    You might get merge conflicts, in which case you should address them if possible!
    In general, the only files that you should need
    to update are those in `_chapters/` and `notebooks/`.  If there is too much
    in the merge conflict, try the following step:

  * **`git cherry-pick` new changes**. If you know exactly which changes you want to
    incorporate from the "master" version of the textbook, you can use `git cherry-pick` to
    only apply the changes from a specific commit into your repo.

    Once you know the commit hash that you want to apply, simply run the following command:

        git cherry-pick <COMMIT-HASH>

    [Here's a list of the latest commits in the textbook](https://github.com/data-8/textbook/commits/gh-pages) for reference.

2. Push changes to your github repository:

       git push

Note that the branch on which the textbook exists is `gh-pages`, not `master`. This should
be the same for your copy of the textbook as well.

## Next step

Now that you've got your own working version of the textbook, it's time to
[connect your course with the homeworks, labs, and other course material in Data 8](connect_labs_and_homework.md).
