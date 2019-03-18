
gosub
==============================================

Purpose
----------------

Causes a branch to a subroutine. Note: This is an advanced function that gives extra flexibility for sophisticated users in some circumstances.
In most cases, it is prefereable to create a procedure (proc).

Format
----------------
.. function:: gosub label 
			       . 
			       . 
			       . 
			  label:     . 
			       . 
			       . 
			  return

Examples
----------------
In the program below the name mysub is a label. When the gosub
statement is executed, the program will jump to the label mysub and
continue executing from there. When the return statement is
executed, the program will resume executing at the statement following the gosub.

::

    x = rndn(3,3);
    z = 0;
    gosub mysub;
    print z;
    end;
     
    /* ------ Subroutines Follow ------ */
     
    mysub:
     z = inv(x);
    return;

Parameters can be passed to subroutines in the following way (line numbers are added for clarity):

::

    1. gosub mysub(x,y);
     2. pop j; /* b will be in j */
     3. pop k; /* a will be in k */
     4. t = j*k;
     5. print t;
     6. end;
     7.
     8. /* ---- Subroutines Follow ----- */
     9.
     10. mysub:
     11. pop b; /* y will be in b */
     12. pop a; /* x will be in a */
     13.
     14. a = inv(b)*b+a;
     15. b = a'b;
     16. return(a,b);

In the above example, when the gosub statement is
executed, the following sequence of events results (line numbers
are included for clarity):
1. 
x and y are pushed on the stack and the program branches to the label mysub in line 10.

11. 
the second argument that was pushed, y, is pop'ped into b.

12. 
the first argument that was pushed, x, is pop'ped into a.

14. 
inv(b)*b+a is assigned to a.

15. 
a'b is assigned to b.

16. 
a and b are pushed on the stack and the program branches to the statement following the gosub,
 which is line 2.

2. 
the second argument that was pushed, b, is pop'ped into j.

3. 
the first argument that was pushed, a, is pop'ped into k.

4. 
j*k is assigned to t.

5. 
t is printed.

6. 
the program is terminated with the end statement.
Matrices are pushed on a last-in/first-out stack in
the gosub() and return() statements. They must be
pop'ped off in the reverse order. No intervening
statements are allowed between the label and the pop
or the gosub and the pop. Only one matrix may be
pop'ped per pop statement.

.. seealso:: Functions :func:`goto`, :func:`proc`, :func:`pop`, :func:`return`
