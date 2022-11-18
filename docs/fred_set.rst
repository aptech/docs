
fred_set
==============================================

Purpose
----------------
Set one (or more) parameters for a given FRED API call. This function can both create a parameter or update an existing 
parameter set if the last argument is provided.

Use of this function is optional as all arguments can be specified inline with any associated FRED API call.

Format
----------------
.. function:: x = fred_set(key, value[, keyN, valueN[, ...[, existing_map]]])

    :param key: The parameter name to set.
    :type key: string

    :param value: The parameter value to set. If this paramater is a vector, it is converted to an array before being sent to the FRED API.
    :type value: any

    :param existing_map: Optional. An existing map to update. If not specified, a new map is returned.
    :type value: Dataframe

    :return x: Parameter map.
    :rtype x: Dataframe


Examples
----------------

Example with a single parameter
+++++++++++++++++++++++++++++++

::

    args = fred_set("realtime_start", "1960-01-01");
    x = fred_load("GNPCA", args);

the first 5 rows of *x* will be:

::

            date            GNPCA 
      1929-01-01        181.80000 
      1929-01-01        203.60000 
      1929-01-01        314.70000 
      1929-01-01        315.70000 
      1929-01-01        709.60000 


Example with multiple parameters
++++++++++++++++++++++++++++++++

::

    args = fred_set("realtime_start", "1980-01-01");
    args = fred_set("realtime_end", "1989-12-31", args);
    x = fred_load("GNPCA", args);

the first 5 rows of *x* will be:

::

            date            GNPCA 
      1929-01-01        314.70000 
      1929-01-01        315.70000 
      1929-01-01        709.60000 
      1930-01-01        285.20000 
      1930-01-01        285.60000 


Example with multiple parameters simultaneously
+++++++++++++++++++++++++++++++++++++++++++++++

::

    args = fred_set("realtime_start", "1980-01-01", "realtime_end", "1989-12-31");
    x = fred_load("GNPCA", args);

the first 5 rows of *x* will be:

::

            date            GNPCA 
      1929-01-01        314.70000 
      1929-01-01        315.70000 
      1929-01-01        709.60000 
      1930-01-01        285.20000 
      1930-01-01        285.60000

.. seealso:: :func:`fred_load`, :func:`fred_search`
