
fftmi
==============================================

Purpose
----------------

Computes a multi-dimensional inverse FFT.

Format
----------------
.. function:: y = fftmi(x, dim)

    :param x: data.
    :type x: Mx1 vector

    :param dim: size of each dimension.
    :type dim: Kx1 vector

    :return y: inverse FFT of *x*.

    :rtype y: Lx1 vector

Remarks
-------

The multi-dimensional data are laid out in a recursive or hierarchical
fashion in the vector *x*. That is to say, the elements of any given
dimension are stored in sequence left to right within the vector, with
each element containing a sequence of elements of the next smaller
dimension. In abstract terms, a 4-dimensional 2x2x2x2 hypercubic *x* would
consist of two cubes in sequence, each cube containing two matrices in
sequence, each matrix containing two rows in sequence, and each row
containing two columns in sequence. Visually, *x* would look something
like this:

.. math::

      X\_hyper = X\_cube1|X\_cube2\\
      X\_cube1 = X\_mat1|X\_mat2\\
      X\_mat1 = X\_row1|X\_row2\\

Or, in an extended GAUSS notation, *x* would be:

::

   Xhyper = x[1,.,.,.] | x[2,.,.,.];
   Xcube1 = x[1,1,.,.] | x[1,2,.,.];
   Xmat1 = x[1,1,1,.] | x[1,1,2,.];
   Xrow1 = x[1,1,1,1] | x[1,1,1,2];

To be explicit, *x* would be laid out like this:

::

   x[1,1,1,1] x[1,1,1,2] x[1,1,2,1] x[1,1,2,2]
   x[1,2,1,1] x[1,2,1,2] x[1,2,2,1] x[1,2,2,2]
   x[2,1,1,1] x[2,1,1,2] x[2,1,2,1] x[2,1,2,2]
   x[2,2,1,1] x[2,2,1,2] x[2,2,2,1] x[2,2,2,2]

If you look at the last diagram for the layout of *x*, you'll notice that
each line actually constitutes the elements of an ordinary matrix in
normal row-major order. This is easy to achieve with :func:`vecr`. Further, each
pair of lines or matrices constitutes one of the desired cubes,
again with all the elements in the correct order. And finally, the two
cubes combine to form the hypercube. So, the process of construction is
simply a sequence of concatenations of column vectors, with a :func:`vecr` step
if necessary to get started.

Examples
----------------

Here's an example, this time working with a 2x3x2x3 hypercube. The variable *dim* contains the dimensions of *x*, beginning with the highest dimension.
The last element of dim is the number of columns, the next to the last
element of *dim* is the number of rows, and so on. Thus

::

   dim = { 2, 3, 3 };

indicates that the data in *x* represents is a 2x3x3 three-dimensional array, i.e.,
two 3x3 matrices of data.

Suppose that *x1* is the first 3x3 matrix and *x2*
the second 3x3 matrix, then:

::

   x = vecr(x1)|vecr(x2)

The size of *dim* tells you how many dimensions *x* has.

::

   // Set dimensions of array
   let dim = 2 3 2 3;

   /*
   ** Assign matrices to place in
   ** first cube
   */
   let x1_1[2, 3] = 1 2 3 4 5 6;
   let x2_1[2, 3] = 6 5 4 3 2 1;
   let x3_1[2, 3] = 1 2 3 5 7 11;

   /*
   ** Form cube one by using vecr
   ** to vectorize x1_1, x2_1, x3_1
   ** then vertically concatenating
   ** the results
   */
   xc1 = vecr(x1_1)|vecr(x2_1)|vecr(x3_1);

This results in three 2x3 matrices, ``x1_1``, ``x2_1``, and ``x3_1`` and an 18x1 vector ``xc1``:

::

  x1_1 = 1.0000   2.0000   3.0000   x2_1 = 6.0000   5.0000   4.0000   x3_1 = 1.0000   2.0000   3.0000
         4.0000   5.0000   6.0000          3.0000   2.0000   1.0000          5.0000   7.0000  11.0000

  xc1 = 1.0000
        2.0000
        3.0000
        4.0000
        5.0000
        6.0000
        6.0000
        5.0000
        4.0000
        3.0000
        2.0000
        1.0000
        1.0000
        2.0000
        3.0000
        5.0000
        7.0000
        11.0000

To assign the second cube we will leave out the :func:`vecr` step. Instead we will construct ``x1``, ``x2``, and ``x3`` as vectors to using `let`.

::

    /*
    ** Assign matrices to place in
    ** second cube
    */
    let x1_2 = 1 1 2 3 5 8;
    let x2_2 = 1 2 6 24 120 720;
    let x3_2 = 13 17 19 23 29 31;

    /*
    ** Form cube two
    ** by vertically concatenating
    ** the x1_2, x2_2, and x3_2
    ** vectors
    */
    xc2 = x1_2|x2_2|x3_2;

This results in three 6x1 vectors ``x1_2``, ``x2_2``, and ``x3_2`` and an 18x1 vector ``xc2``:
We will concatenate ``xc1`` and ``xc2`` and use :func:`fftm` to find the Fourier Fast Transform:

::

    // Hypercube
    xh = xc1|xc2;
    xhfft = fftm(xh, dim);

    let dimi = 2 4 2 4;
    xhffti = fftmi(xhfft, dimi);

The arrays have to be padded in each dimension to the nearest power of
two. Thus the output array can be larger than the input array.

In this example, ``xh`` is an 36x1 vector and ``xhfft`` is a 64x1 vector. This is because in the case of the
2x3x2x3 hypercube example, *x* is padded from 2x3x2x3 out to
2x4x2x4. Hence, the input vector contains 36 elements, while the output
vector would contain 64 elements. You may have noticed that we use a
*dim* with padded values at the end of the example to check our answer.

Source
------

fftm.src

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftn`
