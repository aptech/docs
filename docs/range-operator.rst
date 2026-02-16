
range-operator
==============================================

Purpose
----------------

Creates a sequence of integers or stepped values as a column vector, or specifies an index range when used inside brackets.

Format
----------------

::

    // Two-argument form: consecutive integers
    y = start:end

    // Three-argument form: stepped sequence
    y = start:step:end

    // Inside brackets for indexing
    x[start:end]
    x[start:step:end]

Parameters
----------------

    :param start: Starting value.
    :type start: scalar

    :param step: Step size (increment between elements). Can be positive or negative. Defaults to 1 or -1 based on direction.
    :type step: scalar

    :param end: Ending value.
    :type end: scalar

Returns
----------------

    :return y: Column vector containing the sequence from *start* to *end* with increment *step*.

    :rtype y: Nx1 vector where N = floor((end - start) / step) + 1

Examples
----------------

Basic Range
+++++++++++

::

    // Create a vector from 1 to 5
    x = 1:5;

::

    x =    1.0000000
           2.0000000
           3.0000000
           4.0000000
           5.0000000

Descending Range
++++++++++++++++

::

    // Create a descending vector
    x = 5:1;

::

    x =    5.0000000
           4.0000000
           3.0000000
           2.0000000
           1.0000000

Stepped Range (Three-Argument Form)
+++++++++++++++++++++++++++++++++++

::

    // Count by 2s from 1 to 10
    x = 1:2:10;

::

    x =    1.0000000
           3.0000000
           5.0000000
           7.0000000
           9.0000000

::

    // Count down by 2s
    x = 10:-2:1;

::

    x =   10.0000000
           8.0000000
           6.0000000
           4.0000000
           2.0000000

::

    // Float step values
    x = 0:0.5:2;

::

    x =    0.0000000
          0.50000000
           1.0000000
           1.5000000
           2.0000000

Negative Values
+++++++++++++++

::

    // Range including negative numbers
    x = -2:2;

::

    x =   -2.0000000
          -1.0000000
           0.0000000
           1.0000000
           2.0000000

Variables and Expressions as Bounds
+++++++++++++++++++++++++++++++++++

::

    // Using variables
    a = 1;
    b = 10;
    x = a:b;

    // Using expressions
    n = 5;
    x = (n-2):(n+2);    // Creates 3:7

    // Using function calls
    data = { 3, 7, 1, 9 };
    x = minc(data):maxc(data);    // Creates 1:9

Range as Function Argument
++++++++++++++++++++++++++

::

    // Sum of 1 to 100
    total = sumc(1:100);

::

    total =    5050.0000

::

    // Mean of 1 to 10
    avg = meanc(1:10);

::

    avg =    5.5000000

Index Range (Inside Brackets)
+++++++++++++++++++++++++++++

When used inside brackets, the colon operator creates an index range rather than a vector:

::

    x = { 10, 20, 30, 40, 50 };

    // Select rows 2 through 4
    y = x[2:4];

::

    y =   20.0000000
          30.0000000
          40.0000000

::

    // 2D indexing
    m = reshape(seqa(1,1,12), 3, 4);

    // Select rows 1-2, columns 2-3
    y = m[1:2, 2:3];

Stepped Index Range
+++++++++++++++++++

::

    x = seqa(1, 1, 10);

    // Select every other element (indices 1, 3, 5, 7, 9)
    y = x[1:2:10];

::

    y =    1.0000000
           3.0000000
           5.0000000
           7.0000000
           9.0000000

::

    // Reverse indexing with step
    y = x[10:-2:1];

::

    y =   10.0000000
           8.0000000
           6.0000000
           4.0000000
           2.0000000

::

    // 2D matrix: every other row
    m = reshape(seqa(1,1,20), 4, 5);
    y = m[1:2:4, .];

Remarks
-------

Two-Argument Form (start:end)
+++++++++++++++++++++++++++++

- Outside of brackets, ``a:b`` is equivalent to ``seqa(a, 1, b-a+1)`` for ascending ranges or ``seqa(a, -1, a-b+1)`` for descending ranges.

- Inside brackets, ``x[a:b]`` creates an index range for efficient slicing without creating an intermediate vector.

- Non-integer bounds are truncated: ``1.7:4.2`` produces ``{1, 2, 3, 4}``.

- Single-element ranges are valid: ``5:5`` produces ``{5}``.

Three-Argument Form (start:step:end)
++++++++++++++++++++++++++++++++++++

- The three-argument form ``start:step:end`` creates a sequence with custom step size, similar to MATLAB syntax.

- Outside of brackets, ``a:b:c`` is equivalent to ``seqa(a, b, floor((c-a)/b)+1)``.

- Inside brackets, ``x[a:b:c]`` efficiently indexes with a stepped range.

- The step can be any non-zero value, including floats: ``0:0.1:1`` creates ``{0, 0.1, 0.2, ..., 1}``.

- Negative steps create descending sequences: ``10:-2:1`` creates ``{10, 8, 6, 4, 2}``.

- The step direction must match the start-to-end direction (step > 0 when start < end, step < 0 when start > end).

- A step of zero is an error.

.. seealso:: Functions :func:`seqa`, :func:`seqm`
