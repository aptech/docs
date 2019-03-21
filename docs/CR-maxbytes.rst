
maxbytes
==============================================

Purpose
----------------

Returns maximum memory to be used.

Format
----------------
.. function:: maxbytes

    :param __maxbytes: maximum memory to be used.
    :type __maxbytes: scalar

    :returns: y (*scalar*), maximum memory to be used.

Remarks
-------

maxbytes returns the value in the global scalar \__maxbytes, which can
be reset in the calling program.

maxbytes is called by **Run-Time Library** functions and applications
when determining how many rows can be read from a data set in one call
to readr.

maxbytes replaced the obsolete command coreleft. If coreleft returns a
meaningful number for your operating system and if you wish to reference
it, set \__maxbytes = 0 and then call maxbytes.


Examples
----------------

::

    y = maxbytes;
    print y;

::

    100000000.000

Source
------

system.src

