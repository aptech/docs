.. _arrays:

N-Dimensional Arrays
===============================================

GAUSS supports N-dimensional arrays as a data type separate from
matrices. While a matrix is always 2-dimensional (rows x columns), an
array can have 3, 4, or more dimensions. Arrays are useful for panel
data, multivariate time series, and any computation that operates on
collections of matrices.

.. note::

    If you are coming from Python, a GAUSS array is similar to a NumPy
    ``ndarray`` with 3+ dimensions. **However, GAUSS dimension numbering
    is reversed relative to NumPy:** GAUSS dimension 1 is the innermost
    (columns), while NumPy ``axis=0`` is the outermost. See
    :ref:`dimension-numbering` below.

    If you are coming from MATLAB, a GAUSS array is similar to a
    multidimensional array (e.g., ``A(:,:,k)``).

.. warning::

    Arrays and matrices are **distinct types** in GAUSS, even if they
    contain identical data. A 2x3 array is not the same as a 2x3
    matrix. Use :func:`arraytomat` and :func:`areshape` to convert
    between them.


Creating Arrays
--------------------------------------------

GAUSS provides several functions for creating arrays:

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`areshape`
      - Create an array from a matrix, recycling elements to fill the
        specified dimensions

    * - :func:`aconcat`
      - Concatenate matrices or arrays along a specified dimension

    * - :func:`aeye`
      - Create an array of identity matrices

    * - :func:`arrayinit`
      - Create an array filled with a single scalar value

    * - :func:`arrayalloc`
      - Allocate an array without initializing its contents

    * - :func:`squeeze`
      - Remove singleton dimensions from an array

Example: areshape
++++++++++++++++++++++++++++++++++++

:func:`areshape` is the most common way to create an array. It takes a
matrix and reshapes it into the specified dimensions, recycling elements
if needed:

::

    // Create a 2x2 matrix
    x = { 1 2, 3 4 };

    // Reshape into a 3x2x2 array (3 copies of the matrix)
    a = areshape(x, 3|2|2);
    print a;

This prints::

    Plane [1,.,.]

       1.0000000        2.0000000
       3.0000000        4.0000000

    Plane [2,.,.]

       1.0000000        2.0000000
       3.0000000        4.0000000

    Plane [3,.,.]

       1.0000000        2.0000000
       3.0000000        4.0000000

The **orders vector** (``3|2|2``) specifies the size of each dimension.
The first element of the orders vector is the outermost dimension (3
"planes"), and the last two elements define the rows and columns of
each plane (2x2).

When GAUSS prints an array, ``Plane [k,.,.]`` means the *k*-th slice
along the outermost dimension. The ``.`` symbols represent "all
elements" along the remaining dimensions (rows and columns).

.. _dimension-numbering:

Dimension numbering
++++++++++++++++++++++++++++++++++++

Many array functions take a *dimension* argument (e.g., :func:`amean`,
:func:`aconcat`). GAUSS numbers dimensions from the **innermost out**:

- **Dimension 1** — columns (innermost / last element of the orders
  vector)
- **Dimension 2** — rows (second-to-last element)
- **Dimension 3** — planes (third-to-last element)
- Higher dimensions follow the same pattern

For a ``2|3|4`` array (2 planes of 3 rows by 4 columns):

- ``amean(a, 1)`` averages across the 4 **columns**, returning a
  ``2|3|1`` array
- ``amean(a, 2)`` averages across the 3 **rows**, returning a
  ``2|1|4`` array
- ``amean(a, 3)`` averages across the 2 **planes**, returning a
  ``1|3|4`` array

.. warning::

    The dimension numbers are the **reverse** of the orders vector
    position. The orders vector lists the outermost dimension first
    (``2|3|4``), but dimension 1 refers to the innermost (4 columns).
    This also differs from NumPy, where ``axis=0`` is the outermost
    dimension.

Example: aconcat
++++++++++++++++++++++++++++++++++++

:func:`aconcat` joins two matrices or arrays along a specified
dimension:

::

    x1 = { 1 2, 3 4 };
    x2 = { 5 6, 7 8 };

    // Concatenate along the 3rd dimension
    a = aconcat(x1, x2, 3);
    print a;

This prints::

    Plane [1,.,.]

       1.0000000        2.0000000
       3.0000000        4.0000000

    Plane [2,.,.]

       5.0000000        6.0000000
       7.0000000        8.0000000

The third argument specifies which dimension to concatenate along.
Starting from two 2x2 matrices:

- ``aconcat(x1, x2, 1)`` — join along **columns** (dimension 1):
  result is 2x4
- ``aconcat(x1, x2, 2)`` — join along **rows** (dimension 2): result
  is 4x2
