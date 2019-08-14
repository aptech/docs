
dummydn
==============================================

Purpose
----------------

Creates a set of dummy (0/1) variables by breaking
up a variable into specified categories. The
highest (rightmost) category is unbounded on the
right, and a specified column of dummies is dropped.

Format
----------------
.. function:: dummydn(x, v, p)

    :param x: data to be broken up into dummy variables
    :type x: Nx1 vector

    :param v: Specifies the :math:`K - 1` breakpoints (these must be in ascending order) that determine the :math:`K` categories to be used. These categories should not overlap.
    :type v: (K-1)x1 vector

    :param p: positive integer in the range :math:`[1, K]`, specifying which column should be dropped in the matrix of dummy variables.
    :type p: scalar

    :returns: **y** (*Nx(K-1) matrix*) - contains the :math:`K-1` dummy variables.

Remarks
-------

* This is just like the function :func:`dummy`, except that the pth column of the
  matrix of dummies is dropped. This ensures that the columns of the
  matrix of dummies do not sum to 1, and so these variables will not be
  collinear with a vector of ones.

* Missings are deleted before the dummy variables are created.

* All categories are open on the left (i.e., do not contain their left
  boundaries) and all but the highest are closed on the right (i.e., do
  contain their right boundaries). The highest (rightmost) category is
  unbounded on the right. Thus, only :math:`K-1` breakpoints are required to
  specify *K* dummy variables.


Examples
----------------

::

    // Set seed for repeatable random numbers
    rndseed 135345;

    // Create uniform random integers between 1 and 9
    x = ceil(9*rndu(5, 1));

    // Set the breakpoints
    v = { 1, 5, 7 };

    // Column to drop
    p = 2;

    dm = dummy(x,v);
    dm_dn = dummydn(x,v,p);

The code above produces four dummies based upon the breakpoints in the vector *v*:

::

    x <= 1
    1 < x <= 5 // Since p = 2, this column is dropped
    5 < x <= 7
    7 < x

and then remove the *p*'th column which will result in:

::

         0 1 0 0           0 0 0       2
         0 0 0 1           0 0 1       9
    dm = 0 1 0 0   dm_dn = 0 0 0   x = 4
         0 0 1 0           0 1 0       7
         1 0 0 0           1 0 0       1

Source
------

datatran.src

.. seealso:: Functions :func:`dummy`, :func:`dummybr`, `code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`reclassify`
