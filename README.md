pyRiemannProblem
================

Python scripts for analytically solving simple Riemann Problems.

At present this contains simple scripts for solving nonlinear, scalar, convex Riemann Problems. These approaches are not suitable for numerical evolution codes, but only for comparison. Through using sympy the example scripts should be straightforwardly generalized to much more complicated equations.

Terminology:

A (one dimensional) conservation law is the hyperbolic equation
$ \partial_t q + \partial_x f(q) = 0 $.

A Riemann problem is a conservation law with piecewise constant initial data. Here the initial data is posed at $t = 0$ and the jump between the piecewise constant states located at $x = 0$.

The problem is scalar if $q$ and $f$ are scalar functions.

The problem is convex if $f''(q)$ has a definite sign for all values of $q$. Sometimes it is sufficient to consider a restricted range of $q$ -- those that are required in the solution of the Riemann problem.

Solution:

The solution of a Riemann problem for a system of conservation laws of size $N$ consists of $(N+1)$ piecewise constant states separated by $N$ waves. The solution is self-similar -- a function only of $\xi = x / t$ -- for $t > 0$. The waves may be continuous and cover a range of values of $\xi$, or discontinuous at a single value of $\xi$. A wave may consist of a family of subwaves (a wave containing subwaves is called compound).

In the scalar, convex case there is only one wave, and all waves must be simple (i.e., not compound).