- ``aconcat(x1, x2, 3)`` — join along **planes** (dimension 3):
  result is 2x2x2 (creates a 3-D array)

Example: arrayinit and aeye
++++++++++++++++++++++++++++++++++++

::

    // 2x3x3 array of zeros
    a = arrayinit(2|3|3, 0);

    // 2x3x3 array of identity matrices
    b = aeye(2|3|3);
    print b;

This prints::

    Plane [1,.,.]

       1.0000000        0.0000000        0.0000000
       0.0000000        1.0000000        0.0000000
       0.0000000        0.0000000        1.0000000

    Plane [2,.,.]

       1.0000000        0.0000000        0.0000000
       0.0000000        1.0000000        0.0000000
       0.0000000        0.0000000        1.0000000

:func:`aeye` sets the principal diagonal of the **last two dimensions**
to 1.

Example: Random arrays
++++++++++++++++++++++++++++++++++++

Create a random array by reshaping a random vector:

::

    // 4x3x2 array of standard normal random numbers
    ord = 4|3|2;
    a = areshape(rndn(prodc(ord), 1), ord);


Indexing and Extracting
--------------------------------------------

GAUSS provides several ways to access elements and sub-arrays.

Index operator
++++++++++++++++++++++++++++++++++++

The bracket index operator works like matrix indexing, extended to
N dimensions. Use ``.`` to select all elements along a dimension:

::

    a = areshape(seqa(1, 1, 12), 3|2|2);

    // Extract plane 2 (a sub-array)
    b = a[2,.,.];
    print b;

This prints::

    Plane [1,.,.]

       5.0000000        6.0000000
       7.0000000        8.0000000

.. warning::

    The index operator **always returns an array**, even for a single
    scalar::

        c = a[1,1,1];
        print c;

    Prints::

        Plane [1,.,.]

           1.0000000

    Use :func:`getscalar3D` to extract a single element as a scalar,
    or :func:`getmatrix` / :func:`arraytomat` to get a matrix result.

getarray and getmatrix
++++++++++++++++++++++++++++++++++++

These functions extract contiguous sub-arrays and are faster than the
index operator:

::

    a = areshape(seqa(1, 1, 12), 3|2|2);

    // getarray returns an array (type 21)
    b = getarray(a, 2);
    print b;

This prints::

       5.0000000        6.0000000
       7.0000000        8.0000000

:func:`getarray` extracts a sub-array along the outermost dimension.
The second argument (*loc*) is an Mx1 vector that indexes into the
leading dimensions. For a 3-D array, a scalar selects a plane; for a
4-D array, a 2x1 vector selects a plane within a block::

    // 4-D array: 2 blocks x 3 planes x 2 rows x 2 columns
    a4 = areshape(seqa(1, 1, 24), 2|3|2|2);

    // Extract plane 2 of block 1
    b4 = getarray(a4, 1|2);

:func:`getmatrix` works the same way but guarantees the result is a
**matrix** (type 6) instead of an array (type 21)::

    c = getmatrix(a, 2);
    print type(c);

This prints::

       6.0000000

Use :func:`getmatrix` when you need to pass the result to a function
that requires a matrix.

For 3-D and 4-D arrays, GAUSS also provides convenience functions that
accept separate scalar indices:

- :func:`getscalar3D` — extract a single element from a 3-D array as
  a scalar (type 6)
- :func:`getmatrix4D` — extract a 2-D slice from a 4-D array as a
  matrix (type 6)
- :func:`getscalar4D` — extract a single element from a 4-D array as
  a scalar (type 6)

.. tip::

    For large arrays accessed in loops, :func:`getarray`,
    :func:`getmatrix`, and their 3D/4D variants are significantly
    faster than the index operator.

putarray and setarray
++++++++++++++++++++++++++++++++++++

These functions insert data into an array:

::

    a = arrayinit(3|2|2, 0);

    // putarray returns a new array (does not modify a)
    b = putarray(a, 2, eye(2));
    print b;

This prints::

    Plane [1,.,.]

       0.0000000        0.0000000
       0.0000000        0.0000000

    Plane [2,.,.]

       1.0000000        0.0000000
       0.0000000        1.0000000

    Plane [3,.,.]

       0.0000000        0.0000000
       0.0000000        0.0000000

:func:`putarray` returns a new array with the insertion applied.
:func:`setarray` modifies the array **in place**:

::

    a = arrayinit(3|2|2, 0);
    setarray a, 2, eye(2);    // modifies a directly


Array Operations
--------------------------------------------

Querying dimensions
++++++++++++++++++++++++++++++++++++

:func:`getorders` returns a vector containing the size of each
dimension. The length of the vector equals the number of dimensions:

