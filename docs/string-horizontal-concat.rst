
string-horizontal-concat
==============================================

Purpose
----------------

Horizontally concatenates string arrays by appending columns.

Format
----------------

::

    y = a $~ b

Parameters
----------------

    :param a: Left string array.
    :type a: string or string array

    :param b: Right string array.
    :type b: string or string array

Returns
----------------

    :return y: String array with columns of *a* followed by columns of *b*.

    :rtype y: string array

Examples
----------------

::

    a = { "John", "Jane" };
    b = { "Smith", "Doe" };
    y = a $~ b;

::

    y = "John"    "Smith"
        "Jane"    "Doe"

Building a Table
++++++++++++++++

::

    names = { "Alice", "Bob", "Carol" };
    cities = { "NYC", "LA", "Chicago" };
    countries = { "USA", "USA", "USA" };
    table = names $~ cities $~ countries;

::

    table = "Alice"    "NYC"        "USA"
            "Bob"      "LA"         "USA"
            "Carol"    "Chicago"    "USA"

Remarks
-------

- Both operands must have the same number of rows.
- For element-by-element string combination, use ``$+``.
- Analogous to ``~`` for numeric matrices.

.. seealso:: Operators :doc:`string-vertical-concat`, :doc:`string-combine`, :doc:`horizontal-concatenation`
