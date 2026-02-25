
Introduction to GAUSS for Python/NumPy Users
============================================

Python (with NumPy/pandas) and GAUSS are both used for numerical computing. This guide helps Python users translate their workflows to GAUSS.

Why Consider GAUSS?
-------------------

Python with NumPy/pandas is the dominant data science stack. GAUSS offers:

- **Speed without setup**: No need to optimize with Cython, Numba, or careful vectorization—GAUSS is already fast
- **Econometrics focus**: Strong built-in support for time series, panel data, discrete choice
- **Stability**: Code runs unchanged for decades, no dependency hell
- **Simplicity**: One environment, not Jupyter + conda + pip + virtual environments

The tradeoff: Python has a larger ecosystem, more packages, and is free.

Key Conceptual Differences
--------------------------

+-------------------+---------------------------+---------------------------+
| Concept           | Python/NumPy              | GAUSS                     |
+===================+===========================+===========================+
| Indexing          | 0-based                   | 1-based                   |
+-------------------+---------------------------+---------------------------+
| Slicing end       | Exclusive ``[0:3]``       | Inclusive ``[1:3]``       |
+-------------------+---------------------------+---------------------------+
| Data type         | ndarray, DataFrame        | matrix, dataframe         |
+-------------------+---------------------------+---------------------------+
| Missing values    | ``np.nan``, ``None``      | ``.`` (dot)               |
+-------------------+---------------------------+---------------------------+
| Matrix multiply   | ``@`` or ``np.dot``       | ``*``                     |
+-------------------+---------------------------+---------------------------+
| Element-wise      | ``*``                     | ``.*``                    |
+-------------------+---------------------------+---------------------------+
| Statement end     | Newline                   | ``;`` required            |
+-------------------+---------------------------+---------------------------+

**Critical:** Python is 0-indexed, GAUSS is 1-indexed. Python slices are half-open ``[start:end)``, GAUSS slices are closed ``[start:end]``.

Array/Matrix Creation
---------------------

.. code-block:: python

    # Python/NumPy
    import numpy as np

    A = np.array([[1, 2, 3],
                  [4, 5, 6]])

    zeros = np.zeros((3, 3))
    ones = np.ones((3, 3))
    identity = np.eye(3)
    rand_uniform = np.random.rand(3, 3)
    rand_normal = np.random.randn(3, 3)

::

    // GAUSS
    A = { 1 2 3,
          4 5 6 };

    zeros_mat = zeros(3, 3);
    ones_mat = ones(3, 3);
    identity = eye(3);
    rand_uniform = rndu(3, 3);
    rand_normal = rndn(3, 3);

**Sequences:**

.. code-block:: python

    # Python/NumPy
    np.arange(1, 6)           # [1, 2, 3, 4, 5]
    np.arange(1, 3, 0.5)      # [1, 1.5, 2, 2.5]
    np.linspace(0, 1, 5)      # 5 points from 0 to 1

::

    // GAUSS
    seqa(1, 1, 5);            // Column: start, increment, count
    seqa(1, 0.5, 4);          // {1, 1.5, 2, 2.5}
    seqa(0, 0.25, 5);         // {0, 0.25, 0.5, 0.75, 1}

Note: ``seqa`` takes (start, increment, count), not (start, stop).

Indexing
--------

**This is the biggest difference.** Python is 0-indexed; GAUSS is 1-indexed.

.. code-block:: python

    # Python/NumPy
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])

    A[0, 0]           # First element: 1
    A[0, :]           # First row
    A[:, 0]           # First column
    A[0:2, :]         # Rows 0 and 1 (not 2!)
    A[-1, :]          # Last row

::

    // GAUSS
    A = { 1 2 3,
          4 5 6 };

    A[1, 1];          // First element: 1
    A[1, .];          // First row
    A[., 1];          // First column
    A[1:2, .];        // Rows 1 and 2 (inclusive!)
    A[rows(A), .];    // Last row

**Key differences:**

- GAUSS uses ``.`` for "all", Python uses ``:``
- GAUSS slices are inclusive: ``A[1:3, .]`` gets rows 1, 2, and 3
- Python slices are half-open: ``A[0:3, :]`` gets rows 0, 1, and 2

Operators
---------

**Matrix vs element-wise is reversed!**

.. code-block:: python

    # Python/NumPy
    A * B             # Element-wise multiplication
    A @ B             # Matrix multiplication
    np.dot(A, B)      # Matrix multiplication (alternative)
    A ** 2            # Element-wise power

