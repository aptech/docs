
vcms, vcxs
==============================================

Purpose
----------------
Computes the observed variance-covariance matrix. NOTE: vcms and vcxs have been replaced with functions varCovX and varCovM whose descriptions use more standard statistical nomenclature. vcxs and vcms will continue to be available for backwards compatibility.

Format
----------------
.. function:: vcms(m) 
			  vcxs(x)

    :param m:  A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (x'x) matrix

    :param x: 
    :type x: NxK matrix of data

    :returns: vc (*TODO*), KxK variance-covariance matrix.

