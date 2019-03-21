
vcm, vcx
==============================================

Purpose
----------------
Computes an unbiased estimate a variance-covariance matrix.
		NOTE: vcm and vcx have been replaced with functions varCovXS and varCovMS whose descriptions use more standard statistical nomenclature. vcx and vcm will continue to be available for backwards compatibility.

Format
----------------
.. function:: vcm(m) 
			  vcx(x)

    :param m:  A constant term MUST have
        been the first variable when the moment matrix was computed.
    :type m: KxK moment (x'x) matrix

    :param x: 
    :type x: NxK matrix of data

    :returns: vc (*TODO*), KxK variance-covariance matrix.

