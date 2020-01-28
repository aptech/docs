
base10
==============================================

Purpose
----------------

Breaks number into a number of the form `#.####...` and a power of 10.

Format
----------------
.. function:: { M, P } = base10(x)

    :param x: number to break down.
    :type x: scalar

    :return M: in the range -10 < *M* < 10.

    :rtype M: scalar

    :return P: integer power such that:

    .. math:: M*10^P = x

    :rtype P: scalar

Examples
----------------

::

    { b, e } = base10(4500);

After the code above:

::

    b = 4.5  e = 3

and

::

    b*10^e = 4.5*10^3 = 4500

Source
------------

base10.src
