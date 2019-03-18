
let
==============================================

Purpose
----------------

Creates a matrix from a list of numeric or character values. The result is always of type matrix,
string, or string array.

Format
----------------
.. function:: constant_list

Examples
----------------

::

    let x;

assigns x to be:

::

    x = 0

::

    let x = { 1 2 3, 4 5 6, 7 8 9 };

assigns x to be:

::

    1 2 3
    x = 3 4 5
        6 7 8

::

    let x[3,3] = 1 2 3 4 5 6 7 8 9;

assigns x to be:

::

    1 2 3
    x = 3 4 5
        6 7 8

::

    let x[3,3] = 1;

assigns x to be:

::

    1 1 1
    x = 1 1 1
        1 1 1

::

    let x[3,3];

assigns x to be:

::

    0 0 0
    x = 0 0 0
        0 0 0

::

    let x = dog cat;

assigns x to be:

::

    x = DOG
        CAT

::

    let x = "dog""cat";

assigns x to be:

::

    x = dog
        cat

::

    let string x = { "Median Income", "Country" };

assigns x to be:

::

    x = Median Income
        Country

.. seealso:: Functions :func:`con`, :func:`cons`, :func:`declare`, :func:`load`