::

    // GAUSS
    A .* B;           // Element-wise multiplication
    A * B;            // Matrix multiplication
    A * B;            // (same)
    A .^ 2;           // Element-wise power

**Summary:**

+-------------------+---------------------------+---------------------------+
| Operation         | Python/NumPy              | GAUSS                     |
+===================+===========================+===========================+
| Matrix multiply   | ``@`` or ``np.dot``       | ``*``                     |
+-------------------+---------------------------+---------------------------+
| Element-wise mult | ``*``                     | ``.*``                    |
+-------------------+---------------------------+---------------------------+
| Element-wise div  | ``/``                     | ``./``                    |
+-------------------+---------------------------+---------------------------+
| Element-wise pow  | ``**``                    | ``.^``                    |
+-------------------+---------------------------+---------------------------+

Concatenation
-------------

.. code-block:: python

    # Python/NumPy
    np.hstack([A, B])         # Horizontal
    np.vstack([A, B])         # Vertical
    np.concatenate([A, B], axis=1)  # Horizontal
    np.concatenate([A, B], axis=0)  # Vertical

::

    // GAUSS
    A ~ B;            // Horizontal (tilde)
    A | B;            // Vertical (pipe)

DataFrames / pandas
-------------------

GAUSS dataframes are similar to pandas DataFrames.

**Loading:**

.. code-block:: python

    # Python/pandas
    import pandas as pd
    df = pd.read_csv("data.csv")
    df = pd.read_excel("data.xlsx")

::

    // GAUSS
    df = loadd("data.csv");
    df = loadd("data.xlsx");

**Viewing:**

.. code-block:: python

    # Python/pandas
    df.head()
    df.shape
    df.columns
    df.dtypes

::

    // GAUSS
    print df[1:5, .];
    print rows(df) cols(df);
    print getcolnames(df)';
    // Types inferred from column contents

**Selecting columns:**

.. code-block:: python

    # Python/pandas
    df["price"]
    df[["price", "size"]]
    df.iloc[:, 0]

::

    // GAUSS
    df[., "price"];
    df[., "price" "size"];    // Space-separated names
    df[., 1];

**Filtering:**

.. code-block:: python

    # Python/pandas
    df[df["age"] > 30]
    df.query("age > 30")

::

    // GAUSS
    mask = df[., "age"] .> 30;
    df_filtered = selif(df, mask);

Statistics
----------

.. code-block:: python

    # Python/NumPy
    np.mean(x)
    np.std(x)
    np.sum(x)
    np.min(x)
    np.max(x)

    # Column-wise
    np.mean(X, axis=0)
    np.sum(X, axis=0)

::

    // GAUSS
    meanc(x);     // Column mean (default)
    stdc(x);      // Column std dev
    sumc(x);      // Column sum
    minc(x);      // Column min
    maxc(x);      // Column max

    // Row-wise
    meanr(X);     // meanr = mean row
    sumr(X);      // sumr = sum row

Linear Algebra
--------------

.. code-block:: python

    # Python/NumPy
    np.linalg.inv(A)
    np.linalg.det(A)
    np.linalg.eig(A)
    np.linalg.svd(A)
    np.linalg.cholesky(A)
    np.linalg.solve(A, b)

::

    // GAUSS
    inv(A);
    det(A);
    eig(A);               // Eigenvalues only
    { val, vec } = eigv(A);  // Eigenvalues and vectors
    { u, s, v } = svd(A);
    chol(A);
    inv(A) * b;           // Solve Ax = b

Regression
----------

.. code-block:: python

    # Python/statsmodels
    import statsmodels.api as sm
    X = sm.add_constant(df[["x1", "x2"]])
    model = sm.OLS(df["y"], X).fit()
    print(model.summary())

    # Python/sklearn
    from sklearn.linear_model import LinearRegression
    model = LinearRegression().fit(X, y)

::

    // GAUSS (much simpler)
    call olsmt(df, "y ~ x1 + x2");

Functions
---------

.. code-block:: python

    # Python
    def my_function(x, y):
        result = x + y
        return result

    # Lambda
    square = lambda x: x ** 2

::

    // GAUSS
    proc (1) = my_function(x, y);
        local result;
        result = x + y;
        retp(result);
    endp;

    // No direct lambda equivalent; use procedures

Key differences:

