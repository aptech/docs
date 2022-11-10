
dbnomics_set
==============================================

Purpose
----------------
Set one (or more) parameters for a given DBnomics API call. This function can both create a parameter or update an existing 
parameter set if the last argument is provided.

Use of this function is optional as all arguments can be specified inline with any associated DBnomics API call.

Format
----------------
.. function:: x = dbnomics_set(key1, value1[[[, keyN, valueN], ..., existing_map])

    :param key: The parameter name to set.
    :type key: string

    :param value: The parameter value to set. If this paramater is a vector, it is converted to an array before being sent to the DBnomics API.
    :type value: any

    :param existing_map: Optional. An existing map to update. If not specified, a new map is returned.
    :type value: Dataframe

    :return x: Parameter map.
    :rtype x: Dataframe


Examples
----------------

Setting parameters consecutively
++++++++++++++++++++++++++++++++

::

    args = dbnomics_set("metadata", 0);

    dbnomics_search("GDP", args)


Setting parameters simultaneously
+++++++++++++++++++++++++++++++++

::

    args = dbnomics_set("limit", 10, "offset", 0);

    dbnomics_search("GDP", args)


.. seealso:: :func:`dbnomics_series`



