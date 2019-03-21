
ThreadJoin
==============================================

Purpose
----------------

Completes the definition of a set of threads to be executed simultaneously.

Format
----------------
.. function:: ThreadJoin

Remarks
-------

Each thread in the set must adhere to the **writer-must-isolate** rule
(see **Multi-Threaded Programming in GAUSS**, Chapter 1). Because the
threads in a set execute simultaneously, there is no way of knowing in
one thread the current "state" of a symbol in another, and thus no way
of safely or meaningfully accessing it.


Examples
----------------

::

    ThreadBegin;        //Thread 1--isolates y,z
       y = x'x;
       z = y'y;
    ThreadEnd;
    ThreadBegin;        //Thread 2--isolates q,r
       q = r'r;
       r = q'q;
    ThreadEnd;
    ThreadStat n = m'm; //Thread 3--isolates n
    ThreadStat p = o'o; //Thread 4--isolates p
    ThreadJoin;         //Joins threads 1-4
    b = z + r + n'p;     //y,z,q,r,n,p available again,
                          // can be read and written

Note how threads 1-4 isolate the various symbols they assign to--no other
thread references the written symbols at all. Once the threads are joined,
however, the symbols are again available for use, and can be both read and
assigned to.

.. seealso:: Functions :func:`ThreadBegin`, :func:`ThreadEnd`, :func:`ThreadStat`
