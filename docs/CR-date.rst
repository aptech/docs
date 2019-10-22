
date
==============================================

Purpose
----------------

Returns the current date in a 4-element column
vector, in the order: year, month, day, and
hundredths of a second since midnight.

Format
----------------
.. function:: y = date()

Examples
----------------

::

    print date();

::

       2019.0 
          7.0 
         16.0 
    4571524.7

Remarks
-------

The hundredths of a second since midnight can be accessed using :func:`hsec`.

.. seealso:: Functions :func:`time`, :func:`timestr`, :func:`ethsec`, :func:`hsec`, :func:`etstr`

