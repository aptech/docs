plotIRF
========

Purpose
-------

The `plotIRF` function is designed to plot the Impulse Response Functions (IRFs) from a structural Vector Autoregression (VAR) model. It visualizes the dynamic response of one variable to shocks in another variable over time. The function supports both unrestricted and restricted IRF matrices and includes confidence intervals based on bootstrapped results.

Format
------
.. function:: plotIRF(sOut [, rirf])

    :param sOut: An instance of the :class:`svarOut` structure containing the results from the :func:`svarFit` estimation procedure.
    :type sOut: struct

    :param rirf: Optional, an indicator variable, set to 1 to specify that restricted irfs should be plotted.
    :type rirf: scalar


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
    plotIRF(sOut);

Remarks
-------
The :func:`plotIRF` function expects a filled instance of the :class:`svarOut` structure. It must be called after running :func:`svarFit`.

.. seealso:: Functions :func:`svarFit`, :func:`svarControlCreate`, :func:`plotFEVD`, :func:`plotHD` 

