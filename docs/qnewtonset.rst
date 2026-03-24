
QNewtonSet
==============================================

Purpose
----------------
Resets global variables used by :func:`QNewton` to default values.

Format
----------------
.. function:: QNewtonSet()

Examples
--------

::

    // Change QNewton global settings
    _qn_MaxIters = 500;
    _qn_PrintIters = 1;
    _qn_RelGradTol = 1e-8;

    // ... run QNewton optimization ...

    // Reset all QNewton globals to defaults
    QNewtonSet();

Source
------

qnewton.src

