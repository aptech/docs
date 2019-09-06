
loadstruct
==============================================

Purpose
----------------

Loads a structure into memory from a file on the disk.

Format
----------------
.. function:: { instance, retcode } = loadstruct(file_name, structure_type)

    :param file_name: name of file containing structure.
    :type file_name: string

    :param structure_type: structure type.
    :type structure_type: string

    :return instance: instance of the struct.

    :rtype instance: struct

    :return retcode: 0 if successful, otherwise 1.

    :rtype retcode: scalar

Remarks
-------

*instance* can be an array of structures.


Examples
----------------

Single Instance of Structure
++++++++++++++++++++++++++++

::

    #include ds.sdf
    struct DS p3;

    { p3, retc } = loadstruct("p2", "ds");

Array of structures
++++++++++++++++++++

First, define a new structure *country*, declare and instance *countries*, reshape it to an array, and save the structure to disk.

::

  struct country
  {
    string name;
    scalar population;
  };

  struct country countries;
  countries = reshape(countries, 2, 1);

  countries[1].name = "Canada";
  countries[1].population = 37;
  countries[2].name = "China";
  countries[2].population = 1386;

  retc = saveStruct(countries, "countries");


Now load the saved instance as a new instance *countries_new*

::

  struct country countries_new;
  countries_new = reshape(countries_new, 2, 1);

  { countries_new, retcode } = loadStruct("countries", "country");
