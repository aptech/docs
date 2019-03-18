
intgrat2
==============================================

Purpose
----------------

Integrates the following double integral, using user-defined functions f, g1 and g2 and scalars a and b:
                
                    
                        
                            
                                
                                    
                                        ∫
                                    
                                    
                                        
                                            
                                                a
                                            
                                        
                                    
                                    
                                        
                                            
                                                b
                                            
                                        
                                    
                                
                            
                            
                            
                            
                                
                                    
                                        ∫
                                    
                                    
                                        
                                            
                                                g
                                            
                                            
                                                
                                                    
                                                        2
                                                    
                                                    
                                                        (
                                                        x
                                                        )
                                                    
                                                
                                            
                                        
                                    
                                    
                                        
                                            
                                                
                                                    
                                                        g
                                                    
                                                    
                                                        
                                                            
                                                                1
                                                            
                                                            
                                                                (
                                                                x
                                                                )
                                                            
                                                        
                                                    
                                                
                                            
                                        
                                    
                                
                                
                                
                                    
                                        f
                                        (
                                        x,
                                        y
                                        )
                                        d
                                        y
                                        d
                                        x
                                    
                                
                            
                        
                    
                
            

Format
----------------
.. function:: intgrat2(&f, xl, gl)

    :param &f: pointer to the procedure containing the function to be integrated.
    :type &f: scalar

    :param xl: the limits of x. These must be scalar limits.
    :type xl: 2x1 or 2xN matrix

    :param gl: the limits of y.
        For  xl and   gl, the first row is the upper
        limit and the second row is the lower limit. N integrations are computed.
    :type gl: 2x1 or 2xN matrix of function pointers

    :returns: y (*TODO*), Nx1 vector of the estimated integral(s) of
        f(x, y),
        evaluated between the limits given by  xl and  gl.

Examples
----------------

::

    proc (1) = f(x,y);
       retp(cos(x) + 1).*(sin(y) + 1));
    endp;
     
    proc (1) = g1(x);
       retp(sqrt(1-x^2));
    endp;
     
    proc (1) = g2(x);
       retp(0);
    endp;
     
    xl = 1|-1;
    g0 = &g1|&g2;
    _intord = 40;
    y = intgrat2(&f,xl,g0);

This will integrate the function

::

    f(x,y) = (cos(x)+1)(sin(y)+1)

.*
*
definition of f(x,y). This allows f to return
a vector or matrix of function values.

Source
++++++

intgrat.src

Globals
+++++++

\_intord, \_intq12, \_intq16, \_intq2, \_intq20, \_intq24, \_intq3,
\_intq32, \_intq4, \_intq40, \_intq6, \_intq8

.. seealso:: Functions :func:`intgrat3`, :func:`intquad1`, :func:`intquad2`, :func:`intquad3`, :func:`intsimp`

intergrate 2-dimensional user define adaptive quadrature
