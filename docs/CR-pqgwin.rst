
pqgwin
==============================================

Purpose
----------------

Sets the graphics viewer mode. NOTE: This function is for use only with the deprecated PQG graphics.

Format
----------------
.. function:: pqgwin one 
			  pqgwin many

Remarks
-------

If you call:

::

   pqgwin one

only a single viewer will be used. If you call
::

   pqgwin many

a new viewer will be used for each graph.
pqgwin manual and pqgwin auto are supported for backwards compatibility,
manual = one, auto = many.


Examples
----------------

::

    pqgwin many;

Source
------

pgraph.src

.. seealso:: Functions :func:`setvwrmode`
