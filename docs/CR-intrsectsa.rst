
intrsectsa
==============================================

Purpose
----------------

Returns the intersection of two string vectors, with duplicates removed.

.. NOTE:: This function is deprecated, use :func:`intrsect` instead.

Format
----------------
.. function:: y = intrsectsa(sv1, sv2)

    :param sv1: data
    :type sv1: Nx1 or 1xN string vector

    :param sv2: data
    :type sv2: Mx1 or 1xM string vector

    :return s_intr: all unique strings that are in both *sv1* and *sv2* sorted in ascending order.

    :rtype s_intr: Lx1 vector

Remarks
-------

#. Place smaller vector first for fastest operation.
#. If there are a lot of duplicates it is faster to remove them with
   :func:`unique` before calling :func:`intrsectsa`.


Examples
----------------

::

    // Define string vector number one
    vars_a = "age" $| "weight" $| "bmi";

    // Define string vector number two
    vars_b = "hdl" $| "ldl" $| "age" $| "bmi" $| "smoking";

    shared_vars = intrsectsa(vars_a, vars_b);
    print "Both studies reported the following variables:";
    print shared_vars;

The code above returns:

::

    Both studies reported the following variables:
                 age              bmi

Source
------

intrsect.src

.. seealso:: Functions :func:`intrsect`