::

    a = arrayinit(4|3|5|2, 0);
    print getorders(a);

This prints::

       4.0000000
       3.0000000
       5.0000000
       2.0000000

Use :func:`type` to check whether a variable is an array (type 21) or
matrix (type 6):

::

    a = arrayinit(2|3, 0);
    m = zeros(2, 3);
    print "array type:" type(a);
    print "matrix type:" type(m);

This prints::

    array type:       21.000000
    matrix type:       6.0000000

Transposing dimensions
++++++++++++++++++++++++++++++++++++

:func:`atranspose` reorders the dimensions of an array. The second
argument is a vector specifying the new order of dimensions:

::

    a = areshape(seqa(1, 1, 12), 2|3|2);
    print a;

    // Swap the 2nd and 3rd dimensions (transpose each plane)
    b = atranspose(a, 1|3|2);
    print b;

This prints::

    Plane [1,.,.]

       1.0000000        2.0000000
       3.0000000        4.0000000
       5.0000000        6.0000000

    Plane [2,.,.]

       7.0000000        8.0000000
       9.0000000        10.000000
       11.000000        12.000000

    Plane [1,.,.]

       1.0000000        3.0000000        5.0000000
       2.0000000        4.0000000        6.0000000

    Plane [2,.,.]

       7.0000000        9.0000000        11.000000
       8.0000000        10.000000        12.000000

The vector ``1|3|2`` means: keep dimension 1 in place, move dimension 3
to position 2, and move dimension 2 to position 3. This effectively
transposes each 2D plane within the array.

Array multiplication
++++++++++++++++++++++++++++++++++++

:func:`amult` performs matrix multiplication on the **last two
dimensions** of each array. The leading dimensions must match exactly:

::

    // 2x3x2 array (two 3x2 matrices)
    a = areshape(seqa(1, 1, 12), 2|3|2);

    // 2x2x2 array (two 2x2 matrices)
    b = areshape(seqa(1, 1, 8), 2|2|2);

    // Result: 2x3x2 array (two 3x2 results)
    c = amult(a, b);
    print c;

This prints::

    Plane [1,.,.]

       7.0000000        10.000000
       15.000000        22.000000
       23.000000        34.000000

    Plane [2,.,.]

       91.000000        106.00000
       115.00000        134.00000
       139.00000        162.00000

Each plane in ``c`` is the matrix product of the corresponding planes
in ``a`` and ``b``.

Array mean
++++++++++++++++++++++++++++++++++++

:func:`amean` computes the mean along a specified dimension, collapsing
that dimension to size 1:

::

    a = areshape(seqa(1, 1, 24), 2|3|4);

    // Mean across 4 columns (dimension 1) -> 2|3|1
    b = amean(a, 1);
    print b;

    // Mean across 3 rows (dimension 2) -> 2|1|4
    c = amean(a, 2);
    print c;

This prints::

    Plane [1,.,.]

       2.5000000
       6.5000000
       10.500000

    Plane [2,.,.]

       14.500000
       18.500000
       22.500000

    Plane [1,.,.]
       5.0000000        6.0000000        7.0000000        8.0000000

    Plane [2,.,.]
       17.000000        18.000000        19.000000        20.000000


Looping Over Array Planes
--------------------------------------------

A common pattern is to loop over the planes of a 3-D array, extracting
each plane as a matrix, operating on it, and storing the result back:

::

    a = areshape(rndn(300, 1), 3|10|10);
    result = arrayinit(3|10|10, 0);

    for i(1, 3, 1);
        m = getmatrix(a, i);       // extract plane i as a matrix
        setarray result, i, inv(m); // store inverse back
    endfor;

.. tip::

    Use :func:`getmatrix` / :func:`getarray` and :func:`setarray`
    instead of the index operator (``a[i,.,.]``) inside loops. The
    dedicated functions avoid creating temporary arrays on each
    iteration and can be over **2x faster** for large arrays.


Converting Between Arrays and Matrices
--------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`arraytomat`
      - Convert a 1-D or 2-D array to a matrix

    * - :func:`areshape`
      - Convert a matrix into an array (or reshape an existing array)

    * - :func:`getmatrix`
      - Extract a 2-D slice from an array as a matrix

    * - :func:`squeeze`
      - Remove singleton dimensions; if the result is 2-D it becomes
        a matrix (type 6). E.g., a 1xNx1 array becomes an Nx1 matrix

Example: arraytomat
++++++++++++++++++++++++++++++++++++

::

    // Create a 2-D array (same shape as a matrix, but type 21)
    a = arrayinit(2|3, 5);
    print "array type:" type(a);

    // Convert to a matrix (type 6)
    m = arraytomat(a);
    print "matrix type:" type(m);
    print m;

