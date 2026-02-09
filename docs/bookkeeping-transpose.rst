
bookkeeping-transpose
==============================================

Purpose
----------------

Transposes a matrix without complex conjugation.

Format
----------------

::

    y = x.'

Parameters
----------------

    :param x: Input matrix.
    :type x: MxN matrix

Returns
----------------

    :return y: Transposed matrix with rows and columns swapped, without conjugation.

    :rtype y: NxM matrix

Examples
----------------

::

    x = { 1 2 3,
          4 5 6 };
    y = x.';

::

    y =    1.0000000    4.0000000
           2.0000000    5.0000000
           3.0000000    6.0000000

Complex Matrix
++++++++++++++

::

    // For complex matrices, .' does NOT conjugate
    x = { 1+2i, 3+4i };
    y = x.';

    // y = { 1+2i,
    //       3+4i }
    // (imaginary parts remain positive)

    // Compare with conjugate transpose:
    z = x';

    // z = { 1-2i,
    //       3-4i }
    // (imaginary parts are negated)

Remarks
-------

- For real matrices, ``.'`` and ``'`` produce identical results.
- For complex matrices, ``.'`` preserves the imaginary component while ``'`` conjugates it.

.. seealso:: Operators :doc:`transpose`
