
rndStateSkip
==============================================

Purpose
----------------

To advance a state vector by a specified number of values.

Format
----------------
.. function:: newState = rndStateSkip(numSkip, state)

    :param numSkip: the number of values to skip.
    :type numSkip: scalar

    :param state: opaque state vector
    :type state: vector

    :return newState: the advanced state.

    :type newState: Opaque vector

Examples
----------------

::

    seed = 9192834;
    
    // Create a state from the 118th substream of the
    // Wichmann-Hill RNG
    state = rndCreateState("wh-118", seed);
    
    // Create a new state that is advanced by 2 numbers.
    newState = rndStateSkip(2, state);
    
    // Create and compare numbers from the two state vectors
    { r, state } = rndu(4, 1, state };
    { r2, newState } = rndu(2, 1, newState);

::

         0.54973563 
    r =  0.81642451 
         0.68583300 
         0.09105558 
         
    r2 = 0.68583300 
         0.09105558

Technical Notes
---------------

This function applies ONLY to the MRG32K3A and Wichmann-Hill random number generators.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndn`, :func:`rndu`, :func:`rndBeta`, :func:`rndGamma`

