yjinv
==============================================
Purpose
----------------
Computes the inverse of the Yeo-Johnson transformation.

Format
----------------
.. function:: y_inv = yjinv(mu, wdiag, lamnew, x)

:param mu: Location parameter vector.
:type mu: vector

:param wdiag: Diagonal weight vector.
:type wdiag: vector

:param lamnew: Lambda parameter (logit transformed).
:type lamnew: scalar or vector

:param x: Input data vector.
:type x: vector

:return y_inv: Inverse transformed vector.
:rtype y_inv: vector

Library
-------
bhatlib

Source
------
vecup.src