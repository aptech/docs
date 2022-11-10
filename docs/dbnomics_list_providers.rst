
dbnomics_list_providers
==============================================

Purpose
----------------
Respond a list of providers.

Format
----------------
.. function:: x = dbnomics_list_providers([...])
    
    :param limit: Optional. Default = 1000. The numbers of items to return.
    :type limit: integer

    :return x: A list of providers
    :rtype x: Dataframe


Examples
----------------

::

    dbnomics_list_providers();

::

            code       indexed_at             name           region             slug     terms_of_use          website 
           ACOSS 2022-10-31T04:01 Agence centrale            FRANCE            acoss https://www.acos https://www.acos 
            AFDB 2022-04-04T15:05 African Developm           Africa             afdb https://www.afdb https://www.afdb 
             AIH 2022-10-31T04:43 Africa Informati           AFRICA              aih https://www.afdb https://www.afdb 
           AMECO 2022-10-31T01:27 Annual macro-eco               EU            ameco https://ec.europ https://ec.europ 
           Apple 2022-04-14T06:05            Apple            World            apple https://covid19. https://covid19. 


Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: :func:`dbnomics_provider`

