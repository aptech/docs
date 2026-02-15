
string-combine
==============================================

Purpose
----------------

Combines strings element-by-element, appending corresponding elements.

Format
----------------

::

    y = a $+ b

Parameters
----------------

    :param a: Left string or string array.
    :type a: string or string array

    :param b: Right string or string array.
    :type b: string or string array

Returns
----------------

    :return y: String array with elements combined from *a* and *b*.

    :rtype y: string array

Examples
----------------

Basic String Combination
++++++++++++++++++++++++

::

    a = "Hello ";
    b = "World";
    y = a $+ b;

::

    y = "Hello World"

Array Combination
+++++++++++++++++

::

    first = { "John", "Jane", "Bob" };
    last = { "Smith", "Doe", "Jones" };
    full = first $+ " " $+ last;

::

    full = "John Smith"
           "Jane Doe"
           "Bob Jones"

Building File Paths
+++++++++++++++++++

::

    dir = "/data/";
    files = { "file1", "file2", "file3" };
    ext = ".csv";
    paths = dir $+ files $+ ext;

::

    paths = "/data/file1.csv"
            "/data/file2.csv"
            "/data/file3.csv"

Remarks
-------

- If both operands are arrays, they must have conformable dimensions.
- A scalar string is broadcast to match the dimensions of an array operand.
- This is element-by-element combination, not concatenation of arrays.
- For array concatenation, use ``$|`` (vertical) or ``$~`` (horizontal).

.. seealso:: Operators :doc:`string-vertical-concat`, :doc:`string-horizontal-concat`
