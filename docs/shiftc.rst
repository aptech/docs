
shiftc
==============================================

Purpose
----------------
Shifts the columns of a matrix, or dataframe.

Format
----------------
.. function:: y = shiftc(x, s, f)

    :param x: data to be shifted
    :type x: NxK matrix or dataframe

    :param s: specifies the magnitude of the shift
    :type s: scalar or 1xN vector

    :param f: specifies the value to fill in
    :type f: scalar or 1xN vector

    :return y: shifted matrix
    :rtype y: NxK matrix

Examples
----------------

Example 1: Single with univariate time series lag
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    fname = getGAUSSHome("examples/beef_prices.csv");

    // Load all observations of all variables
    beef = loadd(fname);

    // Trim data to make smaller example set
    beef = beef[1:5,.];

    // Shift all columns of beef forward 2 rows
    // filling the extra rows with a missing value
    beef_lag = shiftc(beef, 2, miss());

After the above code:

::

      beef_lag =   date       beef_price
                      .                .
                      .                .
                 199201        116.64000
                 199202        114.49000
                 199203        111.11000


Example 2: Multiple lags with a single vector
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    data_name = getGAUSSHome("examples/mortgage_long_form.csv");

    // Load all variables from file
    mtg = loadd(data_name);

    // Preview first 7 rows of data
    head(mtg,7);


The first rows *mtg*:

::

           DATE             Rate         Maturity
     2000-01-07        8.1500000            30_yr
     2000-01-14        8.1800000            30_yr
     2000-01-21        8.2600000            30_yr
     2000-01-28        8.2500000            30_yr
     2000-02-04        8.2500000            30_yr
     2000-02-11        8.3600000            30_yr
     2000-02-18        8.3800000            30_yr

::

    // Select first 7 rows of 'Rate'
    rate = mtg[1:7,"Rate"];

    // Lags must be a row vector
    lags = { 0 1 2 4 };

    // Fill with missing values
    fill = {.};

    // Compute lags
    rate_lags = shiftc(rate, lags, fill);

Now *rate_lags* is equal to:

::

    Rate                Rate_2           Rate_3           Rate_4
    8.1500000                .                .                .
    8.2600000        8.1800000        8.1500000                .
    8.2500000        8.2600000        8.1800000                .
    8.2500000        8.2500000        8.2600000        8.1500000
    8.3600000        8.2500000        8.2500000        8.1800000
    8.3800000        8.3600000        8.2500000        8.2600000


Example 3: Replacing with value
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Data
    x = { 1 2 3,
          4 5 6,
          7 8 9 };

    // Amount to shift
    s = { 0 1 2 };

    // Value to fill in
    f = 0;

    // Shift the matrix
    y2 = shiftc(x, s, f);

Now *y2* is equal to:

::

     1.0000000        0.0000000        0.0000000
     4.0000000        2.0000000        0.0000000
     7.0000000        5.0000000        3.0000000

Remarks
-------

The shift is performed within each column of the matrix, vertically. If
the shift value is positive, the elements in the column will be moved
down. A negative shift value causes the elements to be moved up.
The elements that are pushed off the end of the column are lost, and
the fill value will be used for the new elements on the other end.

.. seealso:: Functions :func:`lagn`, :func:`shiftr`
