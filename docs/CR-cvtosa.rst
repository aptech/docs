
cvtosa
==============================================

Purpose
----------------

Converts an NxK character vector to an NxK string array.

Format
----------------
.. function:: sa = cvtosa(cv)

    :param cv: Character vector to be converted to a string array.
    :type cv: NxK vector

    :return sa: contains the contents of *cv*.

    :rtype sa: NxK string array

Examples
----------------

::

    cv = { MEAN MEDIAN MODE, MAX  MIN  QUARTILE };
    sa = cvtosa(cv);
    print sa;

Now the variable *sa* is a string array with the same contents as *cv* as we can see from the output below:

::

    MEAN   MEDIAN   MODE
    MAX    MIN      QUARTILE

.. seealso:: Functions :func:`stocv`, :func:`vget`, :func:`vlist`, :func:`vput`, :func:`vread`
