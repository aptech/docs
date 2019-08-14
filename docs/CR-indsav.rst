
indsav
==============================================

Purpose
----------------

Checks one string array against another and returns the indices of the first string array in the second string array.

Format
----------------
.. function:: indx = indsav(what, where)

    :param what: contains the values to be found in vector *where*
    :type what: Nx1 string array

    :param where: searched for the corresponding elements of *what*
    :type where: Mx1 string array

    :returns: **indx** (*Nx1 vector of indices*) - the values of *what* in *where*.

Examples
----------------

::

  // What elements to look for
  what = "Maggie" $| "Bart" $| "Lisa";

  // Vector to look in
  where = "Homer" $| "Moe" $| "Bart" $| "Sideshow" $| "Lisa" $| "Milhouse" $| "Maggie";

  // Find locations of what in where
  z = indsav(what, where);

::

        7.0000000
    z = 3.0000000
        5.0000000


Remarks
-------

If no matches are found, those elements in the returned vector are set
to the GAUSS missing value code.

If there are duplicate elements in where, the index of the first match
will be returned.
