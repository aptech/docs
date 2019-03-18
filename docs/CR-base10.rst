
base10
==============================================

Purpose
----------------

Breaks number into a number of the form #.####... and a power of 10.

Format
----------------
.. function:: base10(x)

    :param x: number to break down.
    :type x: scalar

    :returns: M (*scalar*), in the range -10 < M < 10.

    :returns: P (*scalar*), integer power such that:
        M*10P = x

Examples
----------------

::

    { b, e } = base10(4500);

After the code above:

::

    b = 4.5  e = 3

and

::

    b*10^e = 4.5*10^3 = 4500

Source
++++++

base10.src

.. raw:: html

   </div>
