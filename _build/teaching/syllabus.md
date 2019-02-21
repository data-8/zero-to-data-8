---
title: 'The Data 8 Course Syllabus'
prev_page:
  url: /teaching/inspiration
  title: 'Inspiration for Data 8 Pedagogy'
next_page:
  url: /misc/README
  title: 'Extra and miscellaneous information'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Course structure

The following is a general description of the course structure for Data 8.
It is a reflection of the content that is covered in the Data 8
textbook, which is freely available at the following link:

https://www.inferentialthinking.com/

The following sections describe some of the major takeaways that students
should learn in the class. Remember, we assume almost *no programming*,
*no statistics*, and *no math* beyond a standard high-school level.

## Conceptual understanding of uncertainty and causality

While much of the technical pieces focus on enabling students to practice
specific technical skills (like programming), it is crucial that those skills
be learned in order to solidify a high-level understanding of how data, statistics,
and inference are inter-related. For example, see
[Chapter 2: Causality and Experiments](https://www.inferentialthinking.com/chapters/02/causality-and-experiments.html)
from the Data 8 textbook.

Below are a few high-level concepts that students should come away with:

* Causality is super important at a conceptual level
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

* data types, structures, tables, etc)
* Programming fundamentals *in the context of data*.
* Start with Data Types and "Tables".
    * Mention a few common data types, e.g. "strings" and cover some methods associated with them - use this to talk about how we can do unique things w/ a string's methods that are unique to its properties
* Because the core point of the course is "data"
* Most data is structured in tables so they talk about it early
* Now talk about functions just before visualization
* *intentionally don't talk about "objects" very much* - in general use functions that take other things as inputs, don't talk about OOP, punt that to a later class. They do mention "methods" earlier on with data types, but not a ton.
* Visualizations - charts, histograms, etc
* Now more complex operations with tables (grouping / joining / etc). *how do you answer datascience questions given the table you have*.
* At this point (week 4) we are already asking / answering specific questions about data using the tools that we have.
* During visualization section, tie it back to the idea of "what is this data representing?" Is it being truthful to the data?

## Statistics, sampling, and hypothesis testing

Randomness and statistics is a core component of data science, and Data 8
has a heavy emphasis on both. Of particular importance is that students come
away with an appreciation for the importance of knowing the sampling method
used to generate data, as well as an understanding for how statistics can
be used (and mis-used) to understand a dataset given an often limited number
of data points.

Below are some statistics fundamentals that students come away with:

* Begin with iteration in the context of probability...begin with flipping a coin
* "for" loops etc are covered in the context of a coin flipping simulation
* Goal is "how do you calculate the probability of an event happening, how do you manipulate your Tables to do this?"
* Next is sampling - how do you take a sample from a table, and use that sample to understand particular statistics about it.
* At each step of this, students are actually *doing* sampling, then visualizing distributions, etc
* Next is statistics - basically, looking at the samples that we took in the previous section
* Final question is "given two samples, are they from the same distribution or not?"

## Inference, prediction, and models

While statistics describe a dataset, they do not inherently make *predictions*
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

* Correlation in the context of a model. Linear regression + least squares.
* Inference - what does a regression line really mean?
* Combine this with the previous section with a confidence interval on the regression line
* Have students write the function to perform these regression lines
* Now classification (aka, advanced prediction)
    * Classify movies as action or romance, do this as a brief introduction to machine learning
    * Some simple algorithms for classification, e.g. k-nearest neighbors

## Comparing distributions

Once students learn the various steps that go into statistically describing a
single dataset, Data 8 covers how to make comparisons *between* datasets. This
is a crucial part of most scientific analysis, as well as in industry data
analytics (e.g., in A/B testing). Data 8 covers comparisons between distributions
as an advanced case of the material that has been covered above.

Below are some fundamentals for comparing two distributions that students come away with:

* Take the previous point one step further: with what confidence can we say if two samples are from the same distribution or not?
* Next is bootstrapping and confidence intervals - doing all of this with random sampling and coding. Students are doing all of this with notebooks etc.
* Now we talk about bias and variance, statistics about statistics (e.g. variability of sample mean)
* Finally, designing experiments and actually interpreting the above (chebychev's stuff + the CLT)


## After the class
* The assumption is that for many people this is the only experience they have with data science
* Others who want to go further have a clear foundation that they can use to go further
