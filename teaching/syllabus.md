# Course structure
## Conceptual ideas + causality
* Causality is super important at a conceptual level
* Where did you get your data from?
* Is it a controlled randomized study or observational data.
* What is cause and effect? In the context of data?

## Programming fundamentals
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

## Statistics and sampling
* Begin with iteration in the context of probability...begin with flipping a coin
* "for" loops etc are covered in the context of a coin flipping simulation
* Goal is "how do you calculate the probability of an event happening, how do you manipulate your Tables to do this?"
* Next is sampling - how do you take a sample from a table, and use that sample to understand particular statistics about it.
* At each step of this, students are actually *doing* sampling, then visualizing distributions, etc
* Next is statistics - basically, looking at the samples that we took in the previous section
* Final question is "given two samples, are they from the same distribution or not?"


## Comparing distributions Comparing between distributions + inference + confidence
* Take the previous point one step further: with what confidence can we say if two samples are from the same distribution or not?
* Next is bootstrapping and confidence intervals - doing all of this with random sampling and coding. Students are doing all of this with notebooks etc.
* Now we talk about bias and variance, statistics about statistics (e.g. variability of sample mean)
* Finally, designing experiments and actually interpreting the above (chebychev's stuff + the CLT)

## Prediction and models
* Correlation in the context of a model. Linear regression + least squares.
* Inference - what does a regression line really mean?
* Combine this with the previous section with a confidence interval on the regression line
* Have students write the function to perform these regression lines
* Now classification (aka, advanced prediction)
    * Classify movies as action or romance, do this as a brief introduction to machine learning
    * Some simple algorithms for classification, e.g. k-nearest neighbors

## Case studies
* A few real-world datasets where they go from start to finish with that dataset, using the tools from before to answer questions.

## Exercises and student work
* The exercises are generally the same concepts but with a different dataset, they ask students to create new functions etc.
* Lots of different kinds of datasets they use with exercises


## After the class
* The assumption is that for many people this is the only experience they have with data science
* Others who want to go further have a clear foundation that they can use to go further
