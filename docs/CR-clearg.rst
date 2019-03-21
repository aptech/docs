
clearg
==============================================

Purpose
----------------

Clears global symbols by setting them equal to scalar zero.

Format
----------------
.. function:: clearg a, b, c

    :returns: a,b,c (*scalar*), scalar global matrices containing 0.

Remarks
-------

.. raw:: html

   <div id="Remarks">

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

.. seealso:: :func:`clear`, :func:`delete`, :func:`new`, :func:`show`, :func:`local`

