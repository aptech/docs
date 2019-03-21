
dtvnormal
==============================================

Purpose
----------------

Normalizes a date and time (DTV) vector.

Format
----------------
.. function:: dtvnormal(t)

    :param t: 
    :type t: 1x8 date and time vector that has
        one or more elements outside the normal range

    :returns: d (*TODO*), Normalized 1x8 date and time vector.

Examples
----------------

::

    format /rd 4,0;
    
    dStart = { 2011 08 21 6 21 37 0 0 };
    mnth = { 0 1 0 0 0 0 0 0 };
    
    //Add 6 months to 'dStart' which will give a 14 for the 
    //month
    dEnd = dStart + 6*mnth;
    
    //Normalize the date vector
    dEnd2 = dtvnormal(dEnd);

After the code above:

::

    dEnd  = 2011   14   21    6   21   37    0    0 
    dEnd2 = 2012    2   21    6   21   37    2   51

.. seealso:: Functions :func:`date`, :func:`ethsec`, :func:`etstr`, :func:`time`, :func:`timestr`, :func:`timeutc`, :func:`utctodtv`
