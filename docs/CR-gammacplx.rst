
gammacplx
==============================================

Purpose
----------------

Computes the Gamma function for complex inputs.

Format
----------------
.. function:: f = gammacplx(x_cplx)

    :param x_cplx: the values used to compute the Gamma function. May include complex elements.
    :type x_cplx: NxK matrix;

    :return g_cplx: the values of the Gamma function evaluated at *x*. May be complex.

    :type g_cplx: NxK matrix

Examples
----------------

::

    // Real component
    xr = { 2.5 ,
           9.1 };

    // Imaginary component
    xi = { 3 ,
           1 };

    // Create complex matrix
    x_cplx = complex(xr, xi);

    // Compute gamma function
    gammacplx(x_cplx);

The results after the code:

::

    -0.21811897 +      0.072034763i
    -25993.298 +        39350.237i

Remarks
---------------

Accuracy is 15 significant digits along the real axis and 13 significant
digits elsewhere. This routine uses the *Lanczos* series approximation for
the complex Gamma function.

References
----------

#. C. Lanczos, SIAM JNA 1, 1964, pp. 86-96.

#. Y. Luke, ''The Special ... approximations,'' 1969, pp. 29-31.

#. Y. Luke, ''Algorithms ... functions,'' 1977.

#. J. Spouge, SIAM JNA 31, 1994, pp. 931-944.

#. W. Press, ''Numerical Recipes.''

#. S. Chang, ''Computation of special functions,'' 1996.

#. W. J. Cody ''An Overview of Software Development for Special
   Functions,'' 1975.

#. P. Godfrey ''A note on the computation of the convergent Lanczos
   complex Gamma approximation.''

#. Original code by Paul Godfrey
