Inference
======================

**CMLMT** includes four broad classes of methods for analyzing the distributions of the estimated parameters:

* Tests of hypotheses for models with constrained parameters.
* Taylor Series covariance matrix of the parameters. This includes two types: the inverted Hessian and the heteroskedastic-consistent covariance matrix computed from both the Hessian and the cross-product of the first derivatives.
* Confidence limits computed by inversion of the Wald and likelihood ratio statistics that take
into account constraints
* Bootstrap
* Likelihood profile and profile t traces

**CMLMT** computes a Taylor-series covariance matrix of the parameters that includes the sampling distributions of the Lagrangean coefficients. However, when the model includes inequality constraints, confidence limits computed from the usual t-statistics, i.e., by simply dividing the parameter estimates by their standard errors, are incorrect because they do not account for boundaries placed on the distributions of the parameters by the inequality constraints.

Inference for Model with Constraints on Parameters
----------------------------------------------------

The likelihood ratio statistic becomes a mixture of chi-squared distributions in the region of constraint boundaries (Gourieroux et al., 1982). If there are no parameters with limits near constraint boundaries, bootstrapping will suffice. Taylor-series methods assume that
it is reasonable to truncate the Taylor-series approximation to the distribution of the parameters at the second order. If this is not reasonable, bootstrapping is an alternative not requiring this assumption. It is important to note that if the limit of the parameter of
interest or any other parameters with which it is correlated more than .6 are near constraint boundaries, then bootstrapping will not produce correct inference (Andrews, 1999).
The hypotheses :math:`H(\theta) vs. H(\theta) \geq 0` can be tested using the :func:`chiBarSq` procedure. 

The procedure :func:`cmlmtBoot`` generates the mean vector and covariance matrix of the bootstrapped parameters. The likelihood profile and profile t traces explicated by Bates and Watts (1988) provide diagnostic material for evaluating parameter distributions. :func:`cmlmtProfile` generates trace plots which are used for this evaluation.

Covariance Matrix of the Parameters
--------------------------------------

An argument based on a Taylor-series approximation to the likelihood function (e.g., Amemiya, 1985, page 111) shows that

.. math:: \hat{\theta} \rightarrow N\left(\theta, A^{-1}BA^{-1}\right)

where

.. math:: A = E \big[ \frac{\partial^2 L}{\partial \theta \partial \theta' \big}]
.. math:: B = E \big[ \left(\frac{\partial L}{\partial \theta}\big)'\left(\frac{\partial L}{\partial \theta}\big\right)]

Estimates of :math:`A` and :math:`B` are

.. math:: \hat{A} = \frac{1}{N} \sum_i^N \frac{\partial^2 L}{\partial \theta \partial \theta' \big}
.. math:: \hat{B} = \big[ \left(\frac{\partial L}{\partial \theta}\right)'\left(\frac{\partial L}{\partial \theta}\big\right)]

Without loss of generality we may consider two types of constraints, the nonlinear equality and the nonlinear inequality constraints (the linear constraints are included in nonlinear, and the bounds are regarded as a type of linear inequality). Furthermore, the inequality constraints may be treated as equality constraints with the introduction of "slack" parameters into the model:

.. math:: H\left(\theta \right) \geq 0

is changed to 

.. math:: H\left(\theta \right) \geq \zeta^2

Further distinguish *active* from *inactive* inequality constraints. Active inequality constraints have nonzero Lagrangeans, :math:\lambda_j , and zero slack parameters, :math:`\zeta_j`, while the reverse is true for inactive inequality constraints. Keeping this in mind, define the diagonal matrix, :math:`Z`, containing the slack parameters, :math:`\zeta_j`, for the inactive constraints, and another diagonal matrix, :math:`\Gamma`, containing the Lagrangean coefficients. Also define, :math:`H_{\oplus} \left(\theta\right) representing the active constraints, and :math:`H_{\ominus} \left(\theta\right) the inactive.

The likelihood function augmented by constraints is then

.. math:: L_A = L + \lambda_1 g\left(\theta \right)_1 + \ldots + \lambda_1 g\left( \theta \right)^1 + \lambda_1 h_{\oplus 1}\left(\theta \right) + \ldots + \lambda_j h_{\oplus j}\left(\theta \right) + h_{\ominus 1}\left(\theta \right)_i - \zeta_1^2 + \ldots + h_{\ominus K}\left(\theta \right)_i - \zeta_K^2

and the Hessian of the augmented likelihood is

.. math::  \begin{gather} E \left[ \frac{\partial^2 L_A}{\partial \theta \partial \theta'} \right] =  \begin{bmatrix} 
                                                                                    \sum 0 0 \dot{G}' \dot{H_\oplus}' \dot{H_\ominus}'
                                                                                    0 2\Gamma 0 0 0 0 &
                                                                                    0 0 0 0 0 2Z &
                                                                                    \dot{G} 0 0 0 0 0 &
                                                                                    \dot{H_\oplus} 0 0 0 0 0 &
                                                                                    \dot{H_\ominus} 0 2Z 0 0 
                                                                                    \end{bmatrix} \end{gather}

where the dot represents the Jacobian with respect to :math:`\theta`, :math:`L = \sum_{i=1}^N log P\left(Y_i; \theta\right)`, and :math:`\sum = \frac{\partial^2 L_A}{\partial \theta \partial \theta'}`. The covariance matrix of the parameters, Lagrangeans, and slack parameters is the Moore-Penrose inverse of this matrix. Usually, however, we are interested only in the covariance matrix of the parameters, as well as the covariance matrices of the Lagrange coefficients associated with the active inequality constraints and the equality constraints.                                                                                

These matrices may be computed without requiring the storage and manipulation of the entire Hessian. Construct the partitioned array

