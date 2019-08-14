
hsec
==============================================

Purpose
----------------

Returns the number of hundredths of a second since midnight.

Format
----------------
.. function:: y = hsec

    :return y: hundredths of a second since midnight.

    :type y: scalar

Remarks
-------

The number of hundredths of a second since midnight can also be accessed
as the :math:`[4,1]` element of the vector returned by the :func:`date` function.


Examples
----------------

::

    // Define random x matrix
    x = rndu(1000, 1000);

    // Starting time
    tStart = hsec;

    //  Multiply x*x
    y = x*x;

    // Calculate time elapsed
    tTotal = hsec-tStart;

In this example, :func:`hsec` is used to time a 1000x1000 multiplication in GAUSS. A 1000x1000 matrix,
*x*, is created, and the current time, in hundredths of a
second since midnight, is stored in the variable *tStart*.
Then the multiplication is carried out. Finally, *tStart*
is subtracted from :func:`hsec` to give the time difference
which is assigned to *tTotal*.

.. seealso:: Functions :func:`date`, :func:`time`, :func:`timestr`, :func:`ethsec`, :func:`etstr`
