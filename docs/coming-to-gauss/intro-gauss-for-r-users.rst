
Introduction to GAUSS for R Users
=================================

R and GAUSS are both used for statistical computing, but they approach data differently. This guide helps R users translate their workflows to GAUSS.

.. note::

    This guide is written for GAUSS 26.

What Sets GAUSS Apart
---------------------

- **Compiled speed, matrix-first**: Highly optimized BLAS throughout. Matrices are the native type, not a secondary data structure.
- **One way to do things**: No choosing between 5 packages for the same task. Stable API, consistent conventions.
- **Dataframes that are matrices**: Named columns and types, but you can do matrix algebra directly on them—no conversion step.
- **Stability**: No breaking changes between versions. Code runs for decades without dependency updates.

Key Conceptual Differences
--------------------------

+-------------------+---------------------------+---------------------------+
| Concept           | R                         | GAUSS                     |
+===================+===========================+===========================+
| Data storage      | data.frame, tibble        | dataframe, matrix         |
+-------------------+---------------------------+---------------------------+
| Indexing          | 1-based                   | 1-based (same)            |
+-------------------+---------------------------+---------------------------+
| Missing values    | ``NA``                    | ``.`` (dot)               |
+-------------------+---------------------------+---------------------------+
| Vectors           | First-class type          | Column matrices           |
+-------------------+---------------------------+---------------------------+
| Assignment        | ``<-`` or ``=``           | ``=`` only                |
+-------------------+---------------------------+---------------------------+
| Statement end     | Optional ``;``            | Required ``;``            |
+-------------------+---------------------------+---------------------------+
| String concat     | ``paste()``               | ``$+``                    |
+-------------------+---------------------------+---------------------------+

Data Frames
-----------

R's data.frame and GAUSS dataframes are similar—tabular data with named columns of different types.

**Creating:**

.. code-block:: r

    # R
    df <- data.frame(
        name = c("Alice", "Bob", "Charlie"),
        age = c(25, 30, 35),
        score = c(85.5, 92.0, 78.5)
    )

::

    // GAUSS
    name = "Alice" $| "Bob" $| "Charlie";
    age = { 25, 30, 35 };
    score = { 85.5, 92.0, 78.5 };

    df = asDF(age ~ score, "age", "score");
    // Note: asDF creates a dataframe from numeric matrices.
    // String arrays like 'name' are added separately with dfname.

**Loading from CSV:**

.. code-block:: r

    # R
    df <- read.csv("data.csv")
    # or
    df <- read_csv("data.csv")  # tidyverse

::

    // GAUSS
    df = loadd("data.csv");

**Viewing:**

.. code-block:: r

    # R
    head(df)
    str(df)
    names(df)

::

    // GAUSS
    print df[1:6, .];           // First 6 rows
    print rows(df) cols(df);    // Dimensions
    print getcolnames(df)';     // Column names

Column Selection
----------------

.. code-block:: r

    # R
    df$price              # By name
    df[, "price"]         # By name
    df[, 3]               # By position
    df[, c("a", "b")]     # Multiple columns

::

    // GAUSS
    df[., "price"];       // By name
    df[., "price"];       // Same
    df[., 3];             // By position
    df[., "a" "b"];       // Multiple columns (space-separated)

Row Selection
-------------

.. code-block:: r

    # R
    df[1:5, ]             # First 5 rows
    df[df$age > 30, ]     # Filter by condition
    df[c(1, 3, 5), ]      # Specific rows

::

    // GAUSS
    df[1:5, .];           // First 5 rows
    df[df[., "age"] .> 30, .];  // Filter by condition
    df[1|3|5, .];         // Specific rows (use | to concatenate indices)

Note: In GAUSS, use ``.>`` for element-wise comparison, not ``>``.

Data Manipulation
-----------------

**Creating new columns:**

.. code-block:: r

    # R
    df$new_col <- df$a + df$b
    # or (dplyr)
    df <- df %>% mutate(new_col = a + b)

