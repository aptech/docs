
intrleavsa
==============================================

Purpose
----------------

Interleaves the rows of two string arrays that have been sorted on a common column.

Format
----------------
.. function:: y = intrleavsa(sa1, sa2, ikey)

    :param sa1: String array 1
    :type sa1: NxK

    :param sa2: String array 2
    :type sa2: MxK

    :param ikey: index of the key column the string arrays are sorted on.
    :type ikey: scalar integer

    :returns: **y** (*LxK string array*) - combined string array.


Examples
----------------

::

  // Create first string array
  string db_one = { "adams" "rebecca" "CO",
            "zowleski" "larry" "WI",
            "jones" "zoe" "MO",
            "harrison" "mike" "CA"};

  // Sort first string array
  db_one = sortc(db_one, 1);

  print "First sorted string array " db_one;
  print ;

  // Create second string array
  string db_two = { "yamhill" "jennifer" "WA",
             "ryan" "amy" "AZ",
             "davis" "sarah" "MI",
             "smith" "donald" "FL" };


  // Sort second string array on surnames
  db_two = sortc(db_two, 1);

  print "Second sorted string array " db_two;
  print ;

  // Interleave both string arrays

  // Define string arrays to interleave
  sa_1 = db_one;
  sa_2 = db_two;

  // Define column to merge on
  ikey = 1;

  // Combine string arrays
  db_total = intrleavsa(sa_1, sa_2, ikey);

  print "Combined string arrays" db_total;

The output from this reads:

::

    First sorted string array
               adams          rebecca               CO
            harrison             mike               CA
               jones              zoe               MO
            zowleski            larry               WI

    Second sorted string array
               davis            sarah               MI
                ryan         jennifer               AZ
               smith           donald               FL
             yamhill              amy               WA

    Combined string arrays
               adams          rebecca               CO
               davis            sarah               MI
            harrison             mike               CA
               jones              zoe               MO
                ryan         jennifer               AZ
               smith           donald               FL
             yamhill              amy               WA
            zowleski            larry               WI

Remarks
-------

The two string arrays MUST have exactly the same number of columns AND
have been already sorted on a *key* column.

This procedure will combine them into one large string array, sorted by the *key* column.

Source
------

sortd.src

.. seealso:: Functions :func:`intrleav`
