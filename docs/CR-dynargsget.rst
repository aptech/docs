
dynargsGet
==============================================

Purpose
----------------

Returns specified dynamic arguments with the option to set default values.

Format
----------------
.. function:: dyn_1 = dynargsGet(idx)
              dyn_1 = dynargsGet(idx,dflt_1)
              { dyn_1, dyn_2 [, dyn_3] } = dynargsGet(idx, dflt_1, dflt_2 [, dflt_3]);

    :param idx: A scalar input specifies the index of the dynamic argument to return. A 2x1 matrix input
                specifies the start and end of the range of dynamic arguments to return. 
    :type idx: Scalar or 2x1 matrix
    :param dflt_1: Default values to be returned if the dynamic argument is not found. There must be one default
                   value passed in for each dynamic argument requested by the *idx* input, or not default values.
    :type dflt_1: Scalar, matrix, string, or any legal GAUSS variable type

    :return dyn_1: Either the corresponding dynamic argument or default value.

    :rtype m: Type of the dynamic argument or default 

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
       local a, b, c;
    
       // Return the first 3 dynamic arguments
       // or the default value provided below
       { a, b, c } = dynargsGet(1|3, 5, 10, 15);
    
       print "a = " a;
       print "b = " b;
       print "c = " c;
       print "---------";
    endp;

The above code will call the ``dynargsTest`` procedure three times with different dynamic arguments. It will print out the following three sets of print statements:

::

    a =        1.5000000 
    b =        10.000000 
    c =        15.000000 
    ---------
    a =        1.5000000 
    b =        2.5000000 
    c =        15.000000 
    ---------
    a =        1.5000000 
    b =        2.5000000 
    c =        3.5000000 
    ---------

Example with one required input and one optional input 
+++++++++++++++

In this example, the procedure requires one input, *length*. The second input, *width*, is an optional dynamic argument. If *width* is passed in,
then it is used to compute the area of the rectangle.

If the second argument is not passed in, then the procedure will compute the area of a square. This happens because the procedure sets the default value
for *width* to be equal to the first required input, *length*.

::

    square = area(3);
    rectangle = area(3, 2);
    
    // Procedure to compute the area of a rectangle
    proc (1) = area(length,...);
        local width;
        
        // If one or more dynamic arguments
        // are passed in, assign the first one
        // to 'width'.
        //
        // Otherwise, if no dynamic arguments
        // are passed in, assign the value of
        // 'length' to 'width'
        width = dynargsGet(1, length);
        
        retp(length * width);
    endp;


After the code above:

::

    square = 9
    rectangle = 6 



Example with one required input, one dynamic argument and no default value
+++++++++++++++++++++++++++++++++++++++

This example performs the same as the previous example, but does not pass in a default value to :func:`dynargsGet`.

::

    square = area(3);
    rectangle = area(3, 2);

    // Procedure to compute the area of a rectangle
    proc (1) = area(length,...);
        local width;
        
        // If one or more dynamic arguments
        // are passed in, assign the first one
        // to 'width'.
        //
        // Since a default value is not provided,
        // if no dynamic arguments are passed
        // in, 'width' will be an empty matrix
        width = dynargsGet(1);
        
        // Check to see if 'width' is an empty matrix
        if isempty(width);
            width = length;
        endif;
        
        retp(length * width);
    endp;


After this code is run, as in the previous example:

::

    square = 9
    rectangle = 6 

Remarks
------------

* :func:`dynargsGet` can only be called inside a GAUSS proc which accepts ``...`` as its final input. 
* If a requested dynamic argument is not passed in and no default values are provided, an empty matrix will be returned. This can be tested for with :func:`isempty`. See the examples.
* :func:`dynargsCount` will return the number of dynamic arguments passed in to the function.
* You can find out the types of the dynamic arguments by calling :func:`dynargsTypes`.
  


.. seealso:: Functions :func:`dynargsCount`, :func:`dynargsTypes`
