
indcv
==============================================

Purpose
----------------

Checks one character vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: z = indcv(what, where)

    :param what: contains the elements to be found in vector *where*
    :type what: Nx1 character vector

    :param where: searched for matches to the elements of *what*
    :type where: Mx1 character vector

    :return z: of integers containing the indices of the corresponding element of *what*
        in *where*.

    :rtype z: Nx1 vector

Examples
----------------

::

    newVars = { YEARS, BONUS, GENDER };
    what = { AGE, PAY, SEX };
    where = { AGE, SEX, JOB, DATE, PAY };

    // Return the indices in 'where' of the items in 'what'
    z = indcv(what, where);

    // Replace AGE, PAY, SEX with YEARS, BONUS, GENDER
    where[z] = newVars;

After the code above:

::

            YEARS
           GENDER       1
    where =   JOB   z = 5
             DATE       2
            BONUS

Remarks
-------

If no matches are found for any of the elements in *what*, then the
corresponding elements in the returned vector are set to the GAUSS
missing value code.

Both arguments will be forced to uppercase before the comparison.

If there are duplicate elements in *where*, the index of the first match
will be returned.


.. seealso:: Functions :func:`indnv`, :func:`indsav`
