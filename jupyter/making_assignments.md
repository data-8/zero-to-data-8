# Creating Data 8 Assignments

Assignments in Data 8 are created in [Otter-Grader-based](https://otter-grader.readthedocs.io/en/v4.4.1/) format. Otter-Grader parses a parent notebook containing questions, solutions, and tests to creates two distribution directories: one with solutions and all tests for automatic grading and a second with no solutions and only public tests for students. Otter-Grader also includes utilities to generate filtered LaTeX PDFs of students' notebooks to ease the process of manually grading written questions.

## Writing Your Own Assignments

Otter-Grader makes writing your own assignments very easy by providing tools to parse simple markdown yaml-format in a parent notebook. To create a question, add a YAML-formatted metadata block to the end of the Markdown cell for that question to define some configurations for it. An example question cell might contain:

```{text}
# BEGIN QUESTION
name: q1
points: 2
Question 1. Write a function called sieve that takes in a positive integer n and returns a set of the prime numbers less than or equal to n. Use the Sieve of Eratosthenes to find the primes.
```

The `BEGIN QUESTION` block contains the mandatory parameter `name` and two optional parameters, `manual` and `points`. 


Immediately after the question cell should be a solution cell.
```
# BEGIN SOLUTION
def sieve(n):
    """
    Generate a set of prime numbers less than or equal to a positive integer.
    """
    # BEGIN SOLUTION
    is_prime = [True for _ in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if is_prime[p]:
            for i in range(p ** 2, n + 1, p):
                is_prime[i] = False
        p += 1

    is_prime[0]= False
    is_prime[1]= False

    return set(i for i in range(n + 1) if is_prime[i])
    # END SOLUTION
# END SOLUTION
```

 Using specially-formatted Python comments, otter-grader can parse the solution cell and replace lines with ellipsis or other user-defined prompts (this behavior is described in more detail in the otter-grader docs, linked below). 
 
 After the solution cell comes zero or more test cells, denoted by a beginning `# BEGIN TESTS` annotation, finishing with an ending `# END TESTS` annotation, and between these two lines functions that test the code. These functions' names begin with `test_` and are marked as  `# HIDDEN` if appropriate. The `# IGNORE` lines provide funcationality for the grader to call the test funcions appropriately.
```
# BEGIN TESTS
def test_low_primes(sieve):
    assert sieve(1) == set()
    assert sieve(2) == {2}
    assert sieve(3) == {2, 3}

test_low_primes(sieve)  # IGNORE
# HIDDEN
def test_higher_primes(sieve):
    assert sieve(20) == {2, 3, 5, 7, 11, 13, 17, 19}
    assert sieve(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

test_higher_primes(sieve)  # IGNORE
# END TESTS
# END QUESTION
```
 
  These cells will have their outputs parsed by otter-grader to generate the otter-formatted test files needed for autograding. The otter-grader docs [tutorial](https://otter-grader.readthedocs.io/en/latest/tutorial.html) describes how to call otter-grader to parse the notebook.

Once you have run otter-grader, you're ready to distribute your assignment to students! The `student` subdirectoy of your output directory will contain the version of the notebook for students (with solutions removed and only public tests) and the `autograder` subdirectory the version *with* solutions and hidden tests.

For more information, check out the [otter-grader documentation](https://otter-grader.readthedocs.io/en/v4.4.1/).

### Best Practices for Autograder Tests

There are several nuances to writing good autograder tests. While Otter-Grader does abstract away the doctest format required for writing them from scratch, there are some details that shouldn't be overlooked. [Writing Autograder Tests](https://autograder-tests.rtfd.io) is a guide on best practices for writing Pythonic autograder tests and will help you think through the best ways to write tests in your notebook.

