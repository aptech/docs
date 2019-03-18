
close
==============================================

Purpose
----------------
Closes a GAUSS file.

Format
----------------
.. function:: close(handle)

    :param handle: the file handle given to the file when it was opened with the open,
        create, or fopen command.
    :type handle: scalar

    :returns: y (*scalar*), 0 if successful, -1 if unsuccessful.

Examples
----------------

::

    new;				
    cls;
    
    // Create 'mydata' matrix				
    mydata = seqa(1,1,3);
    
    // Using saved function to save mydata matrix into 'mydata.dat' file				
    saved(mydata,"mydata.dat","x");
    
    // Set a random seed				 
    rndseed 855;
    
    // Open 'mydata.dat' file				
    open f1 = mydata for append;
    
    // Create an appended data set 'x'				
    x = rndu(3,1);
    
    y = writer(f1,x);
    f1 = close(f1);
    
    data_new = loadd("mydata.dat");
    
    print "mydata = " mydata;
    print "x = " x;
    print "data_new = " data_new;

After running above code,

::

    1.0000000 
    mydata = 
    	1.0000000 
    	2.0000000 
    	3.0000000 
    x = 
    	0.33589398 
    	0.62804541 
    	0.017829664 
    data_new = 
    	1.0000000 
    	2.0000000 
    	3.0000000 
    	0.33589398 
    	0.62804541 
    	0.017829664

The first 1 means the "mydata.dat" file is closed.

.. seealso:: Functions :func:`closeall`
