# The Educator's Guide to Technology Infrastructure for Data 8

This online resource serves as a "snapshot" of the Data 8 technology stack, and a guide for others
that wish to adopt a Data 8 classroom environment. For a guide on the *pedagogical* and *curriculum* 
considerations, [there is a separate guide here](../v1/teaching/inspiration).

[comment]: <> (TODO: A reminder to change the link above once the new guide is created and finished.)

## What is Data 8?

[Data 8](http://data8.org/) is a "Foundations in Data Science" course taught for first year students 
at UC Berkeley. It combines principles/skills in statistics, programming, inference, modeling,
hypothesis testing, visualization, and exploration. It provides a foundation in the many fields
encompassed by "data science", and gives students a practical introduction to the field. For a 
more in-depth description of the topics taught, please reference the separate 
[pedagogy guide](../v1/teaching/curriculum).

Creating a data science course from first-principles requires considerable
advances in the technology available to instructors. In creating Data 8, the
development team has worked closely with members of the open-source community,
and has contributed to or adopted many open source projects. The goal driving
development of technology for Data 8 is to *develop an open platform of which
Berkeley happens to be the first user.*

As such, most of these components are freely available to the educational community, and we welcome
others to adopt these tools for their own uses and become contributors to these projects over time.

## Brief Outline

The following is an outline of the technical pieces that go into running Data 8. It is broken down 
by activity/need so that it might be most useful for others hoping to accomplish the same goals.

### JupyterHub

[Quick Link to Jupyterhub Intro](jupyterhub/intro)

Data 8 started with 60 students in Fall 2015, and now has 1350 students as of Spring 2020. 
The course operates on a scale and level of complexity that required several technological 
improvements to our current teaching toolset. The Data 8 team worked closely with various 
open-source projects in order to contribute to tools that are broadly useful.

### Autograding

[Quick Link to Autograding Intro](autograding/intro)

Automating the grading of assignments within a Jupyter environment has been made simpler in recent 
years with the implementation of several open-source software solutions. These strides towards 
automated solutions save professors and instructors the long hours of grading assignments manually. 
This chapter serves as a guide towards choosing one that best fits a course's scale and requirements.