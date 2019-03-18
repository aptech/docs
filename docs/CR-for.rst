
for
==============================================

Purpose
----------------

Begins a for loop.

Format
----------------
.. function:: for i (start,  stop,  step) 
			                   . 
			       . 
			       . 
			  endfor

    :param i: the name of the counter variable.
    :type i: literal

    :param start: the initial value of the counter.
    :type start: scalar expression

    :param stop: the final value of the counter.
    :type stop: scalar expression

    :param step: the increment value.
    :type step: scalar expression

Examples
----------------

//A basic 'for' loop
for i (1, 4, 1);
   print i;
endfor;
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    1.000
    2.000
    3.000
    4.000

x = zeros(10,5); 
for i (1, rows(x), 1);
  for j (1, cols(x), 1);
	x[i,j] = i*j;
  endfor;
endfor;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

x = rndn(3,3);
y = rndn(3,3);

for i (1, rows(x), 1);
   for j (1, cols(x), 1);
      if x[i,j] >= y[i,j];
         continue;
      endif;
      temp = x[i,j];
      x[i,j] = y[i,j];
      y[i,j] = temp;
   endfor;
endfor;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

li = 0;
x = rndn(100,1);
y = rndn(100,1);

for i (1, rows(x), 1);
   if x[i] != y[i];
      li = i;
      break;
   endif;
endfor;

if li;
   print "Compare failed on row " li;
endif;
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

