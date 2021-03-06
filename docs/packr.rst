
packr
==============================================

Purpose
----------------
Deletes the rows of a matrix that contain any missing values.

Format
----------------
.. function:: y = packr(x)

    :param x: data
    :type x: NxK matrix

    :return y: Matrix of *x* containing only those rows
        that do not have missing values in any of their elements.

    :rtype y: LxK matrix

Examples
----------------

Example 1: Basic example
++++++++++++++++++++++++

::

    // Create a 5x3 matrix with missing values
    x = {  1  2  3,
           4  .  6,
           .  8  .,
          10 11 12,
           . 14  5 };

    // Remove all rows which contain a missing value
    x_trim = packr(x);

After the code above, *x_trim* will equal:

::

    x_trim =  1  2  3
             10 11 12


Example 2
+++++++++

::

    // Set the rng seed for repeatable random numbers

    rndseed 7342692;

    // Create a 3x3 matrix of random integers between 1 and 10
    x = ceil(rndu(3, 3) * 10);

    // Turn all elements with a value of 8 into missing values
    x2 = miss(ceil(rndu(3, 3)*10), 8);

    // Remove all rows that contain missing values
    y = packr(x2);

After the code above:

::

        6 10  3          6 10  3
    x = 8  7  8     x2 = .  7  .     y = 6 10 3
        8  6  7          .  6  7


Example 3
+++++++++

::

    // Open a GAUSS data file for reading

    open fp = mydata;
    obs = 0;
    sum = 0;

    // Continue looping until the end of the file has been
    // reached
    do until eof(fp);
       // Read in 100 lines of the data file and remove any rows
       // with missing values
       x = packr(readr(fp, 100));
       
       // Check to see if 'packr' returned a missing value; if
       // not, update 'obs' and 'sum'
       if not scalmiss(x);
         obs = obs + rows(x);
         sum = sum + sumc(x);
       endif;
    endo;
    mean = sum/obs;

In this example the sums of each column in a data
file are computed as well as a count of the rows
that do not contain any missing values. :func:`packr` is
used to delete rows that contain missings and
:func:`scalmiss` is used to skip the two sum steps if all
the rows are deleted for a particular iteration of
the read loop. Then the sums are divided by the
number of observations to obtain the means.

Remarks
-------

This function is useful for handling missing values by "listwise
deletion," particularly prior to using the ``/`` operator to compute least
squares coefficients.

If all rows of a matrix contain missing values,:func:` packr` returns a scalar
missing value. This can be tested for quickly with the :func:`scalmiss` function.


.. seealso:: Functions :func:`impute`, :func:`scalmiss`, :func:`miss`, :func:`missrv`
