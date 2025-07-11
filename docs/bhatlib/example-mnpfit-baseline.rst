Basic Multinomial Probit (MNP) Example
=======================================

This **GAUSS** optimization example demonstrates the use of the BHATLIB library for multinomial probit (MNP) estimation. The example illustrates how to set up a simple MNP model and estimate the parameters using the :func:`mnpfit` procedure. A program file matching this is example is provided in the BHATLIB library examples directory, which can be found in the GAUSS installation directory.

This basic example estimates a standard MNP model with alternative-specific constants and three generic explanatory variables: in-vehicle travel time (IVTT), out-of-vehicle travel time (OVTT), and cost (COST).

We demonstrate the following steps:
1. Preparing the environment and loading the necessary libraries.
2. Specifying the data file and key variables.  
3. Specifying choice variables and restrictions.
4. Specifying independent variables.
5. Running the MNP estimation using the :func:`mnpfit` procedure.

Data notes
-----------
This example uses the "TRAVELMODE.csv" dataset, which is included in the BHATLIB library. It comprises travel mode choice information for 1125 workers along with several variables that can be used as explanatory variables in a mode choice model. It provides a nice template for the data structure expected in the BHATLIB library. 
More details about setting up data for use with the BHATLIB library can be found in the `Data Preparation Guidelines. <https://docs.aptech.com/gauss/bhatlib/bhatlib-data-guidelines.html>`_


Step One: Preparing the environment and loading the libraries
----------------------------------------------------------------
The first step is to prepare the environment and load the necessary libraries. This includes loading the BHATLIB and maxlik libraries. In addition, we will clear the workspace to ensure a clean start.

:: 

    /*
    ** Step One: Preparing the environment
    ** and loading the libraries
    */
    // Clear environment and command window
    new;
    cls;

    // Load necessary libraries
    library bhatlib, maxlik;

Note that the `new` command clears all objects from the workspace. If you have data or results you want to keep, you should save them before running this command. The `cls` command clears the command window.

Step Two: Specifying data file
-------------------------------------------------
The next step is to specify the data file and the key variables that will be used in the model. In this example, we will use the "TRAVELMODE.csv" dataset, which is included in the BHATLIB library. Note that we do not have to load the data, we just need to specify the file name with the full path.

::

    // Data file 
    fname = __FILE_DIR$+"TRAVELMODE.csv"; 

Step Three: Specifying choice variables and restrictions
---------------------------------------------------------
In this step, we will specify the choice variables and any restrictions that apply to the model. The choice variables are the alternatives available to the decision-maker, and the restrictions define which alternatives are available in each observation.

These are specified in a string format, where each alternative should be represented by a column in the data. In our example the three choices, Drive Alone (DA), Shared Ride (SR), and Transit (TR) are contained in the `"Alt1_ch"`, `"Alt2_ch"`, and `"Alt3_ch"` columns. We input these as the `dvunordname` varible.

::

    // Specify available choices
    string dvunordname = { "Alt1_ch" "Alt2_ch" "Alt3_ch" };              


Additionally, the :func:`mnpfit` procedure allows for restrictions on the availability of choices to inviduals. These are specified using the `davunordname` variable. In this example, we assume that all alternatives are available to all individuals, so we do not need to specify any restrictions, and we set this equal to `"none"`.

:: 
    
    // Specify choice restrictions. If no choice restrictions
    // set equal to "none". Otherwise use "uno" for unrestricted
    // choices and specify column for identifying restricted choices
    string davunordname = "none";  
    
If there are choice restrictions, additional columns containing choice availability should be added to the dataset. These columns should be equal to 1 for individuals where the choice is available and 0 when the choice is not available.  

Step Four: Specifying independent variables
-------------------------------------------------
In this step, we will specify the independent variables that will be used in the model. These variables are used to explain the choice behavior of individuals. 

We specify our independent variables using the `ivunord` string array. This string array input should have one row for each available choice and one column for each independent variable. These rows represent the utility of each alternative, and the columns represent the independent variables that will be used in the model. 

If a variable is not used for a particular alternative, it should be set to `"sero"` in the corresponding row. To include a constant term in the model, we can use `"uno"` variable. 

In addition, the choice dependent variables should be included in the dataset with a separate column for each alternative. In this example, we will use the following independent variables: in-vehicle travel time (IVTT), out-of-vehicle travel time (OVTT), and cost (COST). As an example, the IVTT data is contained in three columns: `"IVTT_DA"`, `"IVTT_SR"`, and `"IVTT_TR"` for the three alternatives.

::
    
    /* Independent variable specification below; 
    ** Put alternative specific constants FIRST; 
    ** Have one row for each alternative and for each segment 
    ** The number of rows below will be #alts x nseg 
    */
    string ivunord = 
    {	"sero"	"sero"	"IVTT_DA"	  "OVTT_DA"	    "COST_DA"	,
        "uno"	"sero"	"IVTT_SR"	  "OVTT_SR"	    "COST_SR"	,
        "sero"	"uno"	"IVTT_TR"	  "OVTT_TR"	    "COST_TR"	};

Step Five: Running the MNP estimation
-------------------------------------------------
The final step is to run the MNP estimation using the :func:`mnpfit` procedure. This procedure will estimate the parameters of the model based on the specified data and independent variables.

::

    // Run the MNP estimation
    beta_hat = mnpfit(fname, dvunordname, davunordname, ivunord, 1);


Results
-----------
Convergence details
++++++++++++++++++++
The first portion of the results provide details about convergence and performance. 

::

    return code =    2
    maximum number of iterations exceeded

    Mean log-likelihood       -0.587654
    Number of cases     1125

These results indicate that the optimization failed to converge normally, with a return code of 2. It also informs us that the error is a result of the maximum number of iterations being exceeded. 

Additionally, the mean log-likelihood is reported as -0.587654, and the number of cases used in the estimation is 1125.

Parameter estimates
++++++++++++++++++++
The next section of the results reports the parameter estimates and the associated gradients.

::

    Covariance matrix of the parameters computed by the following method:
    Cross-product of first derivatives

    Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
    ------------------------------------------------------------------
    CON_SR          -0.9884        0.1002   -9.861   0.0000      0.0000
    CON_TR          -0.5345        0.2132   -2.508   0.0122      0.0000
    IVTT            -0.8870        0.1768   -5.018   0.0000      0.0000
    OVTT            -1.0292        0.2020   -5.095   0.0000      0.0000
    COST            -0.5986        0.0690   -8.675   0.0000      0.0000
    cor1             0.4734        0.1598    2.962   0.0031      0.0000
    scale1           1.9865        0.3214    6.181   0.0000      0.0000

In this example, the gradients are all 0 for the estimates, as is expected at or near an optimum. We see that the estimates for the alternative-specific constants (CON_SR and CON_TR) are negative, indicating that these alternatives are less preferred compared to the base alternative (Drive Alone). The IVTT, OVTT, and COST variables also have negative estimates, suggesting that higher values of these variables decrease the likelihood of choosing that alternative. 

