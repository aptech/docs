
clear
==============================================

Purpose
----------------

Clears space in memory by setting matrices equal to scalar zero.

Format
----------------
.. function:: clear x, y

Examples
----------------

::

    A = rndn(1000, 1000);
    /*
    ** Code that uses 'A' would be here
    ** Free memory holding 'A'
    */
    clear A;

Remarks
-------


If your program is running out of memory, or uses considerable system
resources, using :func:`clear` to deallocate large matrices after they are no
longer needed may allow it to run more efficiently.

::

   clear x;

is equivalent to

::

   x = 0;

Matrix names are retained in the symbol table after they are cleared.

Matrices can be cleared even though they have not previously been
defined. :func:`clear` can be used to initialize matrices to scalar 0.

.. seealso:: Functions `clearg`, `new`, `show`, `delete`
