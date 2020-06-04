# Zero to Data 8

This repository hosts the content and website for Zero to Data 8,
the guide to deploying your own Data 8 course infrastructure.

All of the content resides in `content/` and is hosted online
at `data8.org/zero-to-data-8`.

## Install software to build the book

Building this book requires the latest beta version of Jupyter Book. You can
install it locally here:

```
pip install -U "jupyter-book>=0.7.0b"
```

See [the jupyter book documentation](https://jupyterbook.org) for more information.

## To make changes to this book

1. Edit the files in `content/` that you wish to change. If you add a **new**
   file, make sure to add a new entry for it in `_toc.yml`.
2. Run `jupyter-book build .`. This will update the book's built markdown files.
3. Push to github.

That's it!
