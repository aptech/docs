
pvGetParVector
==============================================

Purpose
----------------

Retrieves parameter vector from structure of type :class:`PV`.

Format
----------------
.. function:: p = pvGetParVector(p1)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :return p: parameter vector.

    :rtype p: Kx1 vector

Examples
----------------

::

    // Declare 'p1' as an instance of a 'PV' structure
    struct PV p1;

    // Initialize 'p1' with default values
    p1 = pvCreate;

    x = { 1 2,
          3 4 };

    // 1's indicate elements to pack into 'p1' parameter vector
    mask = { 1 1,
             0 0 };

    p1 = pvPackm(p1, x, "X", mask);

    print pvUnpack(p1, "X");

:func:`pvUnpack` returns the entire value of *x* that was packed in. Therefore, the `print`
statement above, produces:

::

     1.000 2.000
     3.000 4.000

::

     print pvGetParVector(p1);

:func:`pvGetParVector` returns only those elements indicated by the mask variable and therefore the
`print` statement above, returns:

::

     1.000
     2.000

Remarks
-------

Matrices or portions of matrices (stored using a mask) are stored in the
structure of type :class:`PV` as a vector in the p member.


Source
------

pv.src
