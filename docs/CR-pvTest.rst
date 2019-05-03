
pvTest
==============================================

Purpose
----------------

Tests an instance of structure of type :class:`PV` to determine 
if it is a proper structure of type :class:`PV`.

Format
----------------
.. function:: pvTest(p1)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :returns: i (*scalar*), if 0, *p1* is a proper structure of
        type :class:`PV`, else if 1, an improper or unitialized structure
        of type :class:`PV`.

Source
------

pv.src

