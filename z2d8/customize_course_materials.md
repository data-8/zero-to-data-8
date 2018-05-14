# Customizing your class materials

The materials covered thus far assume you'd like to run your course using
the same materials covered in Data 8. However, sometimes it makes sense to
modify or adapt these materials for your own course. This page covers how
to adapt the materials for use with your Data 8 course website.

## Customizing the Data 8 textbook

The Data 8 textbook is written using Jupyter Notebooks, which store
all of the textbook content. These notebooks are converted to HTML, and then hosted
online. The following steps show how you can modify these notebooks, convert
them to HTML, and then use them in your course.

### Download the textbook repository

The raw materials for the textbook can be found at
https://github.com/data-8/textbook. To get your version of the textbook,
use the following steps:

1. Fork the Data 8 textbook repository on GitHub, and clone it to your computer.
2. Familiarize yourself with the textbook materials. Here's a general rundown:

     * `notebooks/` contains the Jupyter Notebooks that contain all the course
       material. This is the folder where you'll make edits.
     * `chapters/` contains a collection of Markdown files that define the
       page title and structure of the textbook. These embed the HTML that is
       generated from `notebooks/`.
     * `notebooks-html/` contains HTML that is *generated* from the Jupyter Notebooks
       for the final site.
     * `notebooks-images/` contains images *generated* for the content in `notebooks-html/`.

You may use this textbook in your own version of Data 8. There is some
setup you'll need to do in order to adapt the materials for your course

### Modify the textbook

Now that you have your own local copy of the Data 8 textbook, you can make
any modifications that you'd like. Generally, you should only modify the
Jupyter Notebooks in `notebooks/`, as this is where most course content lives.

Any changes to those notebooks will result in changes to the HTML files once
they are built. To re-build those HTML files, see the next section.

### Build the HTML for the textbook

This section covers how to prepare the HTML for your version of the textbook.

1. After you have forked the textbook, cloned it to your computer, and made the
  necessary changes to it, then:
2. Navigate to the root of the repository for your version of the Data 8 textbook
3. Run `make notebooks` to generate HTML you can use with your course site.
4. An HTML version will be created for each notebook, and placed in the folder `notebooks-html/`.
   New images will be placed in `notebooks-images/`
5. Commit these changed notebooks (and any other changes you've made) to the git repository.
6. Push the changes up to your GitHub repository, e.g.:

      git push origin gh-pages

7. Connect your changed textbook HTML files to your course template repository.
   To do so, see the next section.

### Connect your modified textbook to your course website

Finally, we need to connect your modified version of the textbook with the course
website you've set up. To do that, take the following steps:

1. In the textbook repository, make sure that the content in `notebooks-html/`
   and `notebooks-images/` is correct. If not, see the previous section on
   building the HTML for your modified textbook.
2. In the course template repository, navigate to the `scripts/` directory.
3. Run the script `convert_data8_textbook.py`. This takes two arguments. The
   first is the path to your textbook folder. The second is the path to your
   course template folder. Here's an example of its usage:

       python convert_data8_textbook.py path/data8/textbook/ path/to/data8/data8-template/

Running the above script will copy over all the built textbook materials into your
course template repository, and will make some modifications needed in
order to work with Jekyll. You can then re-build your Jekyll website to demo
the changes, or upload it to GitHub to see it live.
