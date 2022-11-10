
dbnomics_provider
==============================================

Purpose
----------------
Respond a provider with its category tree.

Format
----------------
.. function:: x = dbnomics_provider(provider_code[, ...])

    :param provider_code: Code of the provider
    :type provider_code: string

    :return x: A provider with its category tree
    :rtype x: Dataframe

Examples
----------------

::

    dbnomics_provider("AMECO");

::

                children             code         doc_href             name 
        [{"children":[{"                1 https://ec.europ Population and E 
        [{"children":[{"                2 https://ec.europ      Consumption 
        [{"children":[{"                3 https://ec.europ Capital Formatio 
        [{"children":[{"                4 https://ec.europ Domestic and Fin 
        [{"children":[{"                5 https://ec.europ  National Income 


Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: :func:`dbnomics_list_providers`

