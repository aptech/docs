
dummybr
==============================================

Purpose
----------------

Creates a set of dummy (0/1) variables. The highest (rightmost) category is bounded on the right.

Format
----------------
.. function:: dummybr(x, v)

    :param x: data that is to be broken up into dummy variables
    :type x: Nx1 vector

    :param v: specifies the :math:`K` breakpoints (these must be in ascending order) that determine the :math:`K` categories to be used. These categories should not overlap.
    :type v: Kx1 vector

    :returns: **y** (*NxK matrix*) - containing the :math:`K` dummy variables. Each row will have a maximum of one 1.

Remarks
-------

Missings are deleted before the dummy variables are created.

All categories are open on the left (i.e., do not contain their left
boundaries) and are closed on the right (i.e., do contain their right
boundaries). Thus, :math:`K` breakpoints are required to specify :math:`K` dummy
variables.

The function :func:`dummy` is similar to :func:`dummybr`, but in that function the
highest category is unbounded on the right.


Examples
----------------

::

    // Set seed for repeatable random numbers
    rndseed 135345;

    // Create uniform random integers between 1 and 9
    x = ceil(9*rndu(5, 1));

    // Set the breakpoints
    v = { 1, 5, 7 };

    dm = dummybr(x, v);

The code above produces three dummies based upon the breakpoints in the vector *v*:

::

    x < 1
    1 < x < 5
    5 < x < 7

which look like:

::

         0 1 0       2
         0 0 0       9
    dm = 0 1 0   x = 4
         0 0 1       7
         1 0 0       1

Source
------

datatran.src

.. seealso:: Functions :func:`dummydn`, :func:`dummy`, `code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`reclassify`
