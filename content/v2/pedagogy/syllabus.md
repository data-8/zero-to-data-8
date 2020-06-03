# Course structure

The following is a general description of the course structure for Data 8.
It covers how to build your course syllabus and is a reflection of the content that is covered in the Data 8
textbook, which is freely available at the following link:

https://www.inferentialthinking.com/

The following sections describe some of the major takeaways that students
should learn in the class. Data 8 assumes *no programming*,
*no statistics*, and *no math* beyond a standard high-school level.

## Conceptual understanding of uncertainty and causality

A lot of the technical pieces in the course focus on enabling students to practice
specific technical skills (like programming). It is crucial that these skills
be learned in order to solidify a high-level understanding of how data, statistics,
and inference are inter-related. For example, see
[Chapter 2: Causality and Experiments](https://www.inferentialthinking.com/chapters/02/causality-and-experiments.html)
from the Data 8 textbook.

Below are a few high-level concepts that students should come away with:

* A solid understanding of causality on a conceptual level.
* Where did you get your data from?
* Is it a controlled randomized study or observational data.
* What is cause and effect? In the context of data?

## Programming fundamentals

Scripting and interactive computing are the primary ways that we operationalize
the data science methods covered in the course. While it is possible to find
programs that let you carry out various techniques with user-interfaces, Data 8
stresses that programming fundamentals will facilitate learning the analytic
topics and provide a more useful and generic skillset in computational methods.

In Data 8, programming fundamentals are taught *alongside* statistical concepts.
For example, [iteration is taught alongside random sampling](https://www.inferentialthinking.com/chapters/09/2/iteration.html).

Below are some programming fundamentals that students come away with:

* Data types, structures, functions, tables, etc
* Programming fundamentals *in the context of data*.
* How to answer data science questions with the tables you have.
* Complex operations with tables (grouping, joining, etc). 
* How to create visualizations (charts, histograms, etc) and understand what is being represented.


## Statistics, sampling, and hypothesis testing

Randomness and statistics are core components of data science. Data 8
has a heavy emphasis on both. It is particularly important that students come
away with an appreciation for how a sampling method is
used to generate data, as well as an understanding for how statistics can
be used (and mis-used) to understand a dataset given a limited number
of data points.

Below are some statistics fundamentals that students come away with:

* Iteration in the context of probability of an event (e.g probability when flipping a coin)
   * "for" loops etc are covered in the context of a coin flipping simulation
* How to manipulate tables to calculate probability.
* Sampling and empirical distributions - how to make conclusions based on random samples?
* How to compare two samples.

## Inference, prediction, and models

While statistics describe a dataset, it does not inherently make *predictions*
about the underlying distribution from which the data are drawn. Data 8 relies
heavily on bootstrapping and permutation methods in order to make estimations
of error/confidence in parameters derived from the data.

Beyond estimating the value of a model's parameter given limited data, models
are also used to generate *predictions* about the world given a new set of
data. Data 8 treats prediction as an extension of inference. In the same
sense that inference quantifies uncertainty in a model's parameter, we can also
generate uncertainty in predictions given a data point that the model has not
seen before. This is given treatment in the case of regression (models with quantitative outputs)
as well as classification (models with qualitative outputs).

Below are some inference, prediction, and modeling fundamentals that students come away with:

* Correlation in the context of modeling. 
* Linear regression and least squares.
* Regression inference - what does a regression line really mean?
* How to compute confidence integrals of regression lines.
* How to train classifiers with simple algorithms such as k-nearest neighbors
* Brief introduction to machine learning

## Comparing distributions

Once students learn the various steps that go into statistically describing a
single dataset, Data 8 covers how to make comparisons *between* datasets. This
is a crucial part of most scientific analysis, as well as in industry data
analytics (e.g., in A/B testing). Data 8 covers comparisons between distributions
as an advanced case of the material that has been covered above.

Below are some fundamentals for comparing two distributions that students come away with:

* A/B testing - with what confidence can we say if two numerical samples come from the same underlying distribution or not?
* Bootstrapping and confidence intervals 
* Importance of bias and variance of the sample mean
* Statistics about statistics (e.g. variability of sample mean) 
* How to use sample means effectively for inference?
* How to design experiments and intrepret the distributions with Central Limit Theorem, Chebyshev's, etc.


# Building a Course syllabus page

You may use whatever technology you prefer for managing your course and
distributing content. However, we recommend setting up a syllabus page that
is used for distributing interact links and course materials. For an example,
see the structure of the Spring 2020 course syllabus:[http://data8.org/sp20/]

The syllabus has the following structure:

| Date          | Topic | Lecture  | Reading | Assignment
| ------------- | ----- | -------  | ------- | ----------
| Fri 01/24 | Cause and Effect | [Slides](https://docs.google.com/presentation/d/1lSwG_uGwQRL3oGQnmn7aphxYZlzX0G0KHeyNM-cNZb4/edit?usp=sharing) | [Chapter 2](https://www.inferentialthinking.com/chapters/02/causality-and-experiments.html) | [Homework 01](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp20&subPath=materials/sp20/hw/hw01/hw01.ipynb)
| Mon 01/27 | Tables | [Slides](https://docs.google.com/presentation/d/1jn2X5JtbOqOfiBa_QdV2ITw491dhRdxIvKR0bR1tWUk/edit?usp=sharing), [Demos](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp20&subPath=lec/lec03.ipynb), [Video](https://www.youtube.com/watch?v=BW9XcOG8jag) | [Chapter 3](https://www.inferentialthinking.com/chapters/03/programming-in-python.html)| |
| Wed 01/29 | Data Types |  [Slides](https://docs.google.com/presentation/d/1TjU8ismB9qSrWAivDq2HvuYy68sRTE_Q_V3gPcHP0qQ/edit?usp=sharing), [Demos](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp20&subPath=lec/lec04.ipynb), [Video](http://youtube.com/watch?v=F3krVj7GkI0) | [Chapters 4](https://www.inferentialthinking.com/chapters/04/data-types.html), [5](https://www.inferentialthinking.com/chapters/05/sequences.html)| [Lab 02: Table Operations](http://datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/data-8/materials-sp20&subPath=materials/sp20/lab/lab02/lab02.ipynb)

Each row is a lecture, and each column is a type of material you can distribute.
The links in the columns either point to pages on the [course textbook](https://inferentialthinking.com).
or interact links that connect students with the course JupyterHub for distribution of homeworks and labs.

The videos and slides listed above and on the [Data 8 website](http://data8.org/sp20/) are restricted to berkeley.edu addresses. 


## Assignments

Alongside the textbook are several computational homeworks, labs, and projects that let students interact with the
ideas covered in class. They can all be run interactively in the Data 8 environment.

These homework, labs, and project materials are freely available on the semester course repository.
There is a new repository created for each semester of the course, as the materials
tend to evolve over time. For example, here is the repository for the Spring 2020 course:

[https://github.com/data-8/materials-sp20]



