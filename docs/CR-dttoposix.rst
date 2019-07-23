
dttoposix
==============================================

Purpose
----------------
Converts DT scalar format to POSIX date/time format (seconds since Jan 1, 1970).

Format
----------------
.. function:: dttoposix(dt)

    :param dt: DT scalar format.
    :type dt: NxK matrix

    :returns: **p_time** (*NxK matrix*) - date/times in POSIX format.

Examples
----------------

Full length DT Scalar
+++++++++++++++++++++

::

    // March 26th, 2001 at 08:51:18
    dt = 20010326085118;

    // Convert to seconds since Jan 1, 1970
    p_time = dttoposix(dt);

    print "p_time = " p_time;

The above code produces the following output:

::

    p_time = 985596678

Vector of short DT Scalars
+++++++++++++++++++++++++++

::

    // Create a 2x1 vector of
    // short DT Scalars
    // March 21, 2000
    // October 14, 2008
    dt = { 20000321,
           20081014 };

    // Convert to seconds since Jan 1, 1970
    p_time = dttoposix(dt);

    print "p_time = " p_time;

The above code produces the following output:

::

    p_time =  953596800 
             1223942400

Remarks
-------

In DT scalar format, 10:50:31 on July 15, 2010 is 20100703105031. A
posix scalar gives the number of seconds since or before January 1,
1970, UTC.

.. seealso:: Functions :func:`dttostr`, :func:`dttostrc`, :func:`posixtostrc`, :func:`strtodt`, :func:`strtodt`
