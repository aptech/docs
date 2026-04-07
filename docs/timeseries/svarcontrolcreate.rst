svarControlCreate
==================

Purpose
-------
Initialize an :class:`svarControl` structure with default values for use with :func:`svarIrf` and :func:`svarIrfNarr`.

Format
------

.. function:: adv = svarControlCreate()

   :return adv: An instance of an :class:`svarControl` structure with the following members:

       .. include:: include/svarcontrol.rst

   :rtype adv: struct

Examples
--------

Default Settings
++++++++++++++++

::

    new;
    library timeseries;

    struct svarControl adv;
    adv = svarControlCreate();

Adding Zero Restrictions
++++++++++++++++++++++++

::

    new;
    library timeseries;

    struct svarControl adv;
    adv = svarControlCreate();

    // Zero restriction: shock 1 has no contemporaneous
    // effect on variable 3
    adv.zero_restr = { 3 1 0 };

Adding Narrative Restrictions
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    struct svarControl adv;
    adv = svarControlCreate();

    // Narrative restriction: shock 3 was positive at obs 84
    // [type, variable, shock, date1, date2, sign]
    adv.narrative_restr = { 1 3 3 84 0 1 };

Remarks
-------

The :class:`svarControl` structure is optional. When only sign restrictions
are needed, :func:`svarIrf` can be called without it. The advanced structure
is required when using zero restrictions or narrative restrictions, or when
overriding default algorithm settings.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`svarIrf`, :func:`svarIrfNarr`
