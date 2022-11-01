
dbnomics_datasets_provider_data
==============================================

Purpose
----------------
Respond one or several datasets of a provider.

Format
----------------
.. function:: x = dbnomics_datasets_provider_data(provider_code, dataset_code[, ...])

    :param provider_code: Code of the provider
    :type provider_code: string

    :param dataset_code: Code of the dataset
    :type dataset_code: string

    :param limit: Optional. Default = 50. The numbers of items to return.
    :type limit: integer

    :return x: A list of dataset
    :rtype x: Dataframe

Examples
----------------

::

    head(dbnomics_datasets_provider_data("AMECO", "ZUTN"));

        code dimensions_codes dimensions_label dimensions_value         dir_hash       indexed_at             name        nb_series    provider_code    provider_name 
        ZUTN ["freq","unit"," {"freq":"Frequen {"freq":{"a":"An 11dab34a51b507c5 2022-05-18T07:54 Unemployment rat               49            AMECO Annual macro-eco 

Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: 

