
strtofcplx
==============================================

Purpose
----------------

Converts a string array to a complex numeric matrix.

Format
----------------
.. function:: strtofcplx(sa)

    :param sa: 
    :type sa: NxK string array containing numeric data

    :returns: x (*NxK complex matrix*) .



Remarks
-------

strtofcplx supports both real and complex data. It is slower than strtof
for real matrices. strtofcplx requires the presence of the real part.
The imaginary part can be absent.

.. seealso:: Functions :func:`strtof`, :func:`ftostrC`
