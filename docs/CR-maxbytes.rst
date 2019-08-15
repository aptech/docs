
maxbytes
==============================================

Purpose
----------------

Returns maximum memory to be used.

Format
----------------
.. function:: y = maxbytes()

    :return y: maximum memory to be used.

    :rtype y: scalar

Global Input
------------

:__maxbytes: (*scalar*) maximum memory to be used.

Remarks
-------

:func:`maxbytes` returns the value in the global scalar *__maxbytes*, which can
be reset in the calling program.

:func:`maxbytes` is called by `Run-Time Library` functions and applications
when determining how many rows can be read from a data set in one call
to :func:`readr`.

:func:`maxbytes` replaced the obsolete command :func:`coreleft`. If :func:`coreleft` returns a
meaningful number for your operating system and if you wish to reference
it, set *__maxbytes* = 0 and then call :func:`maxbytes`.


Examples
----------------

::

    y = maxbytes;
    print y;

        100000000.000

Source
------

system.src

