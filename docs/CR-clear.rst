
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
    //Code that uses 'A' would be here
    //Free memory holding 'A'
    clear A;

.. seealso:: Functions :func:`clearg`, :func:`new`, :func:`show`, :func:`delete`
