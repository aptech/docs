
dummy
==============================================

Purpose
----------------

Creates a set of dummy (0/1) variables by breaking
up a variable into specified categories. The
highest (rightmost) category is unbounded on the
right.

Format
----------------
.. function:: dummy(x, v)

    :param x: Data that is to be broken up into dummy variables
    :type x: Nx1 vector

    :param v: Specifies the K-1 breakpoints (these must be in ascending order) that determine the K categories to be used. These categories should not overlap.
    :type v: (K-1)x1 vector

    :returns: **y** (*NxK matrix*) - contains the *K* dummy variables.

Remarks
-------

Missings are deleted before the dummy variables are created.

All categories are open on the left (i.e., do not contain their left
boundaries) and all but the highest are closed on the right (i.e., do
contain their right boundaries). The highest (rightmost) category is
unbounded on the right. Thus, only :math:`K-1` breakpoints are required to
specify *K* dummy variables.

The function :func:`dummybr` is similar to :func:`dummy`, but in that function the
highest category is bounded on the right. The function :func:`dummydn` is also
similar to :func:`dummy`, but in that function a specified column of dummies is
dropped.


Examples
----------------

::

    // Set seed for repeatable random numbers
    rndseed 135345;

    // Create uniform random integers between 1 and 9
    x = ceil(9*rndu(5, 1));

    // Set the breakpoints
    v = { 1, 5, 7 };

    dm = dummy(x, v);

The code above produces four dummies based upon the breakpoints in the vector *v*:

::

    x < 1
    1 < x < 5
    5 < x < 7
    7 < x

which look like:

::

         0 1 0 0       2
         0 0 0 1       9
    dm = 0 1 0 0   x = 4
         0 0 1 0       7
         1 0 0 0       1

Source
------

datatran.src

.. seealso:: Functions :func:`dummybr`, :func:`dummydn`, `code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`reclassify`
