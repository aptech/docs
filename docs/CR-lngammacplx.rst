
lngammacplx
==============================================

Purpose
----------------

Returns the natural log of the Gamma function.

Format
----------------
.. function:: lngammacplx(z)

    :param z: 
    :type z: NxK matrix;  z may be complex

    :returns: f (*TODO*), NxK matrix.



Remarks
-------

Note that lngammacplx(z) may yield a result with a different imaginary
part than ln(gammacplx(z)). This is because lngammacplx(z) returns the
value of the logarithm of gamma(z) on the corresponding branch of the
complex plane, while a call to ln(z) always returns a function value
with an imaginary part within [-π,π]. Hence the imaginary part of the
result can differ by a multiple of 2*π. However, exp(lngammacplx(z)) =
gammacplx(z). This routine uses a Lanczos series approximation for the
complex ln(gamma) function.

