
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

.. seealso:: Functions :func:`strtof`, :func:`ftostrC`
