
seqa, seqm
==============================================

Purpose
----------------
seqa creates an additive sequence. seqm creates a multiplicative
sequence.

Format
----------------
.. function:: seqa(start, inc, n)
              seqm(start, inc, n)

    :param start: specifying the first element
    :type start: scalar

    :param inc: specifying increment
    :type inc: scalar

    :param n: specifying the number of elements in the sequence
    :type n: scalar

    :returns: y (*nx1 vector*) containing the specified sequence.

Remarks
-------

For :func:`seqa`, *y* will contain a first element equal to *start*, the second
equal to :math:`start + inc`, and the last equal to :math:`start + inc*(n-1)`.

For instance,

::

    seqa(1,1,10);

will create a column vector containing the numbers 1, 2, ...10.

For :func:`seqm`, *y* will contain a first element equal to *start*, the second
equal to :math:`start * inc`, and the last equal to :math:`start * inc^n-1`.

.. DANGER:: fix equations

For instance,

::

   seqm(10,10,10);

will create a column vector containing the numbers 10, 100,...:math:`10^10`.

Examples
----------------

::

    a = seqa(2,2,10)';
    print a;

::

    2 4 6 8 10 12 14 16 18 20

::

    m = seqm(2,2,10)';
    print m;

::

    2 4 8 16 32 64 128 512 1024

Note that the results have been transposed in this example. Both functions return Nx1 (column) vectors.

.. seealso:: Functions :func:`recserar`, :func:`recsercp`

