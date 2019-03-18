
dstatmtControlCreate
==============================================

Purpose
----------------

Fills a dstatmtControl structure with default settings.

Format
----------------
.. function:: dstatmtControlCreate()

    :returns: c (*TODO*), instance of dstatmtControl structure with members set to default values.

Examples
----------------

::

    //Declare 'dsm' as an instance of a 
    //'dstatmtControl' structure
    struct dstatmtControl dsm;
    
    //Apply default values to 'dsm'
    dsm = dstatmtControlCreate();

Source
++++++

dstatmt.src

.. seealso:: Functions :func:`dstatmt`

default dstatmtControl structure dstatmt descriptive statistics
