
dynargsTypes
==============================================

Purpose
----------------

Returns a vector containing the types of the dynamic arguments passed into the current procedure.

Format
----------------
.. function:: n = dynargsTypes()

    :return n: A vector containing the types of each dynamic argument passed into the current procedure. Each type will be represented by an integer as specified in the table below.

        **Data types:**

        .. csv-table::
            :widths: auto

            "matrix","6"
            "array,"21"
            "sparse matrix","38"
            "string,"13"
            "string array","15"
            "structure","17"
            "structure pointer","23"

    :rtype n: matrix


Examples
----------------

Basic example with no required inputs
++++++++++++++

::

    a = { 1, 2, 3, 4 };
    b = 7;
    c = "This is a string";

    // Call with 3 dynamic arguments
    dynargsTest(a, b, c);
    
    // Create example procedure which only
    // takes dynamic arguments
    proc (0) = dynargsTest(...);
       local t;
    
       // Find out the types of the dynamic
       // arguments which were passed in
       t = dynargsTypes();
    
       print "Dynamic argument types = " t;
    endp;

The above code will produce the following output:

::

    Dynamic argument types = 
    
     6
     6
    13

Basic example with one required input
++++++++++++++

::

    new;

    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    sparse matrix A;
    A = denseToSp(rndn(2,2), 0);

    // Call with 1 required argument and 2 dynamic arguments
    dynargsTest(1.5, myPlot, A);
    
    // Create example procedure which takes
    // 1 required argument, 'a', followed by
    // the dynamic arguments
    proc (0) = dynargsTest(a,...);
       local t;
    
       // Find out the types of the dynamic
       // arguments which were passed in
       t = dynargsTypes();
    
       print "Dynamic argument types = " t;
    endp;

The above code will print out the type for the second and third inputs which are the dynamic arguments.

::

    Dynamic argument types = 

    17
    38

Remarks
------------

* :func:`dynargsTypes` can only be called inside a GAUSS proc which accepts ``...`` as its final input. 
* Use :func:`dynargsGet` to access the dynamic arguments and assign them to local variables.
* Use :func:`dynargsCount`, or ``rows(dynargsTypes())`` to find out how many dynamic arguments were passed in.
  


.. seealso:: Functions :func:`dynargsGet`, :func:`dynargsCount`
