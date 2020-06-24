# The `datascience` Package

The `datascience` package is an open source Python package that helps make programming more accessible to all students, regardless of background. As a pedagogical aid, the package is designed to help students more intuitively conduct data science techniques without first spending considerable time directly learning more complex tools such as `pandas` or `matplotlib`. At Berkeley, these other packages are introduced in further upper-division coursework such as Data 100.

## Technical details

The `datascience` package was built with the main goal to teach students about working with tables and visualizations in an introductory data science setting. It was inspired by techniques in SQL, `pandas`, and R data frames, and follows a more natural langauge programming design to have a more intuitive way in syntax.

The package is built on built-in Python data structures, with several dependencies:

- `NumPy`: a tool for numerical computing and linear algebra. The `datascience` package relies on `numpy` arrays as its primary data structure; for example, each column in `datascience` Table objects are `numpy` arrays. Often, many `numpy` functions are also separtely introduced in the course, such as `np.mean` or `np.append`.
- `SciPy`: a set of tools for scientific computing.  The `minimize` function, used to minimize RMSE, uses the `optimize` module from `scipy`.
- `Matplotlib`: a tool for visualization. Plotting is directly done in `datascience` by calling plotting functions on Table objects. Notably, tweaking plots such as renaming titles or adjusting axis shape are abstracted away from students.
- `pandas`: the more industry standard tool for data manipulation and analysis. Although `pandas` is not a significant dependency, `datascience` supports conversion between its Table objects and `pandas` dataframes.

The `datascience` python package was written by Berkeley professors John DeNero and David Culler, as well as students Sam Lau and Alvin Wan. The full documentation to the `datascience` package can be found [here](http://data8.org/datascience/), but students typically only need the [Python Reference Guide](http://data8.org/sp20/python-reference.html) for all the functions that are used widely in Data 8.

## Pedagogical Choices

One large barrier to entry in doing data science for many students is the coding knowledge required. Since Data 8 was designed to be highly accessible to students of all backgrounds, the `datascience` package was thus created to help make the programming part of the course more accessible to students with no coding background by removing syntax complexities. However, this decision comes with a profound trade-off: the package loses computational flexibility and power for increased ease of understanding and usage compared to industry-standard tools such as `pandas`. This trade-off was acceptable for teaching Data 8, as datasets and their associated computation are typically not too large (<100 MB), and the computational flexibility required is limited to within the scope of the course.

Overall, Data 8 emphasizes developing computational thinking skills over details in the specific syntax. This training allows students to more seamlessly transition to other more complex packages after Data 8.

One limitation from using the `datascience` package is that it does not support a wide range of data cleaning procedures. Data 8 abstracts away methods in data cleaning, which will instead be taught in Data 100. As such, students typically receive well-formed data without missing values in Data 8. However, if you plan on placing a larger focus data cleaning or more advanced data manipulation procedures in your course, using `pandas` may perhaps be more appropriate.
