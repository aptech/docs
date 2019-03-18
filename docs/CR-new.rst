
new
==============================================

Purpose
----------------

Erases everything in memory including the symbol table; closes all open files as well as the auxiliary output and turns
the window on if it was off; also allows the size of the new symbol table and the main program space to be specified.

Format
----------------
.. function:: new 
			  new nos

    :param nos: optional input which indicates the maximum number of global
        symbols allowed.
    :type nos: scalar

Examples
----------------

::

    new; /* clear global symbols. */

::

    new 300; /* clear global symbols,set maximum
             ** number of global symbols to 300,
             ** and leave program space unchanged.
             */

.. seealso:: Functions :func:`clear`, :func:`delete`, :func:`output`
