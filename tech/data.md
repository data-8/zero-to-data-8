# Handling Data with the DataHub

Most Data Science courses require some kind of external data
set in order to teach their materials. This page describes how
data is handled on the DataHub and in student environments.


## Small-enough datasets

As Data 8 is an introductory course, it can generally make due
with datasets that can be downloaded on-the-fly within a student
session. The `datascience` packages uses a helper function called
`read_url` that loads in a dataset that exists on the web. In
addition, the [Data 8 Textbook](https://inferentialthinking.com) has
several datasets stored alongside chapter material.

For example, in Chapter 3, students perform some [basic text analysis](https://www.inferentialthinking.com/chapters/01/3/plotting-the-classics.html)
on the full text of "Huckleberry Fin". This dataset lives in the Data 8 textbook repository at the following URL:

https://www.inferentialthinking.com/chapters/01/3/huck_finn.txt

As such, students can download and load this data interactively with
the following commands:

```python
huck_finn_url = 'https://www.inferentialthinking.com/chapters/01/3/huck_finn.txt'
huck_finn_text = read_url(huck_finn_url)
```

Many datasets are loaded in this was in Data 8 (so long as they don't
take long to load).

## Larger datasets

While some data is small enough that it can be downloaded
interactively, other data sets are large enough that they
are better-off shared between students. Data 8 shares these datasets on a
folder that all students have read-only access to. It is slower to update
and modify this data, but much more efficient than requiring students to
download it and store their own copy.
