
threadfor, threadendfor
==============================================

Purpose
----------------

Begins a parallel for loop.

.. _threadfor:
.. _threadendfor:
.. index:: threadfor, threadendfor

Format
----------------

::

    threadfor i (start, stop, step);
      .
      .
      .
    threadendfor;

**Parameters**

:i: (*literal*) the name of the counter variable.
:start: (*scalar*) the initial value of the counter.
:stop: (*scalar*) the final value of the counter.
:step: (*scalar*) the increment value.

Examples
----------------

Example 1
+++++++++

::

    // A basic 'threadfor' loop
    threadfor i (1, 4, 1);
        print i;
    threadendfor;

The code above, will print out:

::

    1.000
    2.000
    3.000
    4.000

Simple bootstrap of the mean of one variable
++++++++++++++++++++++++++++++++++++++++++++

::

    // Create fully pathed name of dataset
    dataset = getGAUSSHome() $+ "examples/fueleconomy.dat";

    // Load all contents of dataset
    x = loadd(dataset);

    // Extract 2nd column
    engine_disp = x[., 2];

    iters = 500;
    nobs = rows(engine_disp);

    // Pre-allocate vector to hold sample means
    sample_means = zeros(iters, 1);

    threadFor i(1, iters, 1);
        // Create tmp variable 'idx',
        // containing random integers from 1-nobs
        //'idx' exists ONLY during the loop
        idx = ceil(nobs * rndu(nobs, 1));

        // Extract random sample into tmp variable,
        //'sample'. Only exists during loop
        sample = engine_disp[idx];

        // Calculate mean of sample
        // and assign using loop counter
        //'sample_means' will persist after loop
        sample_means[i] = meanc(sample);
    threadEndFor;

Remarks
-------

#. The iterations of a `threadfor` loop may execute in any order.
#. Indexed assignments to global variables that use the loop counter
   behave the same as in a standard `for` loop.
#. Non-indexed assignments will create a temporary variable that
   persists only through the remainder of the current loop iteration.
   For example:

   ::

       a = 34.7;
       threadfor i(1, 2, 1);
           a = rndu(1,1);
           print a;
       threadEndfor;

       print a;

   will produce output similar to the following:

   ::

       0.90560157
       0.52594285
       34.700000

#. `threadfor` loops may not be nested
#. Debugging inside of `threadfor` loops is currently not supported.


.. seealso:: `Performance considerations`
