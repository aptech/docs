
strtofcplx
==============================================

Purpose
----------------

Converts a string array to a complex numeric matrix.

Format
----------------
.. function:: x = strtofcplx(sa)

    :param sa: numeric data
    :type sa: NxK string array

    :return x: complex numeric matrix created from contents in *sa*;

    :rtype x: NxK complex matrix

Remarks
-------

:func:`strtofcplx` supports both real and complex data. It is slower than :func:`strtof`
for real matrices. :func:`strtofcplx` requires the presence of the real part.
The imaginary part can be absent.

Examples
----------------

::

    // Spaces required around + and -
    string sa = { "3 + 2i" "1 - 4i" };

    x = strtofcplx(sa);
    print x;

The code above produces the following output:

::

    3.0000000 + 2.0000000i       1.0000000 - 4.0000000i

.. seealso:: Functions :func:`strtof`, :func:`ftostrC`