::

    // GAUSS
    new_col = df[., "a"] + df[., "b"];
    df = df ~ asDF(new_col, "new_col");

**Sorting:**

.. code-block:: r

    # R
    df[order(df$age), ]
    # or (dplyr)
    df %>% arrange(age)

::

    // GAUSS
    df = sortc(df, "age");

**Filtering:**

.. code-block:: r

    # R
    df[df$age > 30, ]
    # or (dplyr)
    df %>% filter(age > 30)

::

    // GAUSS
    mask = df[., "age"] .> 30;
    df_filtered = selif(df, mask);

**Group operations:**

.. code-block:: r

    # R (dplyr)
    df %>%
        group_by(category) %>%
        summarize(mean_val = mean(value))

::

    // GAUSS
    // Use aggregate functions
    result = aggregate(df, "mean", "category");

Statistics
----------

.. code-block:: r

    # R
    mean(x)
    sd(x)
    sum(x)
    min(x)
    max(x)
    median(x)
    var(x)
    cor(x, y)

::

    // GAUSS
    meanc(x);     // Column mean
    stdc(x);      // Column std dev
    sumc(x);      // Column sum
    minc(x);      // Column min
    maxc(x);      // Column max
    median(x);    // Median
    vcx(x);       // Variance-covariance
    corrx(x~y);   // Correlation matrix

The ``c`` suffix means "column-wise" operation.

Linear Regression
-----------------

.. code-block:: r

    # R
    model <- lm(y ~ x1 + x2, data = df)
    summary(model)

::

    // GAUSS
    call olsmt(df, "y ~ x1 + x2");

The output is displayed automatically with coefficients, standard errors, t-values, R-squared, etc.

**Accessing results:**

.. code-block:: r

    # R
    coef(model)
    residuals(model)
    fitted(model)

::

    // GAUSS
    struct olsmtOut oOut;
    oOut = olsmt(df, "y ~ x1 + x2");

    print oOut.coefficients;
    print oOut.residuals;
    print oOut.fitted;

Matrices
--------

R has matrices, but vectors are more common. GAUSS is matrix-first.

.. code-block:: r

    # R
    A <- matrix(c(1,2,3,4,5,6), nrow=2, ncol=3, byrow=TRUE)

::

    // GAUSS
    A = { 1 2 3, 4 5 6 };

**Operations:**

.. code-block:: r

    # R
    A %*% B       # Matrix multiplication
    A * B         # Element-wise
    t(A)          # Transpose
    solve(A)      # Inverse
    solve(A, b)   # Solve Ax = b

::

    // GAUSS
    A * B;        // Matrix multiplication
    A .* B;       // Element-wise
    A';           // Transpose
    inv(A);       // Inverse
    b / A;        // Solve Ax = b

**Note:** In GAUSS, ``*`` is matrix multiplication by default. Use ``.*`` for element-wise.

Apply Functions
---------------

R's ``apply`` family has GAUSS equivalents:

.. code-block:: r

    # R
    apply(X, 1, mean)   # Row means
    apply(X, 2, mean)   # Column means
    sapply(list, func)

::

    // GAUSS
    meanr(X);           // Row means (meanr = mean row)
    meanc(X);           // Column means (meanc = mean column)
    // Custom functions use loops or matrix operations

Loops
-----

.. code-block:: r

    # R
    for (i in 1:10) {
        print(i)
    }

::

    // GAUSS
    for i (1, 10, 1);
        print i;
    endfor;

GAUSS for loop syntax: ``for var (start, end, increment);``

Functions
---------

.. code-block:: r

    # R
    my_func <- function(x, y) {
        result <- x + y
        return(result)
    }

::

    // GAUSS
    proc (1) = my_func(x, y);
        local result;
        result = x + y;
        retp(result);
    endp;

Key differences:

- ``proc (n) =`` declares n return values
- ``local`` declares local variables
- ``retp()`` returns values
- ``endp`` ends the procedure

