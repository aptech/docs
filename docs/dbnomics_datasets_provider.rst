
dbnomics_datasets_provider
==============================================

Purpose
----------------
Respond one or several datasets of a provider.

Format
----------------
.. function:: x = dbnomics_datasets_provider(provider_code[, ...])

    :param provider_code: Code of the provider
    :type provider_code: string

    :param limit: Optional. Default = 50. The numbers of items to return.
    :type limit: integer

    :return x: A list of dataset
    :rtype x: Dataframe

Examples
----------------

::

    dbnomics_datasets_provider("AMECO");

::

        code dimensions_codes dimensions_label dimensions_value         dir_hash       indexed_at             name        nb_series    provider_code    provider_name 
        AAGT ["freq","unit"," {"freq":"Frequen {"freq":{"a":"An bc8933e82d44de92 2022-05-18T07:54 Average share of        50.000000            AMECO Annual macro-eco 
       ADGGI ["freq","unit"," {"freq":"Frequen {"freq":{"a":"An 374687ca6ff83aeb 2022-06-01T01:24 Snow ball effect        40.000000            AMECO Annual macro-eco 
       ADGGU ["freq","unit"," {"freq":"Frequen {"freq":{"a":"An a3d21f71ccd636a1 2022-06-01T01:24 Impact of the no        41.000000            AMECO Annual macro-eco 
       AKGDV ["freq","unit"," {"freq":"Frequen {"freq":{"a":"An 718114eb49ce6a3c 2022-05-18T07:54 Marginal efficie        50.000000            AMECO Annual macro-eco 
       AKNDV ["freq","unit"," {"freq":"Frequen {"freq":{"a":"An b9bf44b914244916 2022-05-18T07:54 Net capital stoc        45.000000            AMECO Annual macro-eco 


Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: :func:`dbnomics_datasets_provider_data`

