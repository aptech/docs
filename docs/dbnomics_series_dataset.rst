
dbnomics_series_dataset
==============================================

Purpose
----------------
Respond a list of series belonging to the same dataset.

Format
----------------
.. function:: x = dbnomics_series_dataset(provider_code, dataset_code, series_code[, ...])

    :param provider_code: The code of a provider.
    :type provider_code: string

    :param dataset_code: The code of a dataset.

    :type dataset_code: string

    :param series_code: A series code mask is an alternative way to express a dimension filter. Can't be used with `dimensions` parameter.

        Series codes masks can designate many series by:

        - removing a constraint on a dimension, for example `M..PCPIEC_WT`;
        - enumerating many values for a dimension, separated by a '+', for example `M.FR+DE.PCPIEC_WT`;

          - if values contains '+', they can be protected with double quotes. Example: 'A+"FR+BE"' will enumerate series for 'A' and 'FR+BE' dimensions.

        - combining these possibilities many times in the same code mask.

        If the rightmost dimension value code is removed, then the final '.' can be removed too: `A.FR.` = `A.FR`.

    :type series_code: string

    :param dimensions: Optional. JSON object describing the dimensions filtering the search. Can't be used with *series_code* parameter.
    :type dimensions: string

    :param q: Optional. Full-text search query
    :type q: string

    :param metadata: Optional. Default = True. Return providers and datasets metadata in response.
    :type metadata: bool

    :param limit: Optional. Default = 1000. The numbers of items to return.
    :type limit: integer

    :return x: A list of series
    :rtype x: Dataframe

Examples
----------------

::

    head(dbnomics_series_dataset("{"FREQ": ["A"]}", "GDP France"));

    

Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: 

