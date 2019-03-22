
fftmi
==============================================

Purpose
----------------

Computes a multi-dimensional inverse FFT.

Format
----------------
.. function:: fftmi(x, dim)

    :param x: data.
    :type x: Mx1 vector

    :param dim: size of each dimension.
    :type dim: Kx1 vector

    :returns: y (*Lx1 vector*), inverse FFT of x.



Remarks
-------

The multi-dimensional data are laid out in a recursive or heirarchical
fashion in the vector x. That is to say, the elements of any given
dimension are stored in sequence left to right within the vector, with
each element containing a sequence of elements of the next smaller
dimension. In abstract terms, a 4-dimensional 2x2x2x2 hypercubic x would
consist of two cubes in sequence, each cube containing two matrices in
sequence, each matrix containing two rows in sequence, and each row
containing two columns in sequence. Visually, x would look something
like this:

::

                   
   Xhyper = Xcube1|Xcube2
                Xcube1 = Xmat1|Xmat2
                              Xmat1 = Xrow1|Xrow2
               

Or, in an extended GAUSS notation, x would be:

::

   Xhyper = x[1,.,.,.] | x[2,.,.,.];
   Xcube1 = x[1,1,.,.] | x[1,2,.,.];
   Xmat1 = x[1,1,1,.] | x[1,1,2,.];
   Xrow1 = x[1,1,1,1] | x[1,1,1,2];

To be explicit, x would be laid out like this:

::

   x[1,1,1,1] x[1,1,1,2] x[1,1,2,1] x[1,1,2,2]
   x[1,2,1,1] x[1,2,1,2] x[1,2,2,1] x[1,2,2,2]
   x[2,1,1,1] x[2,1,1,2] x[2,1,2,1] x[2,1,2,2]
   x[2,2,1,1] x[2,2,1,2] x[2,2,2,1] x[2,2,2,2]

If you look at the last diagram for the layout of x, you'll notice that
each line actually constitutes the elements of an ordinary matrix in
normal row-major order. This is easy to achieve with vecr. Further, each
pair of lines or ''matrices'' constitutes one of the desired cubes,
again with all the elements in the correct order. And finally, the two
cubes combine to form the hypercube. So, the process of construction is
simply a sequence of concatenations of column vectors, with a vecr step
if necessary to get started.

Here's an example, this time working with a 2x3x2x3 hypercube.

::

   let dim = 2 3 2 3;
   let x1[2,3] = 1 2 3 4 5 6;
   let x2[2,3] = 6 5 4 3 2 1;
   let x3[2,3] = 1 2 3 5 7 11;
   xc1 = vecr(x1)|vecr(x2)|vecr(x3); /* cube 1 */
   let x1 = 1 1 2 3 5 8;
   let x2 = 1 2 6 24 120 720;
   let x3 = 13 17 19 23 29 31;
   xc2 = x1|x2|x3;                    /* cube 2 */
    
   xh = xc1|xc2;                      /* hypercube */
   xhffti = fftmi(xh,dim);

We left out the vecr step for the 2nd cube. It's not really necessary
when you're constructing the matrices with let statements.

dim contains the dimensions of x, beginning with the highest dimension.
The last element of dim is the number of columns, the next to the last
element of dim is the number of rows, and so on. Thus

::

   dim = { 2, 3, 3 };

indicates that the data in x is a 2x3x3 three-dimensional array, i.e.,
two 3x3 matrices of data. Suppose that x1 is the first 3x3 matrix and x2
the second 3x3 matrix, then

::

   x = vecr(x1)|vecr(x2)

The size of dim tells you how many dimensions x has.

The arrays have to be padded in each dimension to the nearest power of
two. Thus the output array can be larger than the input array. In the
2x3x2x3 hypercube example, x would be padded from 2x3x2x3 out to
2x4x2x4. The input vector would contain 36 elements, while the output
vector would contain 64 elements.



Source
------

fftm.src

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftn`
