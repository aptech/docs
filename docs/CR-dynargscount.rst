
dynargsCount
==============================================

Purpose
----------------

Returns the number of dynamic arguments passed into the current procedure.

Format
----------------
.. function:: n = dynargsCount()

    :return n: The number of dynamic arguments passed into the current procedure.


Examples
----------------

Basic example with no required inputs
++++++++++++++

::

    // Call with 1 dynamic argument
    dynargsTest(1.5);

    // Call with 2 dynamic arguments
    dynargsTest(1.5, 2.5);

    // Call with 3 dynamic arguments
    dynargsTest(1.5, 2.5, 3.5);
    
    // Create example procedure which only
    // takes dynamic arguments
    proc (0) = dynargsTest(...);
       local n;
    
       // Find out how many dynamic
       // arguments were passed in
       n = dynargsCount();
    
       print "Number of dynamic arguments = " n;
       print "---------";
    endp;

The above code will call the ``dynargsTest`` procedure three times with different dynamic arguments. It will print out the following three sets of print statements:

::

    Number of dynamic arguments = 1
    ---------
    Number of dynamic arguments = 2
    ---------
    Number of dynamic arguments = 3
    ---------

Basic example with one required input
++++++++++++++

::

    // Call with the 1 required argument
    dynargsTest(1.5);

    // Call with 1 required argument and 1 dynamic argument
    dynargsTest(1.5, 2.5);

    // Call with 1 required argument and 2 dynamic arguments
    dynargsTest(1.5, 2.5, 3.5);
    
    // Create example procedure which takes
    // 1 required argument, 'a', followed by
    // the dynamic arguments
    proc (0) = dynargsTest(a,...);
       local n;
    
       // Find out how many dynamic
       // arguments were passed in
       n = dynargsCount();
    
       print "Number of dynamic arguments = " n;
       print "---------";
    endp;

This time the printout will be the same, except that each number will be one less than in the previous example. This is because the first argument is required this time. 

::

    Number of dynamic arguments = 0
    ---------
    Number of dynamic arguments = 1
    ---------
    Number of dynamic arguments = 2
    ---------

Remarks
------------

* :func:`dynargsCount` can only be called inside a GAUSS proc which accepts ``...`` as its final input. 
* Use :func:`dynargsGet` to access the dynamic arguments and assign them to local variables.
* You can find out the types of the dynamic arguments by calling :func:`dynargsTypes`.
  


.. seealso:: Functions :func:`dynargsGet`, :func:`dynargsTypes`
