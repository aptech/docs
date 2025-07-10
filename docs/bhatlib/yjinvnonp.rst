yjinvnonp
==============================================
Purpose
----------------
Computes the inverse of the nonparametric Yeo-Johnson transformation.

Format
----------------
.. function:: y_inv = yjinvnonp(mu, wdiag, lamnonp, x)

:param mu: Location parameter vector.
:type mu: vector

:param wdiag: Diagonal weights.
:type wdiag: vector

:param lamnonp: Lambda parameter (nonparametric).
:type lamnonp: scalar or vector

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