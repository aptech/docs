
trace
==============================================

Purpose
----------------
Allows the user to trace program execution for debugging purposes.

Format
----------------
.. function:: trace new 
			  trace new, mask

    :param new: new value for trace flag.
    :type new: scalar

    :param mask: optional mask to allow leaving some bits
        of the trace flag unchanged.
    :type mask: scalar

Examples
----------------

::

    trace 1+8;    //trace fn/proc calls/returns to standard 
                  //output 
    trace 2+8;    //trace line numbers to standard output 
    trace 1+2+8;  //trace line numbers and fn/proc calls/
                  //returns to standard output
    trace 1+16;   //trace fn/proc calls/returns to printer 
    trace 2+16;   //trace line numbers to printer
    trace 1+2+16; //trace line numbers and fn/proc calls/ 
                  //returns to printer

.. seealso:: Functions :func:`lineson`
