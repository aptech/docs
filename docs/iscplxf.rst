
iscplxf
==============================================

Purpose
----------------

Returns whether a dataset is complex or real.

Format
----------------
.. function:: fh_iscplx = iscplxf(fh)

    :param fh: file handle of an open file.
    :type fh: scalar

    :return fh_iscplx: 1 if the dataset is complex, 0 if it is real.

    :rtype fh_iscplx: scalar

Examples
----------------

::

    // Open a dataset file
    open fh = mydata.dat;

    // Check if the dataset contains complex data
    result = iscplxf(fh);
    print result;

    fh = close(fh);

.. seealso:: Functions :func:`hasimag`, :func:`iscplx`
