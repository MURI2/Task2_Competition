# Task2_Competition

### Finding an appropriate measure of competitive fitness

##### Things our measure of fitness has to take into account:

1) The environment is deterministic (i.e., transfers happen at the same time every time)

2) The environment is cyclical (i.e., each transfer it goes back to the same state)

3) The change in environmental quality happens slowly, so it is continous. There are no discrete "starvation" and "no starvation" states. The environment slowly changes and decays over time.


We intuitively expect that average geometric fitness (i.e., the expected multiplicative growth rate) is maximized under long-term starvation. 

When fitness is $$r$$, at generation $$t$$ the population size $$N$$ is:

$$N(t)= \left ( \prod_{i=0}^{t-1}r_{i} \right )N_{0}$$

And the geometric mean fitnes ($$G$$) is the average population growth rate per-generation:

$$G= \prod_{i=0}^{t-1} r_{i}^{1/t}$$

Assuming that growth rates ($$r_{i}$$) are drawn from probability distribution ($$h(r)$$), geometric mean fitness can be expressed as:

$$G = \prod_{r}r^{h(r)}$$

This formula becomes very simple when the distribution of growth rates is assumed to be log-normal.

$$P(r; \mu, \sigma)= \left ( \frac{1}{r\sqrt{2\pi}\sigma}\right ) exp\left ( - \frac{(ln(r) - \mu)^{2}}{2\sigma^{2}}\right )$$

using this distribution as $$h(r)$$, the logarithmic form of the geometric mean fitness can be analytically solved and reduces to the mean of the lognormal distribution, so:

$$w = ln \,G = \mu = \mathbf{E}[ln \, r]$$

See Yoshimura et al. (2009) for the derivation. 



  