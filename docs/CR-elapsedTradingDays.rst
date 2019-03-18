
elapsedTradingDays
==============================================

Purpose
----------------

Computes number of trading days between two dates inclusively.

Format
----------------
.. function:: elapsedTradingDays(a,  b)

    :param a: date in DT scalar format.
    :type a: scalar

    :param b: date in DT scalar format.
    :type b: scalar

    :returns: n (*number of trading days between dates inclusively*), that is,
        elapsed time includes the dates  a and  b.

Examples
----------------

::

    //September 10, 2015
    tStart = 20150910110231;
    
    //September 28, 2015
    tEnd = 20150928080722;
    
    nDays = elapsedTradingDays(tStart, tEnd);

::

    nDays = 12

Source
++++++

finutils.src

Globals
+++++++

\_fin_holidays

.. seealso:: Functions :func:`getNextTradingDay`, :func:`getPreviousTradingDay`, :func:`getNextWeekDay`, :func:`getPreviousWeekDay`
