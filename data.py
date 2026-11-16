"""Synthetic regression data with correlated predictors and a contaminated response.

Design (all choices are explicit arguments, so every number in the results can be reproduced):
  * Predictors: multivariate normal with AR(1) correlation, corr(x_i, x_j) = rho**|i-j|.
  * Coefficients: "sparse" = n_active nonzero coefficients; "dense" = every coefficient nonzero and small.
  * Noise: N(0, sigma^2).
  * Contamination: a fraction eps of observations is replaced by outliers.
      - "response": the response is shifted by +/- shift*sigma (outliers in y only).
      - "leverage": the row of X is also moved far from the bulk (bad leverage points), and y is shifted.
  * Test data are always generated WITHOUT contamination, so test error measures how well the
    underlying relationship was recovered, not how well outliers were reproduced.
"""
from dataclasses import dataclass
import numpy as np


@dataclass
class Dataset:
    X: np.ndarray
    y: np.ndarray
    X_test: np.ndarray
    y_test: np.ndarray
    beta: np.ndarray
    outlier_mask: np.ndarray


def _cov(p, rho):
    idx = np.arange(p)
    return rho ** np.abs(idx[:, None] - idx[None, :])


def make_beta(p, structure, n_active, rng):
    beta = np.zeros(p)
    if structure == "sparse":
        active = rng.choice(p, size=n_active, replace=False)
        beta[active] = rng.choice([-3.0, -2.0, 2.0, 3.0], size=n_active)
    elif structure == "dense":
        beta[:] = rng.choice([-0.5, -0.3, 0.3, 0.5], size=p)
    else:
        raise ValueError(structure)
    return beta


def generate(n=200, p=30, rho=0.9, sigma=1.0, structure="sparse", n_active=5,
             eps=0.1, shift=10.0, kind="response", n_test=1000, seed=0):
    # Three independent random streams, so that (i) the clean training data, (ii) the contamination and
    # (iii) the test data do not depend on each other. Datasets that differ only in eps therefore share the
    # same underlying clean sample, and the test set never changes with eps.
    ss = np.random.SeedSequence(seed)
    rng, rng_c, rng_t = (np.random.default_rng(s) for s in ss.spawn(3))
    L = np.linalg.cholesky(_cov(p, rho))
    X = rng.standard_normal((n, p)) @ L.T
    beta = make_beta(p, structure, n_active, rng)
    y = X @ beta + sigma * rng.standard_normal(n)

    mask = np.zeros(n, dtype=bool)
    k = int(round(eps * n))
    if k > 0:
        idx = rng_c.choice(n, size=k, replace=False)
        mask[idx] = True
        sign = rng_c.choice([-1.0, 1.0], size=k)
        y[idx] = y[idx] + sign * shift * sigma
        if kind == "leverage":
            X[idx] = X[idx] + 4.0 * rng_c.standard_normal((k, p))
        elif kind != "response":
            raise ValueError(kind)

    X_test = rng_t.standard_normal((n_test, p)) @ L.T
    y_test = X_test @ beta + sigma * rng_t.standard_normal(n_test)
    return Dataset(X, y, X_test, y_test, beta, mask)
