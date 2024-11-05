import pymc as pm
import numpy as np

mu = pm.Normal('mu', mu=160, sigma=15)
sigma = pm.HalfNormal('sigma', sigma=10)
heights = pm.Normal('heights', mu=mu, sigma=sigma, observed=observed_heights)

print("Începem eșantionarea MCMC...")
trace = pm.sample(1000, tune=1000, return_inferencedata=True)
print("Eșantionarea MCMC s-a încheiat.")