- ``proc (n) =`` declares number of return values
- ``local`` declares local variables (required)
- ``retp()`` returns values
- ``endp`` ends procedure

Loops
-----

.. code-block:: python

    # Python
    for i in range(10):
        print(i)

    # List comprehension
    squares = [x**2 for x in range(10)]

::

    // GAUSS
    for i (0, 9, 1);
        print i;
    endfor;

    // No comprehensions; use matrix operations
    x = seqa(0, 1, 10);
    squares = x.^2;

Note: Python's ``range(10)`` is 0-9; GAUSS ``for i (0, 9, 1)`` is also 0-9.

Quick Reference Table
---------------------

+-------------------------+---------------------------+---------------------------+
| Operation               | Python/NumPy              | GAUSS                     |
+=========================+===========================+===========================+
| Create array            | ``np.array([[1,2],[3,4]])``| ``{ 1 2, 3 4 }``         |
+-------------------------+---------------------------+---------------------------+
| Zeros                   | ``np.zeros((n,m))``       | ``zeros(n, m)``           |
+-------------------------+---------------------------+---------------------------+
| Identity                | ``np.eye(n)``             | ``eye(n)``                |
+-------------------------+---------------------------+---------------------------+
| Random normal           | ``np.random.randn(n,m)``  | ``rndn(n, m)``            |
+-------------------------+---------------------------+---------------------------+
| Range/sequence          | ``np.arange(1, n+1)``     | ``seqa(1, 1, n)``         |
+-------------------------+---------------------------+---------------------------+
| First element           | ``A[0, 0]``               | ``A[1, 1]``               |
+-------------------------+---------------------------+---------------------------+
| First row               | ``A[0, :]``               | ``A[1, .]``               |
+-------------------------+---------------------------+---------------------------+
| First column            | ``A[:, 0]``               | ``A[., 1]``               |
+-------------------------+---------------------------+---------------------------+
| Last row                | ``A[-1, :]``              | ``A[rows(A), .]``         |
+-------------------------+---------------------------+---------------------------+
| Matrix multiply         | ``A @ B``                 | ``A * B``                 |
+-------------------------+---------------------------+---------------------------+
| Element-wise multiply   | ``A * B``                 | ``A .* B``                |
+-------------------------+---------------------------+---------------------------+
| Horizontal concat       | ``np.hstack``             | ``A ~ B``                 |
+-------------------------+---------------------------+---------------------------+
| Vertical concat         | ``np.vstack``             | ``A | B``                 |
+-------------------------+---------------------------+---------------------------+
| Transpose               | ``A.T``                   | ``A'``                    |
+-------------------------+---------------------------+---------------------------+
| Shape                   | ``A.shape``               | ``rows(A)`` ``cols(A)``   |
+-------------------------+---------------------------+---------------------------+
| Column mean             | ``np.mean(A, axis=0)``    | ``meanc(A)``              |
+-------------------------+---------------------------+---------------------------+
| Row mean                | ``np.mean(A, axis=1)``    | ``meanr(A)``              |
+-------------------------+---------------------------+---------------------------+
| Load CSV                | ``pd.read_csv()``         | ``loadd()``               |
+-------------------------+---------------------------+---------------------------+
| Print                   | ``print(x)``              | ``print x;``              |
+-------------------------+---------------------------+---------------------------+

Common Gotchas
--------------

1. **Indexing starts at 1.** The first element is ``A[1, 1]``, not ``A[0, 0]``

2. **Slices are inclusive.** ``A[1:3, .]`` includes rows 1, 2, AND 3

3. **Operators are reversed.** ``*`` is matrix multiply, ``.*`` is element-wise (opposite of NumPy!)

4. **Semicolons required.** Every statement ends with ``;``

5. **All rows/columns.** Use ``.`` not ``:`` (e.g., ``A[., 1]`` not ``A[:, 0]``)

6. **String quotes.** Only double quotes ``"string"`` work

7. **No negative indexing.** Use ``A[rows(A), .]`` for last row, not ``A[-1, :]``

What's Next?
------------

- :doc:`../getting-started/quickstart` — General GAUSS introduction
- :doc:`../data-management` — Data import, export, manipulation
- `NumPy documentation <https://numpy.org/doc/stable/>`_ — For comparison

.. seealso::

    :func:`loadd`, :func:`olsmt`, :func:`meanc`, :func:`inv`, :func:`rndn`
