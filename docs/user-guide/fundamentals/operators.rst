.. _operators:

Operators and Expressions
===============================================

GAUSS is a matrix language, and most of its operators work on matrices
as well as scalars. The key distinction to learn is between **matrix**
operators (which follow linear-algebra rules) and **element-wise**
operators (which apply independently to each element). Element-wise
operators are prefixed with a dot: ``.*``, ``./``, ``.^``, ``.==``, etc.

This page covers arithmetic, concatenation, comparison, logical, and
indexing operators, plus broadcasting rules and operator precedence.
For complete specifications of each operator, see the
:doc:`/cc/operators` reference.

.. note::

    In GAUSS, curly braces create matrix literals. Spaces separate
    columns, commas separate rows: ``{ 1 2, 3 4 }`` creates a 2x2
    matrix with rows [1 2] and [3 4].

.. note::

    If you are coming from MATLAB, the dot-prefix convention is similar,
    but not identical — GAUSS ``^`` is element-wise (same as ``.^``),
    unlike MATLAB where ``^`` is matrix power.
    If you are coming from Python/NumPy, GAUSS ``*`` is ``@`` (matrix
    multiply), and GAUSS ``.*`` is ``*`` (element-wise).

.. note::

    In GAUSS, any nonzero value is TRUE and zero is FALSE. Comparison
    operators return 1 for true and 0 for false.


Arithmetic Operators
--------------------------------------------

.. list-table::
    :widths: 10 25 65
    :header-rows: 1

    * - Operator
      - Name
      - Description

    * - ``+``
      - Addition
      - Element-wise addition (supports :ref:`broadcasting <exe-conformability>`)

    * - ``-``
      - Subtraction
      - Element-wise subtraction (supports :ref:`broadcasting <exe-conformability>`)

    * - ``*``
      - Matrix multiply
      - Standard matrix product (NxK \* KxM = NxM). If either operand is
        a scalar, performs element-wise multiplication instead.

    * - ``.*``
      - Element-wise multiply
      - Multiplies corresponding elements

    * - ``/``
      - Matrix division
      - ``A / B`` is equivalent to ``inv(B) * A``. If either operand is
        a scalar, performs element-wise division instead.

    * - ``./``
      - Element-wise division
      - Divides corresponding elements

    * - ``^``  ``.^``
      - Element-wise power
      - Raises each element independently. Both forms are identical —
        GAUSS has no matrix power operator.

    * - ``.*.``
      - Kronecker product
      - Tensor product of two matrices. See :func:`kronecker`.

    * - ``%``
      - Modulo (element-wise)
      - Remainder after division for each element

    * - ``'``
      - Transpose
      - Transposes rows and columns

    * - ``!``
      - Factorial
      - ``n!`` computes n factorial

Example: Matrix vs. element-wise multiply
+++++++++++++++++++++++++++++++++++++++++++++

::

    A = { 1 2, 3 4 };
    B = { 5 6, 7 8 };

    // Matrix multiply: linear algebra product
    print "A * B:";
    print A * B;

    // Element-wise multiply: each element independently
    print "A .* B:";
    print A .* B;

This prints:

::

    A * B:

       19.000000        22.000000
       43.000000        50.000000
    A .* B:

       5.0000000        12.000000
       21.000000        32.000000

Matrix multiply produces a 2x2 result using dot products of rows and
columns. Element-wise multiply simply multiplies each pair of
corresponding elements: 1*5, 2*6, 3*7, 4*8.

Example: Element-wise power
+++++++++++++++++++++++++++++++++

::

    x = { 1, 2, 3, 4, 5 };

    // Square each element
    print x .^ 2;

This prints:

::

       1.0000000
       4.0000000
       9.0000000
       16.000000
       25.000000


Concatenation Operators
--------------------------------------------

.. list-table::
    :widths: 10 25 65
    :header-rows: 1

    * - Operator
      - Name
      - Description

    * - ``~``
      - Horizontal concatenation
      - Joins matrices side by side (same row count)

    * - ``|``
      - Vertical concatenation
      - Stacks matrices top to bottom (same col count)

    * - ``$+``
      - String concatenation
      - Joins two strings end to end

Example: Building matrices with ~ and |
++++++++++++++++++++++++++++++++++++++++++

::

    a = { 1 2, 3 4 };
    b = { 5 6, 7 8 };

    // Side by side (horizontal): same number of rows required
    print a ~ b;

    // Stacked (vertical): same number of columns required
    print a | b;

This prints:

::

       1.0000000        2.0000000        5.0000000        6.0000000
       3.0000000        4.0000000        7.0000000        8.0000000

       1.0000000        2.0000000
       3.0000000        4.0000000
       5.0000000        6.0000000
       7.0000000        8.0000000

These operators are used throughout GAUSS to assemble data. For example,
``1|rows(x)`` creates the 2x1 column vector ``{ 1, rows(x) }`` — this
idiom appears frequently with functions like :func:`rndi` that take
range vectors.


Comparison Operators
--------------------------------------------

