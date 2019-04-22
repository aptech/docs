
lngammacplx
==============================================

Purpose
----------------

Returns the natural log of the Gamma function.

Format
----------------
.. function:: lngammacplx(z)

    :param z: data. may be complex.
    :type z: NxK matrix

    :returns: f (*NxK matrix*)

Remarks
-------

Note that ``lngammacplx(z)`` may yield a result with a different imaginary
part than ``ln(gammacplx(z))``. This is because ``lngammacplx(z)`` returns the
value of the logarithm of ``gamma(z)`` on the corresponding branch of the
complex plane, while a call to ``ln(z)`` always returns a function value
with an imaginary part within :math:`[-π,π]`. Hence the imaginary part of the
result can differ by a multiple of :math:`2*π`. However, ``exp(lngammacplx(z)) = gammacplx(z)``. 
This routine uses a Lanczos series approximation for the complex ``ln(gamma)`` function.

References
----------

#. C. Lanczos, SIAM JNA 1, 1964. pp. 86-96.

#. Y. Luke, ''The Special ... approximations,'' 1969 pp. 29-31.

#. Y. Luke, ''Algorithms ... functions,'' 1977.

#. J. Spouge, SIAM JNA 31, 1994. pp. 931.

#. W. Press, ''Numerical Recipes.''

#. S. Chang, ''Computation of special functions,'' 1996.

#. P. Godfrey, ''A note on the computation of the convergent Lanczos
   complex Gamma approximation.''

#. Original code by Paul Godfrey

