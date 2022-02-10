
threadBegin
==============================================

Purpose
----------------

Marks the beginning of a multi-line block of code to be executed as a thread.

.. _threadBegin:
.. index:: threadBegin

Format
----------------

::

    threadBegin;

Examples
----------------

::

    threadBegin;
       m = n*p;
       n = calcA(m);
    threadEnd;

Notice that the writer-must-isolate rule (see `Multi-Threaded Programming in GAUSS <MT-MultiThreadedProgramming.html>`_)
does not apply within the bounds of the `threadBegin`/`threadEnd` pair, as there is no risk of
simultaneous access to a symbol. The rule only applies between the threads in a given set (and their children).

See `threadJoin` for an example of a fully-defined thread set.

.. seealso:: Functions `threadEnd`, `threadJoin`, `threadStat`