GAUSS has two sets of comparison operators: **element-wise** (dot-prefix)
and **matrix** (no prefix).

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - Element-wise
      - Matrix
      - Description

    * - ``.==``
      - ``==``
      - Equal

    * - ``./=`` (or ``.!=``)
      - ``/=`` (or ``!=``)
      - Not equal

    * - ``.<``
      - ``<``
      - Less than

    * - ``.<=``
      - ``<=``
      - Less than or equal

    * - ``.>``
      - ``>``
      - Greater than

    * - ``.>=``
      - ``>=``
      - Greater than or equal

- **Element-wise** (e.g., ``.==``) — compares each pair of elements and
  returns a matrix of 1s and 0s the same size as the inputs.
- **Matrix** (e.g., ``==``) — returns a single scalar: 1 if the
  condition holds for **every** element, 0 otherwise.

Example: Element-wise vs. matrix comparison
++++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 1 5, 3 2 };
    y = { 2 4, 3 3 };

    // Element-wise: returns a matrix of 0s and 1s
    print "x .== y:";
    print x .== y;

    // Matrix: returns a single scalar (1 only if ALL elements match)
    print "x == y:";
    print x == y;

This prints:

::

    x .== y:

       0.0000000        0.0000000
       1.0000000        0.0000000
    x == y:
       0.0000000

Element-wise ``.==`` shows that only position [2,1] is equal (both 3).
Matrix ``==`` returns 0 because the matrices are not identical everywhere.

.. tip::

    Use element-wise comparisons (``.==``, ``.<``, etc.) when you want
    to find *which* elements meet a condition. Use matrix comparisons
    (``==``, ``<``, etc.) when you need a single yes/no answer — for
    example, in an ``if`` statement, which requires a scalar.


Logical Operators
--------------------------------------------

.. list-table::
    :widths: 20 20 60
    :header-rows: 1

    * - Element-wise
      - Matrix
      - Description

    * - ``.and``
      - ``and``
      - Logical AND

    * - ``.or``
      - ``or``
      - Logical OR

    * - ``.not``
      - ``not``
      - Logical NOT

    * - ``.xor``
      - ``xor``
      - Logical exclusive OR

    * - ``.eqv``
      - ``eqv``
      - Logical equivalence

The same element-wise vs. matrix distinction applies: ``.and`` returns a
matrix of results; ``and`` returns a single scalar.

Example: Logical operators
+++++++++++++++++++++++++++++++++

::

    a = { 1 0, 1 1 };
    b = { 1 1, 0 0 };

    print "a .and b:";
    print a .and b;

    print ".not a:";
    print .not a;

This prints:

::

    a .and b:

       1.0000000        0.0000000
       0.0000000        0.0000000
    .not a:

       0.0000000        1.0000000
       0.0000000        0.0000000


Indexing
--------------------------------------------

Square brackets ``[ ]`` are used to extract or assign submatrices.

.. note::

    GAUSS indices start at 1 (like R and MATLAB), not 0 (like Python).
    The first element of a vector is ``v[1]``, not ``v[0]``.

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

**Single element:**

::

    x[2, 3]          // 7 — row 2, column 3

**Entire row or column** — use a dot ``.`` for "all":

::

    x[., 1]          // { 1, 5, 9 } — all rows of column 1
    x[2, .]          // { 5 6 7 8 } — row 2, all columns

**Range** — use a colon ``:`` for consecutive indices:

::

    x[1:2, .]        // rows 1 through 2, all columns

**Specific rows/columns** — list indices separated by spaces:

::

    x[1 3, 2 4]      // rows 1 and 3, columns 2 and 4

Example: Indexing a matrix
+++++++++++++++++++++++++++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    print "x[2, 3] =" x[2, 3];
    print "x[., 1] (all rows, col 1):";
    print x[., 1];
    print "x[1:2, .] (rows 1-2, all cols):";
    print x[1:2, .];
    print "x[1 3, 2 4] (rows 1,3 cols 2,4):";
    print x[1 3, 2 4];

This prints:

::

    x[2, 3] =       7.0000000
    x[., 1] (all rows, col 1):

       1.0000000
       5.0000000
       9.0000000
    x[1:2, .] (rows 1-2, all cols):

       1.0000000        2.0000000        3.0000000        4.0000000
       5.0000000        6.0000000        7.0000000        8.0000000
    x[1 3, 2 4] (rows 1,3 cols 2,4):

       2.0000000        4.0000000
       10.000000        12.000000

.. note::

    Vectors can be indexed with a single index: ``v[3]`` returns the
    third element regardless of whether *v* is a row or column vector.


.. _exe-conformability:

ExE Conformability (Broadcasting)
--------------------------------------------

Element-wise operators do not require the operands to have exactly the
same dimensions. GAUSS automatically **broadcasts** smaller operands to
match larger ones, following these rules:

- A **scalar** is conformable with any matrix — the scalar is applied
  to every element.
- A **column vector** (Nx1) is conformable with an NxK matrix — the
  vector is applied to each column.
