
isstructype
==============================================

Purpose
----------------

Returns 1 if structure matches the input type.

Format
----------------
.. function:: structure_matches = isStructType(struct_instance, struct_type)

    :param struct_instance: Structure to check.
    :type struct_instance: Struct

    :param struct_type: Structure type to check for.
    :type struct_type: String
    
    :return match: 1 if *struct_instance* is a structure of the type type specified by *struct_type*.
    :rtype match: Scalar

Examples
----------------

Basic usage
+++++++++++++

::

    // Create structure 
    struct plotControl plt;
    plt = plotGetDefaults("Bar");
    
    // Check if structure is olsmtControl
    isStructType(plt, "olsmtControl");

Because *plt* is a :class:`plotControl` structure this returns 0.

::

    // Now check for plotControl structure
    isStructType(plt, "plotControl");


This returns 1 because *plt* is a :class:`plotControl` structure. 

Create a function to handle different data types
+++++++++++++++++++++++++++++++++++++++++++++++++++++

:func:`isstructtype` can be used to verify data in your program and handle it appopriately.

In this example, we will create a function that will print our data differently whether it comes in as a numeric matrix, a PV structure or a DS structure. Our first step is to create the procedures to print the different data:

::

    proc (0) = printMatrix(p);
        print p;
    endp;
    
    proc (0) = printDSData(struct DS d);
        for i(1, rows(d), 1);
            print d[i].dataMatrix;
        endfor;
    endp;
    
    proc (0) = printPVData(struct PV p);
        print pvGetParNames(p);
        print pvGetParVector(p);
    endp;

Next we will create our main ``printData`` function that will check the input and call the correct print procedure:

::

    proc (0) = printData(p);
        if isStructType(p, "DS");
            print "DS structure passed in:";
            printDSData(p);
        elseif isStructType(p, "PV");
            print "PV structure passed in:";
            printPVData(p);
        else;
            print "Numeric vector passed in:";
            printMatrix(p);
        endif;
    endp;

Now let's try it out with different data:

::

    x = { -1.2, 0.83, 0.03 };
    
    printData(x);

::

    Numeric vector passed in:
    
          -1.2000000 
          0.83000000 
         0.030000000 

::

    struct DS data;
    data = reshape(data, 2, 1);
    data[1].dataMatrix = x;
    data[2].dataMatrix = 2 * x;

    printData(data);

::

    DS structure passed in:
    
          -1.2000000 
          0.83000000 
         0.030000000 
    
          -2.4000000 
           1.6600000 
         0.060000000 

::

    struct PV p1;
    p1 = pvPack(pvCreate(), x[1], "alpha");
    p1 = pvPack(p1, x[2], "beta");
    
    printData(p1);

::

    PV structure passed in:
    
          alpha[1,1] 
           beta[1,1] 
    
          -1.2000000 
          0.83000000



.. seealso:: Functions :func:`isstring`, :func:`type`
