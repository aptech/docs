svarControlCreate
=================

Purpose
-------
Create an :class:`svarControl` structure with default values for sign-restricted SVAR identification.

Format
------

.. function:: ctl = svarControlCreate()

   :return ctl: An instance of an :class:`svarControl` structure with the following default values:

       .. include:: include/svarcontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    struct svarControl ctl;
    ctl = svarControlCreate();

    // Define sign restrictions: [variable, shock, horizon, sign]
    // Monetary shock (shock 3): FFR up, GDP down, CPI down
    ctl.sign_restr = { 3 3 0  1,
                       1 3 0 -1,
                       2 3 0 -1 };

    // Increase max attempts for tight restrictions
    ctl.max_tries = 50000;
    ctl.n_ahead = 24;

Remarks
-------

The *sign_restr* and *zero_restr* fields are empty by default. At least
one sign restriction must be set before calling :func:`svarIdentify` or
:func:`svarIrf`.

Library
-------
timeseries

Source
------
svar.src

.. seealso:: Functions :func:`svarIdentify`, :func:`svarIrf`
