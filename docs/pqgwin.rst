
pqgwin
==============================================

Purpose
----------------

Sets the graphics viewer mode. 

.. NOTE:: This function is for use only with the deprecated PQG graphics.

Library
-------

pgraph

.. _pqgwin:
.. index:: pqgwin

Format
----------------

::

    pqgwin one;
    pqgwin many;

Examples
----------------

::

    pqgwin many;

Remarks
-------

If you call:

::

   pqgwin one

only a single viewer will be used. If you call
::

   pqgwin many

a new viewer will be used for each graph.

``pqgwin manual`` and ``pqgwin auto`` are supported for backwards compatibility, ``manual = one``, ``auto = many``.


Source
------

pgraph.src

.. seealso:: Functions :func:`setvwrmode`

