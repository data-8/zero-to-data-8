# Using the Data 8 textbook

This page covers how to connect your course with the Data 8 textbook,
either via using the one hosted at [www.inferentialthinking.com](https://www.inferentialthinking.com)
or by customizing your own.

## The Data 8 Textbook

The [online Data 8 textbook](https://www.inferentialthinking.com/) is
built using a site generation engine called [Jekyll](https://jekyllrb.com/),
and hosted online with the free [GitHub Pages](https://pages.github.com/) service.

For a short explanation of the structure / relevant files / etc of the
Data 8 textbook, see the [Data 8 textbook readme](https://github.com/data-8/textbook/blob/gh-pages/README.md).

You have two options for using the Data 8 textbook:

### Use the version of the textbook at [inferentialthinking.com](https://www.inferentialthinking.com)

The textbook hosted online should be suitable for most courses. The "interact" links
at the top of each page point to [mybinder.org](https://mybinder.org), a public
service that lets users interact with material online. If you wish, you may
send students links to this textbook for your course.

**To override this textbook's interact links to point to your JupyterHub** you
may link to the textbook with an optional REST parameter at the end of the url.
Putting `?hub=<your-jupyterhub-url>` at the end of a link to `inferentialthinking.com`
will do the following:

* The interact button will now point to the URL provided.
* A small message will be displayed telling the user where "interact" points.
* Internal links on the page will also now contain this URL.

**Note: users need to supply this URL parameter each time they visit
`inferentialthinking.com`.** For example, you might instruct users to **only**
access the online textbook by clicking a link that you distribute in your
syllabus that contains the `hub=` parameter in it.

### Customize the textbook for your course

Alternatively, you may wish to
customize the textbook for your own course. The most common reason to do so is
in order to make "interact" links point to your JupyterHub. This way, students
can interact with textbook material in their own JupyterHub sessions, and their
work will persist over time.

To do so, follow the steps in the [customizing your textbook](../misc/custom_textbook.md)
guide.

## Next step

Now that you've got your own working version of the textbook, let's discuss
some [course logistics](course_logistics.md)
