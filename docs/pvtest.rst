
pvTest
==============================================

Purpose
----------------

Tests an instance of structure of type :class:`PV` to determine
if it is a proper structure of type :class:`PV`.

Format
----------------
.. function:: i = pvTest(p1)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :return i: if 0, *p1* is a proper structure of
        type :class:`PV`, else if 1, an improper or uninitialized structure
        of type :class:`PV`.

    :rtype i: scalar

Examples
--------

::

    // Create a valid PV structure
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1, 1|2|3, "beta");

    // Test if p1 is a valid PV structure
    i = pvTest(p1);
    print (i == 0);  // 1 (true) means valid

Source
------

pv.src
