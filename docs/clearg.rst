
clearg
==============================================

Purpose
----------------

Clears global symbols by setting them equal to scalar zero.

.. _clearg:
.. index:: clearg

Format
----------------
:: 

    clearg a, b, c;

Remarks
-------

It is considered a best practice to avoid using global variables inside
of procedures when possible.

::

   clearg x;

is equivalent to
::

   x = 0;

where *x* is understood to be a global symbol. `clearg` can be used to
initialize symbols not previously referenced. This command can be used
inside of procedures to clear global matrices. It will ignore any locals
by the same name.

Examples
--------

::

    x = 5;
    y = rndn(3, 3);
    z = "hello";

    print (x);

::

       5.0000000

::

    // Reset all three globals to scalar 0
    clearg x, y, z;

    print (x);

::

       0.0000000

After calling ``clearg``, each variable is reset to a scalar zero regardless of its previous type or dimensions.

.. seealso:: `clear`, `delete`, `new`, `show`, `local`

