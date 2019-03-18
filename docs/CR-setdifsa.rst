
setdifsa
==============================================

Purpose
----------------
Returns the unique elements in one string vector that are not present in a second string vector.

Format
----------------
.. function:: setdifsa(sv1,  sv2)

    :param sv1: Nx1 or 1xN string vector.
    :type sv1: TODO

    :param sv2: Mx1 or 1xM string vector.
    :type sv2: TODO

    :returns: sy (*Lx1 vector containing all unique values that are in sv1 and are not in sv2*), sorted in ascending order.

Examples
----------------

::

    string sv1 = { "mary", "jane", "linda", "john" };
    string sv2 = { "mary", "sally" };
     
    sy = setdifsa(sv1,sv2);

Now sy is equal to:

::

    jane
    john
    linda

Source
++++++

setdif.src

.. seealso:: Functions :func:`setdif`
