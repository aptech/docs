
closeall
==============================================

Purpose
----------------

Closes all currently open GAUSS files.

Format
----------------
.. function:: closeall 
			  closeall list_of_handles

Examples
----------------

::

    new;				
    cls;
    
    // Create 'mydata' matrix				
    mydata = seqa(1,1,3);
    
    // Using saved function to save mydata matrix into 'mydata.dat' file				
    saved(mydata,"mydata.dat","x");
    open f1 = dat1 for read;
    open f2 = dat1 for update;
    x = readr(f1,rowsf(f1));
    x = sqrt(x);
    call writer(f2,x);
    closeall f1,f2;
    				
    // Check the new data file
    mydata_new = loadd("mydata.dat");
    print "mydata = " mydata;
    print "x = " x;
    print "mydata_new = " mydata_new;

After running the above code,

::

    1.0000000 
    mydata = 
    	1.0000000 
    	2.0000000 
    	3.0000000 
    x = 
    	1.0000000 
    	1.4142136 
    	1.7320508 
    mydata_new = 
    	1.0000000 
    	1.4142136 
    	1.7320508

The first 1 means the "mydata.dat" file is closed.

.. seealso:: Functions :func:`close`, :func:`open`
