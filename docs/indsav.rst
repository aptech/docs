
indsav
==============================================

Purpose
----------------

Checks one string array against another and returns the indices of the first string array in the second string array.

Format
----------------
.. function:: indx = indsav(needle, haystack)

    :param needle: contains the values to be found in vector *haystack*
    :type needle: Nx1 string array

    :param haystack: searched for the corresponding elements of *needle*
    :type haystack: Mx1 string array

    :return indx: the values of *needle* in *haystack*.

    :rtype indx: Nx1 vector of indices

Examples
----------------

::

  // What elements to look for
  needle = "Maggie" $| "Bart" $| "Lisa";

  // Vector to look in
  haystack = "Homer" $| "Moe" $| "Bart" $| "Sideshow" $| "Lisa" $| "Milhouse" $| "Maggie";

  // Find locations of needle in haystack
  z = indsav(needle, haystack);

::

        7.0000000
    z = 3.0000000
        5.0000000


Remarks
-------

If no matches are found, those elements in the returned vector are set
to the GAUSS missing value code.

If there are duplicate elements in *haystack*, the index of the first match
will be returned.

.. seealso:: Functions :func:`indnv`, :func:`contains`, :func:`ismember`, :func:`rowcontains`