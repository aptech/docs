
return
==============================================

Purpose
----------------
Returns from a subroutine.

.. _return:
.. index:: return

Format
----------------

::

    return;
    return(x, y, ...);

Remarks
-------

The number of items that may be returned from a subroutine in a return
statement is limited only by stack space. The items may be expressions.
Items are separated by commas.

It is legal to return with no arguments and therefore return nothing.

.. seealso:: `gosub`, `pop`

