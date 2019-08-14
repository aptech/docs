
null1
==============================================

Purpose
----------------

Computes an orthonormal basis for the (right) null space of a matrix and writes it to a GAUSS dataset.

Format
----------------
.. function:: nu = null1(x, dataset)

    :param x: data
    :type x: NxM matrix

    :param dataset: the name of a data set :func:`null1` will write.
    :type dataset: string

    :return nu: the nullity of *x*.

    :type nu: scalar

Remarks
-------

:func:`null1` computes an MxK matrix *b*, where *K* is the nullity of *x*, such that:

::

   x * b = 0 // NxK matrix of 0's

and

::

   b'b = I   // MxM identity matrix

The transpose of *b* is written to the data set named by *dataset*, unless
the nullity of *x* is zero. If *nu* is zero, the data set is not written.

Globals
-------

\_qrdc, \_qrsl

Source
------

null.src