This prints::

    array type:       21.000000
    matrix type:       6.0000000
       5.0000000        5.0000000        5.0000000
       5.0000000        5.0000000        5.0000000


Using Arrays with GAUSS Functions
--------------------------------------------

Many built-in GAUSS functions accept arrays. There are two general
patterns:

Element-wise functions
++++++++++++++++++++++++++++++++++++

Functions like :func:`cdfnc`, :func:`ln`, :func:`exp`, :func:`abs`,
and other element-wise operations return an array of the same size and
shape:

::

    a = areshape(seqa(-2, 0.5, 12), 2|3|2);
    b = cdfnc(a);
    print b;

This prints::

    Plane [1,.,.]

       0.97724987       0.93319280
       0.84134475       0.69146246
       0.50000000       0.30853754

    Plane [2,.,.]

       0.15865525       0.066807201
       0.022750132      0.0062096653
       0.0013498980     0.00023262907

Matrix functions
++++++++++++++++++++++++++++++++++++

Functions like :func:`moment`, :func:`inv`, :func:`det`, and
:func:`svds` operate on the **last two trailing dimensions**. All
leading dimensions are treated as independent instances:

- A 5x10x3 array passed to :func:`moment` returns a 5x3x3 array
  (five 3x3 moment matrices from five 10x3 data matrices).
- A 2x3x4x5x10x6 array passed to :func:`moment` returns a
  2x3x4x5x6x6 array.

::

    // 2x3x4 array
    a = areshape(seqa(1, 1, 24), 2|3|4);

    // amean along dim 1 collapses columns: 2|3|4 -> 2|3|1
    b = amean(a, 1);

.. note::

    Not all functions follow these two patterns exactly. Check the
    function reference if you are unsure how a particular function
    handles array input.


Function Reference
--------------------------------------------

.. list-table:: Creating and reshaping
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`areshape`
      - Create an array from a matrix or reshape an existing array

    * - :func:`aconcat`
      - Concatenate arrays along a specified dimension

    * - :func:`aeye`
      - Create an array of identity matrices

    * - :func:`arrayinit`
      - Create an array filled with a single scalar value

    * - :func:`arrayalloc`
      - Allocate an array without initializing its contents

.. list-table:: Extracting and inserting
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`getarray`
      - Extract a sub-array along the leading dimensions (returns
        array, type 21)

    * - :func:`getmatrix`
      - Extract a 2-D slice as a matrix (returns type 6)

    * - :func:`getscalar3D`
      - Extract a single element from a 3-D array as a scalar

    * - :func:`getmatrix4D`
      - Extract a 2-D slice from a 4-D array as a matrix

    * - :func:`getscalar4D`
      - Extract a single element from a 4-D array as a scalar

    * - :func:`putarray`
      - Insert data into an array (returns new array)

    * - :func:`setarray`
      - Insert data into an array (modifies in place)

.. list-table:: Operations and queries
    :widths: 25 75
    :header-rows: 1

    * - Function
      - Description

    * - :func:`getorders`
      - Get the size of each dimension as a vector

    * - :func:`atranspose`
      - Reorder dimensions of an array

    * - :func:`amult`
      - Matrix multiply along trailing dimensions

    * - :func:`amean`
      - Mean along a specified dimension

    * - :func:`arraytomat`
      - Convert a 2-D array to a matrix

    * - :func:`squeeze`
      - Remove singleton dimensions (may return a matrix)

    * - :func:`type`
      - Returns 21 for arrays, 6 for matrices


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Task
      - How

    * - Create array from matrix
      - ``a = areshape(x, 3|2|2);``

    * - Create array of zeros
      - ``a = arrayinit(3|2|2, 0);``

    * - Create array of identity matrices
      - ``a = aeye(3|2|2);``

    * - Stack matrices into 3-D array
      - ``a = aconcat(x1, x2, 3);``

    * - Get dimension sizes
      - ``getorders(a)``

    * - Extract a plane as matrix
      - ``m = getmatrix(a, i);``

    * - Extract a scalar from 3-D array
      - ``s = getscalar3D(a, plane, row, col);``

    * - Insert matrix into plane
      - ``a = putarray(a, i, m);``

    * - Transpose within each plane
      - ``b = atranspose(a, 1|3|2);``

    * - Multiply across planes
      - ``c = amult(a, b);``

    * - Mean along a dimension
      - ``amean(a, dim)``

    * - Convert array to matrix
      - ``m = arraytomat(a);``

    * - Check if array
      - ``type(a)`` returns 21


.. seealso:: :ref:`operators`, :doc:`/user-guide/advanced/structures`
