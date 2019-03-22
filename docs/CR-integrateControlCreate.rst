
integrateControlCreate
==============================================

Purpose
----------------

Fills an integrateControl structure with default settings.

Format
----------------
.. function:: integrateControlCreate()

    :returns: c (*struct*) instance of :class:`integrateControl` struct with members set to default values.

Examples
----------------

::

    //Declare 'ctl' as an instance of an 
    //'integrateControl' structure
    struct integrateControl ctl;
    
    //Fill with default settings
    ctl = integrateControlCreate();

Source
------

integrate.src

.. seealso:: Functions :func:`integrate1d`

default integrateControl structure integrate1d integrate integrations