Missing Values
--------------

.. code-block:: r

    # R
    is.na(x)
    na.omit(df)
    x[!is.na(x)]

::

    // GAUSS
    ismiss(x);            // Check for missing
    packr(df);            // Remove rows with missing
    delif(x, ismiss(x));  // Select non-missing

GAUSS uses ``.`` (dot) for missing values, not ``NA``.

Plotting
--------

.. code-block:: r

    # R
    plot(x, y)
    hist(x)
    boxplot(x ~ group)

::

    // GAUSS
    plotScatter(x, y);
    plotHist(x, 20);      // 20 bins
    plotBox(data, "value ~ group");

Quick Reference Table
---------------------

+-------------------------+---------------------------+---------------------------+
| Operation               | R                         | GAUSS                     |
+=========================+===========================+===========================+
| Load CSV                | ``read.csv()``            | ``loadd()``               |
+-------------------------+---------------------------+---------------------------+
| Column names            | ``names(df)``             | ``getcolnames(df)``       |
+-------------------------+---------------------------+---------------------------+
| Dimensions              | ``dim(df)``               | ``rows(df)`` ``cols(df)`` |
+-------------------------+---------------------------+---------------------------+
| Select column           | ``df$col``                | ``df[., "col"]``          |
+-------------------------+---------------------------+---------------------------+
| First n rows            | ``head(df, n)``           | ``df[1:n, .]``            |
+-------------------------+---------------------------+---------------------------+
| Filter rows             | ``df[condition, ]``       | ``selif(df, condition)``  |
+-------------------------+---------------------------+---------------------------+
| Sort                    | ``df[order(df$x), ]``     | ``sortc(df, "x")``        |
+-------------------------+---------------------------+---------------------------+
| Column mean             | ``mean(x)``               | ``meanc(x)``              |
+-------------------------+---------------------------+---------------------------+
| Column sum              | ``sum(x)``                | ``sumc(x)``               |
+-------------------------+---------------------------+---------------------------+
| Std deviation           | ``sd(x)``                 | ``stdc(x)``               |
+-------------------------+---------------------------+---------------------------+
| Linear model            | ``lm(y ~ x)``             | ``olsmt(df, "y ~ x")``    |
+-------------------------+---------------------------+---------------------------+
| Matrix multiply         | ``A %*% B``               | ``A * B``                 |
+-------------------------+---------------------------+---------------------------+
| Element-wise            | ``A * B``                 | ``A .* B``                |
+-------------------------+---------------------------+---------------------------+
| Transpose               | ``t(A)``                  | ``A'``                    |
+-------------------------+---------------------------+---------------------------+
| Missing check           | ``is.na(x)``              | ``ismiss(x)``             |
+-------------------------+---------------------------+---------------------------+
| Remove missing          | ``na.omit(df)``           | ``packr(df)``             |
+-------------------------+---------------------------+---------------------------+
| String concat           | ``paste(a, b)``           | ``a $+ b``                |
+-------------------------+---------------------------+---------------------------+

Common Gotchas
--------------

1. **Semicolons required.** Every statement ends with ``;``

2. **Matrix vs element-wise.** ``*`` is matrix multiplication, ``.*`` is element-wise (opposite of R!)

3. **Assignment.** Use ``=`` not ``<-``

4. **All rows/columns.** Use ``.`` not ``:`` (e.g., ``df[., 1]`` not ``df[, 1]``)

5. **Missing values.** Use ``.`` not ``NA``

6. **String quotes.** Only double quotes ``"string"`` work

7. **No piping.** No ``%>%`` or ``|>`` — use nested calls or intermediate variables

What's Next?
------------

- :doc:`../getting-started/quickstart` — General GAUSS introduction
- :doc:`../data-management` — Data import, export, manipulation
- :doc:`intro-gauss-for-stata-users` — Similar transition guide

.. seealso::

    :func:`loadd`, :func:`olsmt`, :func:`meanc`, :func:`selif`, :func:`sortc`
