
cvtosa
==============================================

Purpose
----------------

Converts an NxK character vector to an NxK string array.

Format
----------------
.. function:: cvtosa(cv)

    :param cv: Character vector to be converted to a string array.
    :type cv: NxK vector

    :returns: **sa** (*NxK string array*) - contains the contents of  cv.

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
