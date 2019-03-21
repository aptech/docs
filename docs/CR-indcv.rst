
indcv
==============================================

Purpose
----------------

Checks one character vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: indcv(what, where)

    :param what: 
    :type what: Nx1 character vector which contains the elements to be found in vector
        where

    :param where: 
    :type where: Mx1 character vector to be searched for matches to the elements of what

    :returns: z (*TODO*), Nx1 vector of integers containing the indices of the corresponding element of what
        in  where.

Examples
----------------

::

    let newVars = YEARS BONUS GENDER;
    let what = AGE PAY SEX;
    let where = AGE SEX JOB DATE PAY;
    
    //Return the indices in 'where' of the items in 'what'
    z = indcv(what,where);
    
    //Replace AGE, PAY, SEX with YEARS, BONUS, GENDER
    where[z] = newVars;

After the code above:

::

    YEARS
           GENDER       1
    where =   JOB   z = 5
             DATE       2
            BONUS

.. seealso:: Functions :func:`indnv`, :func:`indsav`
