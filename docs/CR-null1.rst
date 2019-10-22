
null1
==============================================

Purpose
----------------

Computes an orthonormal basis for the (right) null space of a matrix and writes it to a GAUSS dataset.

Format
----------------
.. function:: nu = null1(x, dataset)

    :param x: data
    :type x: NxM matrix

    :param dataset: the name of a dataset :func:`null1` will write.
    :type dataset: string

    :return nu: the nullity of *x*.
    :rtype nu: scalar

Examples
----------------

::

        let x[2, 4] = 2 1 3 -1
                     3 5 1  2;

        b = null1(x, "mynull");
        z = x*b;
        i = b'b;

After the code above:

::

            -0.804  0.142
        b =  0.331 -0.473  z = 0  0  i = 1  0
             0.473  0.331      0  0      0  1
             0.142  0.804

In addition, the dataset ``"mynull.dat"`` is saved in the current working directory and can be loaded using :func:`loadd`.

::

  null_ds = loadd("mynull.dat");
  print null_ds;

Results in

::

  -0.80408330       0.33112495       0.47295835       0.14183340
   0.14183340      -0.47295835       0.33112495       0.80408330

Remarks
-------

:func:`null1` computes an MxK matrix *b*, where *K* is the nullity of *x*, such that:

::

   // NxK matrix of 0's
   x * b = 0

and

::

   // MxM identity matrix
   b'b = I

The transpose of *b* is written to the dataset named by *dataset*, unless
the nullity of *x* is zero. If *nu* is zero, the dataset is not written.

Globals
-------

\_qrdc, \_qrsl

Source
------

null.src
