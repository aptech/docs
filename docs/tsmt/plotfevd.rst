plotFEVD
========

Purpose
-------

The :func:`plotFEVD` function is designed to plot the Factor Error Variance Decompositions from a structural Vector Autoregression (VAR) model. 

Format
------
.. function:: plotFEVD(sOut)

    :param sOut: An instance of the :class:`svarOut` structure containing the results from the :proc:`svarFit` estimation procedure.
    :type sOut: struct

Example
-------

:: 

    // Load library
    new;
    library tsmt;

    /*
    ** Data import
    */
    lutkepohl2 = loadd(getGAUSShome("pkgs/tsmt/examples/lutkepohl2.dta"));

    // Filter data 
    lutkepohl2 = selif(lutkepohl2, lutkepohl2[., "qtr"] .<= "1978-12-30");

    // Set Y
    y = packr(lutkepohl2[., "qtr" "dln_inv" "dln_inc" "dln_consump"]);
    
    // Set up output structures
    struct svarOut sout;

    // Compute structural VAR model
    sout = svarFit(Y);

    // Plot the IRFs
    plotFEVD(sOut);

Remarks
-------
The :func:`plotFEVD` function expects a filled instance of the :class:`svarOut` structure. It must be called after running :func:`svarFit`.

.. seealso:: Functions :func:`svarFit`, :func:`svarControlCreate`, :func:`plotIRF`

