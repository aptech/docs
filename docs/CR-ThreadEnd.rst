
ThreadEnd
==============================================

Purpose
----------------

Marks the end of a multi-line block of code to be executed as a thread.

Format
----------------
.. function:: ThreadEnd

Examples
----------------

::

    ThreadBegin;
       m = n*p;
       n = calcA(m);
    ThreadEnd;

Notice that the writer-must-isolate rule (see  Multi-Threaded Programming in GAUSS, Chapter  1)
does not apply within the bounds of the
ThreadBegin/ThreadEnd pair, as there is no risk of
simultaneous access to a symbol. The rule only applies between the threads in a
given set (and their children).
See ThreadJoin for an example of a fully-defined thread set.

.. seealso:: Functions :func:`ThreadBegin`, :func:`ThreadJoin`, :func:`ThreadStat`
