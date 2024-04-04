bamMCMC
=======

Purpose
-------
Main procedure for conducting MCMC-Gibbs style sampling of models.

Format
------
.. function:: bamOut0 = bamMCMC(myData, MCCtl0)

   Conducts MCMC-Gibbs style sampling based on the provided data and control structures, returning an instance of the bayesOut structure.

    :param myData: An instance of the :class:`dgpControl` structure. For an instance of the :class:`dgpcontrol` structure named *myData*, the members are:
            .. include:: include/dgpcontrol.rst
    :type myData: struct

    :param MCCtl0: An instance of the :class:`bayesControl` structure. For an instance of the :class:`bayesControl` structure named *MCCtl0* the members are:
            .. include:: include/bayescontrol.rst
    :type MCCtl0: struct

    :return bamOut0: An instance of the :class:`bayesOut` structure. For an instance of the :class:`bayesOut` structure named *bamOut0*, the members are:
            .. include:: include/bayesout.rst
    :rtype: struct


Examples
---------

Linear model with AR error terms 
+++++++++++++++++++++++++++++++++
Step One: Data Generation
^^^^^^^^^^^^^^^^^^^^^^^^^
The first step when using :func:`bamMCMC` is to identify the data for the model. For this model, we will use the :func:`dataGen` procedure to generate our data. This data must then be placed in the :class:`dgpOut` structure.

::

    new;
    cls;
    library bet;

    // Data generation control structure
    struct dgpControl GC0;
    
    // Specify autoregressive model
    GC0.Model = "AUTO";
    
    // Turn on plotting of generated data 
    GC0.PlotData = 1;

    // Specify number of observations
    GC0.NumObs = 100;
    
    // Specify model parameters
    GC0.TrueBeta = -3.1|2|-1.0|3;
    GC0.TrueRho = 0.3|-0.5;
    
    // Error variance 
    GC0.TrueSigmaE = 2;

    // X Error Variance
    GC0.TrueSigmaX = 2;
    GC0.TrueTrendX = 0;
    GC0.TrueInterceptX = 0;

    // Call data generation function
    struct dgpOut myData;
    myData = DataGen(GC0);
    
Step Two: Initialize Parameters for MCMC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Next, we set up the specifications for the MCMC simulation. 

::

    // Declare instance of the bayesControl structure
    struct bayesControl MCCtl0;

    // Specify AR(2) model
    MCCtl0.model = "AUTO";
    MCCtl0.numLags = 2;

    // Number of saved iterations
    MCCtl0.SavedIter = 4000;

    // Save skipped iterations 
    MCCtl0.SaveSkip = 1;

    // Number of burn-in iterations 
    MCCtl0.BurnIter = 1000;

    // No intercept  
    MCCtl0.InterceptX = 0;

    // Turn of MLE for start values 
    MCCtl0.MLE = 0;

    // Control printing and graphs 
    MCCtl0.printGraph = 1;
    MCCtl0.printOut = 1;


Step Three: Perform MCMC 
^^^^^^^^^^^^^^^^^^^^^^^^^
The final step is to call :func:`bamMCMC` to perform MCMC simulation.

::

    // Step Three: MCMC
    struct bayesOut BAMSt0;
    bamOut0 = bamMCMC(myData, MCCtl0);
    
Linear model with loaded data  
+++++++++++++++++++++++++++++++++
In this example, the :func:`loadd` procedure is used to load the model data. 

Step One: Load data
^^^^^^^^^^^^^^^^^^^^^^^^^
::

    new;
    library bet;

    // Load data from gbs_auto.gdat file
    data = loadd(__FILE_DIR $+ "gbs_ato.gdat");

    // Call data generation function
    struct dgpOut myData;
    mydata.ydata = data[., "Y"];
    myData.xdata = ones(rows(data), 1)~data[., "X"];

Step Two: Initialize Parameters for MCMC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    // Declare instance of the bayesControl structure
    struct bayesControl MCCtl0;
    
    // Specify AR(2) model
    MCCtl0.model = "AUTO";
    MCCtl0.numLags = 1;
    
    // Number of saved iterations
    MCCtl0.SavedIter = 4000;

    // Save skipped iterations 
    MCCtl0.SaveSkip = 1;

    // Number of burn-in iterations 
    MCCtl0.BurnIter = 1000;

    // No intercept  
    MCCtl0.InterceptX = 0;

    // Turn of MLE for start values 
    MCCtl0.MLE = 0;

    // Control printing and graphs 
    MCCtl0.printGraph = 1;
    MCCtl0.printOut = 1;

Step Three: Perform MCMC 
^^^^^^^^^^^^^^^^^^^^^^^^^
::

    // Define storage structure
    struct bayesOut BAMSt0;
    BAMSt0 = bamMCMC(myData, MCCtl0); 

Remarks
--------
The :func:`bamMCMC` procedure is the main procedure for model estimation in **BET**. It will can be used to estimate a number of different models. The type of model to be estimated is specified in the :class:`bayesControl` structure.  

Estimation with the **BET** library using :func:`bamMCMC` requires three steps:

#. **Data loading or generation** 
    The **BET** library allows you to input data using standard GAUSS data loading tools, such as :func:`loadd`. However, it also provides a complete suite of data generation tools that allow users to specify true data parameters and build hypothetical data sets for analysis. Whether user defined or **GAUSS** generated, the :class:`dgpOut` structure is used to input data into the :func:`bamMCMC` procedure. 

#. **Initialize the MCMC**
    The next step is to setup the parameters of the MCMC simulation using the :class:`bayesControl` structure. This includes the:
    * Model
    * Number of saved iterations
    * Number of iterations to skip
    * Number of burn-in iterations
    * Total number of iterations
    * Inclusion of intercept
    * Plotting behavior

#. **Perform bayesian analysis**
    The final step is to call the :func:`bamMCMC` procedure using :class:`dgpOut` data structure along with the :class:`bayesControl` structure. In this step, **GAUSS** performs Markov Chain Monte Carlo numerical simulation, combined with assumed statistical structures and priors, to numerically compute parameter
    posterior distributions.

    In addition to producing graphs of all MCMC iterations for all parameters and posterior distributions for all parameters, this procedure has one return structure the :class:`bayesOut` structure. The :class:`bayesOut` structure includes:
    * Draws for all parameters at each iteration
    * Posterior Mean for all parameters
    * Posterior standard deviation for all parameters
    * Predicted values
    * Residuals
    * Correlation matrix between Y and Yhat
    * PDF values and corresponding PDF grid for all posterior distributions
    * Log-likelihood value (when applicable)