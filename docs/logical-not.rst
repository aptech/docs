
logical-not
==============================================

Purpose
----------------

Performs logical negation.

Format
----------------

::

    y = not a

Parameters
----------------

    :param a: Input value.
    :type a: scalar, vector, or matrix

Returns
----------------

    :return y: 1 where *a* is zero, 0 where *a* is non-zero.

    :rtype y: same dimensions as input

Examples
----------------

::

    x = 0;
    y = not x;

::

    y =    1.0000000

::

    x = { 0, 1, 0, 5, -3 };
    y = not x;

::

    y =    1.0000000
           0.0000000
           1.0000000
           0.0000000
           0.0000000

In Conditional Logic
++++++++++++++++++++

::

    found = 0;
    if not found;
        print "Not found";
    endif;

::

    Not found

Remarks
-------

- Any non-zero value is considered true; zero is false.
- ``not`` operates element-by-element on matrices.
- Equivalent to ``a .== 0``.

.. seealso:: Operators :doc:`logical-and`, :doc:`logical-or`
