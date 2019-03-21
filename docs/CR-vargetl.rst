
vargetl
==============================================

Purpose
----------------
Accesses a local variable whose name is given as a string argument.

Format
----------------
.. function:: vargetl(s)

    :param s: 
    :type s: string containing the name of the local symbol you wish to access

    :returns: y (*TODO*), contents of the variable whose name is
        in  s.

Examples
----------------

::

    proc rndNormEx( r, c, loc, std, ptVar);
    local rnd1, rnd2, rnd3;
    	
    //Create random normal numbers with mean 0 and standard 
    //deviation 1
    rnd1 = rndn(r, c);
    
    //Change the mean to 'loc'
    rnd2 = rnd1 + loc;
    	
    //Change the standard deviation to 'std'
    rnd3 = std * rnd2;
    
    //Set the contents of tmp to be equal to the contents of 
    //the local variable with the same name as the string 
    //passed in as 'ptVar'
    tmp = vargetl(ptVar);
    	
       print ptVar " is equal to: " tmp;
    	
       retp(rnd3);
    endp;
    
    //Set the rng seed for repeatable results
    rndseed 54223423;
    
    //Passing in the final variable as the string rnd1, will 
    //cause the proc rndNormEx to print the contents of rnd1
    r = rndNormEx( 2, 2, 0, 3, "rnd1");

The code above will produce the following output:

::

    rnd1 is equal to: 
     0.5240627925408163  1.4904799236486497 
    -1.1716182730350617 -0.0519353312479753

.. seealso:: Functions :func:`varputl`
