etsControlCreate
================

Purpose
-------
Create an :class:`etsControl` structure with default values.

Format
------

.. function:: ctl = etsControlCreate()

   :return ctl: An instance of an :class:`etsControl` structure with the following default values:

       .. include:: include/etscontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    ctl = etsControlCreate();
    ctl.period = 12;
    ctl.error = 0;      // additive error
    ctl.trend = 2;      // damped trend
    ctl.season = 1;     // additive seasonality

Remarks
-------

Set ``ctl.trend`` or ``ctl.season`` to ``-1`` to let the wrapper choose the
corresponding component automatically. Use :func:`etsFit` with this structure
for fixed or semi-automatic ETS fitting, or call :func:`autoEts` directly for
full automatic model selection.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsFit`, :func:`autoEts`
