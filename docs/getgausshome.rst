
getGAUSSHome
==============================================

Purpose
----------------

Returns the full path to the GAUSS home directory.

Format
----------------
.. function:: g_home = getGAUSSHome()

    :param relative_path: Optional input containing extra path information, you would like to add to the end of the GAUSS Home path. 
    :type relative_path: string

    :return g_home: full path to GAUSS home directory.

    :rtype g_home: string

Examples
----------------

Locate the GAUSS home directory
+++++++++++++++++++++++++++++++

If you installed GAUSS in the directory, ``C:\gauss``:

::

    g_home = getGAUSSHome();
    print g_home;

::

    C:\gauss

Loading a file from the GAUSS examples directory
++++++++++++++++++++++++++++++++++++++++++++++++

GAUSS 23 and newer versions allow you to pass in the relative path to the file you wish to load as shown below.

::

    // Create full path to dataset
    f_name = getGAUSSHome("examples/fueleconomy.dat");

    // Load the dataset
    fuel_economy = loadd(f_name);

Previous versions did not accept the path as an input and required the use of the string combine operator ``$+`` to create the full path.

::

    // Create full path to dataset
    f_name = getGAUSSHome() $+ "examples/fueleconomy.dat";

    // Load the dataset
    fuel_economy = loadd(f_name);

Remarks
-------

:func:`getGAUSSHome` can be used to load and save files in directories that are
relative to the GAUSS installation directory without knowing its exact
location ahead of time. This can help to make programs that will run on
multiple computers, using different paths without any changes to the
code.


.. seealso:: Functions `__FILE_DIR`
