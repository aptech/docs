
pvGetParVector
==============================================

Purpose
----------------

Retrieves parameter vector from structure of type PV.

Format
----------------
.. function:: pvGetParVector(p1)

    :param p1: 
    :type p1: an instance of structure of type PV

    :returns: p (*Kx1 vector*), parameter vector.

Remarks
-------

Matrices or portions of matrices (stored using a mask) are stored in the
structure of type PV as a vector in the p member.


Examples
----------------

::

    // Define 'PV' structure
    #include pv.sdf
    // Declare 'p1' as an instance of a 'PV' structure
    struct PV p1;
    
    // Initialize 'p1' with default values
    p1 = pvCreate;
    
    x = { 1 2,
          3 4 };
    
    // 1's indicate elements to pack into 'p1' parameter vector
    mask = { 1 1,
             0 0 };
     
    p1 = pvPackm(p1,x,"X",mask);
     
    print pvUnpack(p1,"X");

pvUnpack returns the entire value of x that was packed in. Therefore, the print
statement above, produces:

::

    1.000 2.000
     3.000 4.000

::

    print
     pvGetParVector(p1);

pvGetParVector returns only those elements indicated by the mask variable and therefore the
print statement above, returns:

::

    1.000
     2.000

Source
------

pv.src

