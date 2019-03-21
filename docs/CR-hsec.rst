
hsec
==============================================

Purpose
----------------

Returns the number of hundredths of a second since midnight.

Format
----------------
.. function:: hsec

    :returns: y (*scalar*), hundredths of a second since midnight.

Remarks
-------

The number of hundredths of a second since midnight can also be accessed
as the [4,1] element of the vector returned by the date function.


Examples
----------------

::

    x = rndu(1000,1000);
    tStart = hsec;
    
    y = x*x;
    tTotal = hsec-tEnd;

In this example, hsec is used to time a 1000x1000 multiplication in GAUSS. A 1000x1000 matrix,
x, is created, and the current time, in hundredths of a
second since midnight, is stored in the variable tStart.
Then the multiplication is carried out. Finally, tStart
is subtracted from hsec to give the time difference
which is assigned to tTotal.

.. seealso:: Functions :func:`date`, :func:`time`, :func:`timestr`, :func:`ethsec`, :func:`etstr`
