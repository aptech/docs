
if, else, elseif
==============================================

Purpose
----------------

Controls program flow with conditional branching.

Format
----------------
.. function:: if scalar_expression                  
			   list of statementselseif scalar_expression                  
			   list of statementselseif scalar_expression                  
			   list of statementselse                  
			   list of statementsendif

Examples
----------------

::

    if x < 0;
       y = -1;
    elseif x > 0;
       y = 1;
    else;
       y = 0;
    endif;

.. seealso:: Functions :func:`do`

| 
