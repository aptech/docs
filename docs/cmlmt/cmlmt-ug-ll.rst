The Log-likelihood Function
=============================

**CMLMT** is a set of procedures for estimating the parameters of models via the maximum likelihood method with general constraints on the parameters, along with an additional set of procedures for statistical inference.

**CMLMT** solves the general weighted maximum likelihood problem

.. math:: L = \sum^N_{i=1} log P(Y_i;\theta)^{\omega_i}

where :math:`N` is the number of observations, :math:`omega_i` is a weight, :math:`P(Y_i, \theta) is the probability of :math:`Y_i` given :math:`\theta`, a vector of parameters, subject to the linear constraints

.. math:: A(\Theta) = B
.. math:: C(\Theta) \geq D          

the nonlinear constraints
 
.. math:: G(\Theta) = 0
.. math:: H(\Theta) \geq 0     

and bounds, 
  
.. math:: \Theta_L \leq \Theta \leq \Theta_u
  
:math:`G(\Theta)` and :math:`H(\Theta)` are functions provided by the user and must be differentiable at least once with respect to the parameters.

The procedure :func:`cmlmt` finds values for the parameters in :math:`\theta` such that :math:`L` is maximized. In fact :func:`cmlmt` minimizes :math:`-L`. It is important to note, however, that the user must specify the log-probability to be maximized. **CMLMT** transforms the function into the form to be
minimized.

**CMLMT** has been designed to make the specification of the function and the handling of the data convenient. The user supplies a procedure that computes :math:`log P(Y_i; \theta)` i.e., the log-likelihood, given the parameters in :math:`\theta`, for either an individual observation or set of observations (i.e., it must return either the log-likelihood for an individual observation or a vector of log-likelihoods for a matrix of observations). **CMLMT** uses this procedure to construct the function to be minimized.
