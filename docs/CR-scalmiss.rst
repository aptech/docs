
scalmiss
==============================================

Purpose
----------------
Tests to see if its argument is a scalar missing value.

Format
----------------
.. function:: scalmiss(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*scalar*), 1 if argument is a scalar missing value, 0 if not.

Remarks
-------

scalmiss first tests to see if the argument is a scalar. If it is not
scalar, scalmiss returns a 0 without testing any of the elements.

To test whether any element of a matrix is a missing value, use ismiss.
scalmiss will execute much faster if the argument is a large matrix,
since it will not test each element of the matrix but will simply return
a 0.

An element of x is considered to be a missing if and only if it contains
a missing value in the real part. Thus, scalmiss and scalmiss would
return a 1 for complex x = . + 1i, and a 0 for x = 1 + .i.


Examples
----------------

::

    clear s;
    do until eof(fp);
       y = readr(fp,nr);
       y = packr(y);
       if scalmiss(y);
          continue;
       endif;
       s = s+sumc(y);
    endo;

In this example the packr function will return a scalar missing if
every row of its argument contains missing values, otherwise it will
return a matrix that contains no missing values. scalmiss is used
here to test for a scalar missing returned from packr. If the test returns
true, then the sum step will be skipped for that iteration of the
read loop because there were no rows left after the rows containing
missings were packed out.

