
string-vertical-concat
==============================================

Purpose
----------------

Vertically concatenates string arrays by stacking rows.

Format
----------------

::

    y = a $| b

Parameters
----------------

    :param a: Top string array.
    :type a: string or string array

    :param b: Bottom string array.
    :type b: string or string array

Returns
----------------

    :return y: String array with rows of *a* followed by rows of *b*.

    :rtype y: string array

Examples
----------------

::

    a = { "apple", "banana" };
    b = { "cherry", "date" };
    y = a $| b;

::

    y = "apple"
        "banana"
        "cherry"
        "date"

Building a List
+++++++++++++++

::

    header = { "Name", "Age", "City" };
    data = { "John", "Jane" };
    y = header $| data;

::

    y = "Name"
        "Age"
        "City"
        "John"
        "Jane"

Remarks
-------

- Both operands must have the same number of columns.
- For element-by-element string combination, use ``$+``.
- Analogous to ``|`` for numeric matrices.

.. seealso:: Operators :doc:`string-horizontal-concat`, :doc:`string-combine`, :doc:`vertical-concatenation`
