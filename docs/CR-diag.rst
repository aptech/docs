
diag
==============================================

Purpose
----------------

Creates a column vector from the diagonal of a matrix.

Format
----------------
.. function:: diag(x)

    :param x: 
    :type x: NxK matrix or L-dimensional array where the last two dimensions are NxK

    :returns: y (*min(N,K)x1 vector or L-dimensional array*) where the last two dimensions are min(N,K)x1.

Remarks
-------

If x is a matrix, it need not be square. Otherwise, if x is an array,
the last two dimensions need not be equal.

If x is an array, the result will be an array containing the diagonals
of each 2-dimensional array described by the two trailing dimensions of
x. In other words, for a 10x4x4 array, the result will be a 10x4x1 array
containing the diagonals of each of the 10 4x4 arrays contained in x.

diagrv reverses the procedure and puts a vector into the diagonal of a
matrix.


Examples
----------------
Get the diagonal from a matrix.

::

    rndseed 458716;			
    x = rndu(3,3);
    y = diag(x);
    print "x = " x;
    print "y = " y;

After the above code,

::

    x = 
    0.96748215 0.31791692 0.46520760 
    0.04558545 0.78613263 0.20528802 
    0.73825699 0.30528745 0.73350290 
    y = 
    0.96748215 
    0.78613263 
    0.73350290

Using diag function for a 3x4x4 dimensional array.

::

    x = rndn(48,1);
    
    //Reshape the 48x1 vector into a 3x4x4 dimensional array
    x = areshape(x, 3|4|4);
    d = diag(x);

Now x is equal to:

::

    Plane [1,.,.]
    
      0.082720153    -0.49502230    -0.40613944      1.9283280
       0.23583965    -0.24230946    -0.66047073    -0.73098141
       -1.1187279    -0.27867822     -1.7846293    -0.44603382
      0.030071777     -1.0387861     0.23768949    0.019151917
    
    Plane [2,.,.]
    
       -1.7238416     0.17660645    -0.14798006    0.072065419
        1.3685721    -0.11216325    -0.12985589      1.1816008
       0.63154571     -1.4945397     -1.7276380    -0.28275797
      -0.71832623     -1.3193506    -0.53934998    -0.78348484
    
    Plane [3,.,.]
    
      -0.71111209    -0.30818842    -0.38982318     -2.7205066
       -1.5455077    -0.27131853     0.98686691     0.10870999
       0.57916876      1.8180884     0.76104693      1.1237605
        1.0727710     -1.1071168      1.7443178     -1.0684433

and d is a 3x4x1 array containing the diagonals from x above.

::

    Plane [1,.,.]
    
         0.082720153
         -0.24230946
          -1.7846293
         0.019151917
    
    Plane [2,.,.]
    
          -1.7238416
         -0.11216325
          -1.7276380
         -0.78348484
    
    Plane [3,.,.]
    
         -0.71111209
         -0.27131853
          0.76104693
          -1.0684433

.. seealso:: Functions :func:`diagrv`
