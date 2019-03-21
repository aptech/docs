
threadfor, threadendfor
==============================================

Purpose
----------------

Begins a parallel for loop.

Format
----------------
.. function:: threadfor i (start, stop, step) 
			      . 
			      . 
			      . 
			  threadendfor

    :param i: the name of the counter variable.
    :type i: literal

    :param start: the initial value of the counter.
    :type start: scalar expression

    :param stop: the final value of the counter.
    :type stop: scalar expression

    :param step: the increment value.
    :type step: scalar expression

Examples
----------------

//A basic 'threadfor' loop
threadfor i (1, 4, 1);
   print i;
threadendfor;
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    1.000
    2.000
    3.000
    4.000

Simple bootstrap of the mean of one variable
++++++++++++++++++++++++++++++++++++++++++++

::

    //Create fully pathed name of dataset
    dataset = getGAUSSHome() $+ "examples/fueleconomy.dat";
    
    //Load all contents of dataset
    x = loadd(dataset);
    
    //Extract 2nd column
    engine_disp = x[.,2];
    
    iters = 500;
    nobs = rows(engine_disp);
    
    //Pre-allocate vector to hold sample means
    sample_means = zeros(iters, 1);
    
    threadFor i(1, iters, 1);
        //Create tmp variable 'idx',
        //containing random integers from 1-nobs
        //'idx' exists ONLY during the loop
        idx = ceil(nobs * rndu(nobs, 1));
        
        //Extract random sample into tmp variable,
        //'sample'. Only exists during loop
        sample = engine_disp[idx];
        
        //Calculate mean of sample
        //and assign using loop counter
        //'sample_means' will persist after loop
        sample_means[i] = meanc(sample);
    threadEndFor;

.. seealso:: Functions 
considerations <MT-Multi-Threaded/MT-ThreadingPerformanceConsiderations.html>`__

parallel threading loop
