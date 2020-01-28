
integrateControlCreate
==============================================

Purpose
----------------

Fills an integrateControl structure with default settings.

Format
----------------
.. function:: c = integrateControlCreate()

    :return c: instance of :class:`integrateControl` struct with members set to default values.

    :rtype c: struct

Examples
----------------

::

    /*
    ** Declare 'ctl' as an instance of an
    ** 'integrateControl' structure
    */
    struct integrateControl ctl;

    // Fill with default settings
    ctl = integrateControlCreate();

Source
------

integrate.src

.. seealso:: Functions :func:`integrate1d`

default integrateControl structure integrate1d integrate integrations
