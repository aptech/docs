
scalmiss
==============================================

Purpose
----------------
Tests to see if its argument is a scalar missing value.

Format
----------------
.. function:: scalmiss(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*scalar*), 1 if argument is a scalar missing value, 0 if not.

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

