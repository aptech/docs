
dbnomics_set
==============================================

Purpose
----------------
Set one (or more) parameters for a given DBnomics API call. This function can both create a parameter or update an existing 
parameter set if the last argument is provided.

Use of this function is optional as all arguments can be specified inline with any associated DBnomics API call.

Format
----------------
.. function:: x = dbnomics_set(key, value[, keyN, valueN[, ...[, existing_map]]])

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

::

    args = dbnomics_set("limit", 2);
    x = dbnomics_search("GDP", args);

*x* will be equal

::

                code      description         dir_hash       indexed_at             name nb_matching_seri        nb_series    provider_code    provider_name 
    CHELEM-TRADE-IND CHELEM-TRADE-IND                . 2022-09-02T09:35 CHELEM - Interna        683775.00        797349.00            CEPII Centre d'études 
         gov_10a_exp                . 2022-10-30T23:36                .                .        369772.00        1299223.0            CEPII                . 


.. seealso:: :func:`dbnomics_series`



