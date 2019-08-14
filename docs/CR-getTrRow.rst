
getTrRow
==============================================

Purpose
----------------

Transposes a matrix and then returns a single row from it.

Format
----------------
.. function:: y = getTrRow(a, row)

    :param a: data
    :type a: NxK matrix

    :param row: The row of the matrix to extract
    :type row: scalar

    :return y: extracted data.

    :type y: 1xK row vector

Remarks
-------

:func:`getRow` is designed to give an alternative access to rows in a matrix than indexing the matrix by brackets.


Examples
----------------

::

    rndseed 12984698;

    // Random data matrix
    a = rndn(5, 5);

    /*
    ** Transpose matrix and get data
    ** in the third row
    */
    y = getTrRow(a, 3);

After this code

::

    a =   -0.021549592       -1.5369774       0.25847435       0.24440036      -0.67770177
          0.040552431        -1.2555734       0.70911664       1.1284965       0.56128146
          0.63161066         -0.30454776      -0.54252340      0.098013056     -0.25289740
          1.6585887          1.0805022        0.62438630       -0.21962685     0.37892022
          -0.68182580        0.47291873       -0.29240734      1.9273971       -1.3318647

    y =   0.63161066
          -0.30454776
          -0.54252340
          0.098013056
          -0.25289740

.. seealso:: Functions :func:`getRow`
