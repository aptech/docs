
retp
==============================================

Purpose
----------------
Returns from a procedure or keyword.

.. _retp:
.. index:: retp

Format
----------------

::

    retp;
    retp(x, y,...);


Remarks
-------

For more details, see `Procedures and Keywords <PK-ProceduresandKeywords.html>`_.

In a `retp` statement 0-1023 items may be returned. The items may be
expressions. Items are separated by commas.

It is legal to return with no arguments, as long as the procedure is
defined to return 0 arguments.

Examples
--------

::

    // Procedure returning one value
    proc (1) = addOne(x);
        retp(x + 1);
    endp;

    y = addOne(5);
    print y;

::

    // Procedure returning two values
    proc (2) = minMax(x);
        retp(minc(x), maxc(x));
    endp;

    { lo, hi } = minMax(seqa(1, 1, 10));
    print lo hi;

.. seealso:: `proc`, `keyword`, `endp`

