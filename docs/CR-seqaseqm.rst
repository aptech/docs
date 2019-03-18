
seqa, seqm
==============================================

Purpose
----------------
seqa creates an additive sequence. seqm creates a multiplicative
sequence.

Format
----------------
.. function:: seqm(start,  inc,  n)

    :param start: scalar specifying the first element.
    :type start: TODO

    :param inc: scalar specifying increment.
    :type inc: TODO

    :param n: scalar specifying the number of elements in the sequence.
    :type n: TODO

    :returns: y (*TODO*), nx1 vector containing the specified sequence.

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

Note that the results have been transposed in this example. Both
functions return Nx1 (column) vectors.

.. seealso:: Functions :func:`recserar`, :func:`recsercp`
