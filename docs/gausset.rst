
gausset
==============================================

Purpose
----------------

Resets the global control variables declared in :file:`gauss.dec`.

Format
----------------
.. function:: gausset

Globals
-------

``__altnam``, ``__con``, ``__ff``, ``__fmtcv``, ``__fmtnv``, ``__header``, ``__miss``,
``__output``, ``__row``, ``__rowfac``, ``__sort``, ``__title``, ``__tol``, ``__vpad``,
``__vtype``, ``__weight``

Example
-------

::

    // Reset all global control variables to defaults
    __output = 0;
    __con = 1;
    gausset;
    // __output and __con are now back to their default values

Source
------

gauss.src

