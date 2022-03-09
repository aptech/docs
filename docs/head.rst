
head
=================

Purpose
--------------------

Returns the first ``n`` rows of a matrix, dataframe or string array.

Format
-----------------

.. function:: h = head(X)
              h = head(X, n)

       :param X:  the data to preview.
       :type X:   Matrix, dataframe or string array

       :param n:   Optional input, the number of rows to return. Default = 5.  If a negative number is supplied, all except the first n rows will be returned.
       :type n:   Scalar

       :return h:  The first n rows of X (or all but the first n rows of X, if n is negative).
       :rtype h:   Matrix, dataframe or string array


Examples
----------------

::

      X = { 11 14,
            27 19,
            44 12,
            81 17,
            23 22,
            14 43 };

      head(X);


The above code will print:

::

      11.000000        14.000000 
      27.000000        19.000000 
      44.000000        12.000000 
      81.000000        17.000000 
      23.000000        22.000000

::

    head(X, 3);

will print out:

::

      11.000000        14.000000 
      27.000000        19.000000 
      44.000000        12.000000

::

    head(X, -2);

will print out:

::

      44.000000        12.000000 
      81.000000        17.000000 
      23.000000        22.000000
      14.000000        43.000000

.. sealso:: Functions: :func:`rows`, :func:`tail`