- A **row vector** (1xK) is conformable with an NxK matrix — the
  vector is applied to each row.

This is called **ExE conformability** and works with all element-wise
operators (``.*``, ``.^``, ``.==``, etc.) as well as ``+`` and ``-``.

If the dimensions do not match any of these rules, GAUSS raises the
error: ``Matrix dimensions are incompatible``.

Example: Broadcasting in action
+++++++++++++++++++++++++++++++++

::

    x = { 1, 2, 3 };           // 3x1 column vector
    y = { 10 20 30 40 };       // 1x4 row vector

    // 3x1 .* 1x4 broadcasts to 3x4
    print x .* y;

This prints:

::

       10.000000        20.000000        30.000000        40.000000
       20.000000        40.000000        60.000000        80.000000
       30.000000        60.000000        90.000000        120.00000

Each element of *x* is multiplied by every element of *y*, producing a
3x4 result. This is the GAUSS equivalent of NumPy broadcasting or
MATLAB's implicit expansion.


The Transpose Shorthand: X'Y
--------------------------------------------

GAUSS provides a shorthand for the common expression ``X' * Y``:

::

    // These are equivalent:
    result1 = X' * Y;
    result2 = X'Y;

When the transpose operator ``'`` is immediately followed by a variable
name (no space or operator between them), GAUSS interprets it as
"transpose *X*, then matrix-multiply by *Y*."

Example: Transpose-multiply shorthand
+++++++++++++++++++++++++++++++++++++++

::

    X = { 1 2, 3 4, 5 6 };   // 3x2
    Y = { 7, 8, 9 };          // 3x1

    // Transpose X (2x3) then multiply by Y (3x1) = 2x1
    print X'Y;

This prints:

::

       76.000000
       100.00000

.. warning::

    The shorthand only works for the simple form ``X'Y``. For
    compound expressions, use explicit parentheses::

        // WRONG: ambiguous
        z = X'Y / W'X;

        // RIGHT: explicit grouping
        z = (X'Y) / (W'X);


Operator Precedence
--------------------------------------------

Operators are evaluated from **highest to lowest** precedence. Within
the same precedence level, evaluation is left to right. This table lists
the most commonly used operators:

.. list-table::
    :widths: 15 50 15
    :header-rows: 1

    * - Precedence
      - Operators
      - Category

    * - 90
      - ``'``  ``.'`` (transpose)
      - Unary

    * - 89
      - ``!`` (factorial)
      - Unary

    * - 85
      - ``^``  ``.^`` (power)
      - Arithmetic

    * - 83
      - unary ``-`` (negation)
      - Unary

    * - 80
      - ``*``  ``.*``  ``.*.``  ``/``  ``./``
      - Arithmetic

    * - 75
      - ``%`` (modulo)
      - Arithmetic

    * - 70
      - ``+``  ``-``  ``$+``
      - Arithmetic / String

    * - 68
      - ``~`` (horizontal concat)
      - Concatenation

    * - 67
      - ``|`` (vertical concat)
      - Concatenation

    * - 65
      - ``.==``  ``./=``  ``.<``  ``.<=``  ``.>``  ``.>=``
      - Element-wise comparison

    * - 64–60
      - ``.not``  ``.and``  ``.or``  ``.xor``  ``.eqv``
      - Element-wise logical

    * - 55
      - ``==``  ``/=``  ``<``  ``<=``  ``>``  ``>=``
      - Matrix comparison

    * - 49–45
      - ``not``  ``and``  ``or``  ``xor``  ``eqv``
      - Matrix logical

    * - 10
      - ``=`` (assignment)
      - Assignment

Key takeaways:

- **Power before multiply before add** — same as standard math.
- **Dot-comparisons bind more tightly than non-dot** — ``.==`` (65) is
  evaluated before ``==`` (55).
- **Concatenation sits between arithmetic and comparisons** — so
  ``a + b ~ c + d`` means ``(a + b) ~ (c + d)``.
- When in doubt, **use parentheses** to make evaluation order explicit.

Example: Precedence in practice
+++++++++++++++++++++++++++++++++

::

    // This expression:
    print -5 + 3/4 + 6*3;

    // Is evaluated as:
    print (-5) + (3/4) + (6*3);

Both print:

::

       13.750000


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 25 25 50
    :header-rows: 1

    * - Category
      - Matrix form
      - Element-wise form

    * - Multiply
      - ``*``
      - ``.*``

    * - Divide
      - ``/``
      - ``./``

    * - Power
      - ``^`` or ``.^`` (both element-wise)
      -

    * - Equal
      - ``==`` (scalar result)
      - ``.==`` (matrix result)

    * - Not equal
      - ``/=``
      - ``./=``

    * - Less than
      - ``<``
      - ``.<``

    * - AND
      - ``and``
      - ``.and``

    * - OR
      - ``or``
      - ``.or``

    * - NOT
      - ``not``
      - ``.not``


.. seealso:: :doc:`/cc/operators`, :ref:`control-flow`, :doc:`/user-guide/fundamentals/procedures`, :func:`inv`, :func:`selif`
