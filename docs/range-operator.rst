
range-operator
==============================================

Purpose
----------------

Creates a sequence of consecutive integers as a column vector, or specifies an index range when used inside brackets.

Format
----------------

::

    y = start:end

    x[start:end]

Parameters
----------------

    :param start: Starting value (truncated to integer).
    :type start: scalar

    :param end: Ending value (truncated to integer).
    :type end: scalar

Returns
----------------

    :return y: Column vector containing integers from *start* to *end*.

    :rtype y: (end - start + 1) x 1 vector

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

Remarks
-------

- Outside of brackets, ``a:b`` is equivalent to ``seqa(a, 1, b-a+1)`` for ascending ranges or ``seqa(a, -1, a-b+1)`` for descending ranges.

- Inside brackets, ``x[a:b]`` creates an index range for efficient slicing without creating an intermediate vector.

- Non-integer bounds are truncated: ``1.7:4.2`` produces ``{1, 2, 3, 4}``.

- Single-element ranges are valid: ``5:5`` produces ``{5}``.

.. seealso:: Functions :func:`seqa`, :func:`seqm`
