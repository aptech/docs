
clearg
==============================================

Purpose
----------------

Clears global symbols by setting them equal to scalar zero.

Format
----------------
.. function:: clearg a, b, c

    :return a: global matrix containing 0.
    :type a: scalar

    :return b: global matrix containing 0.
    :type b: scalar

    :return c: global matrix containing 0.
    :type c: scalar

Remarks
-------

It is considered a best practice to avoid using global variables inside
of procedures when possible.

::

   clearg x;

is equivalent to
::

   x = 0;

where *x* is understood to be a global symbol. :func:`clearg` can be used to
initialize symbols not previously referenced. This command can be used
inside of procedures to clear global matrices. It will ignore any locals
by the same name.

.. seealso:: `clear`, `delete`, `new`, :func:`show`, `local`
