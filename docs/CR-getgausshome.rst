
getGAUSSHome
==============================================

Purpose
----------------

Returns the full path to the GAUSS home directory.

Format
----------------
.. function:: getGAUSSHome()

    :returns: g_home (*string*), full path to GAUSS home directory.

Remarks
-------

getGAUSSHome can be used to load and save files in directories that are
relative to the GAUSS installation directory without knowing its exact
location ahead of time. This can help to make programs that will run on
multiple computers, using different paths without any changes to the
code.


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
