# Connect your hub with the course materials

Now that our JupyterHub has the Data 8 computing environment, it's time to
connect it with the course materials for the class (e.g., lectures, labs, and homeworks).

We'll create your own versions of the course materials used in Data 8, then
host them all in one place using a Jekyll website. We'll cover each step below.

## Prepare your computer

First off, take these step to prepare your computer for adapting the Data 8
materials:

1. Create a folder for your data 8 deployment. We'll deal with a few repositories
   for course content, so it's easiest if they all exist under one folder.
2. Make sure that you have `git` installed on your computer.
3. Install Ruby and Jekyll by [following the Jekyll install instructions](https://jekyllrb.com/docs/installation/)
4. Change into the directory of the Data 8 folder you just created, so that all
   repositories we'll use will exist in this folder.

       cd data8/

Now you're ready to set up your course material!

## The Data 8 Course Website

We've created a _template website_ for your Data 8 course. It contains links
to your version of the textbook, as well as tools for posting the course
syllabus and announcements. A demo version of this site can be found here:

http://predictablynoisy.com/data8-template

This course website comes with a relatively up-to-date version of the
course textbook. The Data 8 textbook is an interactive and open textbook that is used
throughout the class. The entire textbook is available freely online, and
the latest version used by Data 8 is found at https://inferentialthinking.com.
This is the version that's found in `data8-template/`

The following sections show you how to set up your course website. If you'd
like to customize your *own* version of the textbook, see the
[customizing the course material](customize_course_materials.html) section.

### Prepare your course website

You'll use a tool called Jekyll to host your course content. Jekyll is a static
website generator - meaning that you can use static files (like markdown) to
generate the HTML needed for a website. Jekyll is used by GitHub pages, which
means that you can automatically host a website online using GitHub and Jekyll.

To get your own version of this course site, take the following steps:

1. Fork the [data-8 template repository](https://github.com/choldgraf/data8-template/) on github.
2. Clone this fork to your computer.

       git clone https://github.com/<YOUR-USERNAME>/data8-template/

3. Change directories to the root of your data 8 template repository

       cd data8-template

4. Install the dependencies needed to build the site.

       bundle install

### Configure your course site for your JupyterHub

You should now have all of the dependencies needed to build your course site.

1. In the `data8-template/` repository, there is a file called `_config.yml`.
   This contains the configuration for your course site. You can modify many things
   in here, such as the name and URL of your course website. Update all of
   the relevant fields for your course. In particular, see the following step
2. Update the fields for your JupyterHub and textbook repository. These are the
   following fields:

     * `hub-url` is the URL for your JupyterHub. It should be a string.
     * `textbook-url` is the URL for the textbook you'll be using. Generally,
       this is the address of your fork of the textbook. E.g., `https://github.com/<YOUR-USERNAME>/textbook`

Update these fields, and you should then be ready to build the site.

### Build and test your site

You should now be able to build your course website with Jekyll. To do so,
run the following command:

    bundle exec jekyll serve

Jekyll will then build your course, and start a server that runs your course
content. Wait for the following text to appear:

    Server address: http://127.0.0.1:4000/

This is the location of your local demo for the course. Go to that URL in the
browser, and you should see a functioning course website. The textbook interact
links should point to the JupyterHub URL you've specified in `_config.yml`.

### Upload the site to GitHub

Once you've confirmed that your course site builds properly, upload the course
content to GitHub. GitHub treats jekyll websites in a special manner. You'll
be able to run your site for free using GitHub's servers. To do this, take the
following steps:

1. Push any changes you've made in `data8-template/` to your fork of the
   repository on GitHub.

       git push origin master

2. Click on `settings` and scroll down to the `GitHub Pages` section.
3. You should see a green confirmation bar with text like this:

       Your site is published at http:<YOUR-USERNAME>.github.io/data8-template/

4. If you see this, visit `http:<YOUR-USERNAME>.github.io/data8-template/` and
   you should see your live website.

Congratulations, you should now have a fully-functioning course website
hosting your version of the textbook! See the sections to the left for next steps.
