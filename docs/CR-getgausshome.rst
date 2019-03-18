
getGAUSSHome
==============================================

Purpose
----------------

Returns the full path to the GAUSS home directory.

Format
----------------
.. function:: getGAUSSHome()

    :returns: g_home (*string*), full path to GAUSS home directory.

Examples
----------------

locate the GAUSS home directory
+++++++++++++++++++++++++++++++

If you installed GAUSS in the directory, C:\gauss:

::

    g_home = getGAUSSHome();
    print g_home;

::

    C:\gauss

loading a file from the GAUSS examples directory
++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Create full path to dataset
    f_name = getGAUSSHome() $+ "examples/fueleconomy.dat";
    
    //Load the dataset
    fuel_economy = loadd(f_name);

.. seealso:: Functions 
