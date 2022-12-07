
indcv
==============================================

Purpose
----------------

Checks one character vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: z = indcv(needle, haystack)

    :param needle: contains the elements to be found in vector *haystack*
    :type needle: Nx1 character vector

    :param haystack: searched for matches to the elements of *needle*
    :type haystack: Mx1 character vector

    :return z: of integers containing the indices of the corresponding element of *needle*
        in *haystack*.

    :rtype z: Nx1 vector

Examples
----------------

::

    newVars = { YEARS, BONUS, GENDER };
    needle = { AGE, PAY, SEX };
    haystack = { AGE, SEX, JOB, DATE, PAY };

    // Return the indices in 'haystack' of the items in 'needle'
    z = indcv(needle, haystack);

    // Replace AGE, PAY, SEX with YEARS, BONUS, GENDER
    haystack[z] = newVars;

After the code above:

::

            YEARS
           GENDER       1
    haystack =   JOB   z = 5
             DATE       2
            BONUS

Remarks
-------

If no matches are found for any of the elements in *needle*, then the
corresponding elements in the returned vector are set to the GAUSS
missing value code.

Both arguments will be forced to uppercase before the comparison.

If there are duplicate elements in *haystack*, the index of the first match
will be returned.


.. seealso:: Functions :func:`indnv`, :func:`indsav`
