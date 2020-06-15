# Creating Data 8 Assignments

Assignments in Data 8 are created in OK format using a tool called [jAssign](https://github.com/okpy/jassign). jAssign parses a master notebook containing questions, solutions, and tests and creates two disribution directories: one with solutions and all tests for autograders and a second with no solutions and only public tests for students. jAssign also includes utilities to generate filtered LaTeX PDFs of students' notebooks to ease the process of manually grading written questions.

## Writing Your Own Assignments

jAssign makes writing your own assignments very easy by providing a simple format for a master notebook. Writing narrative/filler cells is as normal. To create a question, add a YAML-formatted metadata block to the end of the Markdown cell for that question to define some configurations for it. An example question cell might contain:

````
Question 1.1: Fill in the infinite generator `fib` below that yields the Fibonacci sequence.

```
BEGIN QUESTION
name: q1_1
manual: false
points: 1
```
````

The `BEGIN QUESTION` block contains the mandatory parameter `name` and two optional parameters, `manual` and `points`, whose default values are in the block above. Immediately after the question cell should be a solution cell. Using specially-formatted Python comments, jAssign can parse the solution cell and replace lines with ellipsis or other user-defined prompts (this behavior is described in more detail in the jAssign docs, linked below). After the solution cell come zero or more test cells, denoted by a `# TEST` or `# HIDDEN TEST` line at the top of the cell. These cells will have their outputs parsed by jAssign to generate the ok-formatted test files needed for autograding. jAssigns [getting started guide](https://github.com/okpy/jassign#getting-started) describes how to call jAssign to parse the notebook.

Once you have run jAssign, you're ready to distribute your assignment to students! The `student` subdirectoy of your output directory will contain the version of the notebook for students (with solutions removed and only public tests) and the `autograder` subdirectory the version *with* solutions and hidden tests.

For more information, check out the [jAssign documentation](https://github.com/okpy/jassign/tree/master/docs).

### Best Practices for Autograder Tests

There are several nuances to writing good autograder tests. While jAssign does abstract away the doctest format required for writing them from scratch, there are some details that shouldn't be overlooked. [Writing Autograder Tests](https://autograder-tests.rtfd.io) is a guide on best practices for writing Pythonic autograder tests and will help you think through the best ways to write tests in your notebook.

## Other Assignment Development Tools

While Data 8 makes us of OkPy and jAssign, there are other autograding tools that UC Berkeley uses, including [Otter Grader](../tech/autograding/otter.md). Otter includes a forked version of jAssign called Otter Assign that functions similar to jAssign (and is even backwards-compatible with its notebook format). For more information about Otter Assign, see the [Otter documentation](https://otter-grader.rtfd.io).
