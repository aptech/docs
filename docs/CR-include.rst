
#include
==============================================

Purpose
----------------

Inserts code from another file into a GAUSS program.

Format
----------------
.. function:: #include filename 
			  #include "filename"

Examples
----------------

::

    #include  "/gauss/inc/cond.inc"

The command will cause the code in the program
            cond.inc to be merged into the current program at
 the point at which this statement appears.

.. seealso:: Functions :func:`run`, :func:`lineson`
