"""Estimators compared in the benchmark.

KL: the Kibria-Lukman ridge-type estimator in canonical form. With the SVD X = U D V', lambda_j = d_j^2
and alpha_hat = V' beta_OLS, the estimator shrinks each canonical coefficient by (lambda_j - k)/(lambda_j + k).
The shrinkage constant k is estimated as min_j sigma^2 / (2 alpha_j^2 + sigma^2 / lambda_j).
Note that (lambda_j - k)/(lambda_j + k) is NEGATIVE when k exceeds lambda_j; the estimator is therefore
used both as published (clip=False) and with the factor limited to [0, 1] (clip=True). The benchmark reports both.

Robust selector: trimmed LASSO. Repeatedly fit a cross-validated LASSO on the retained observations,
keep the h observations with smallest squared residuals, and stop when the retained set stops changing.
This is a simple, from-scratch trimming scheme in the spirit of sparse least trimmed squares; it is NOT the
FAST-LTS algorithm of the robustHD package.
"""
import numpy as np
from sklearn.linear_model import LassoCV, RidgeCV, Lasso


def _center(X, y):
    xm, ym = X.mean(0), y.mean()
    return X - xm, y - ym, xm, ym


class Linear:
    """Base class: fit on centered data, predict with intercept."""
    def _finish(self, coef, xm, ym):
        self.coef_ = coef
        self.intercept_ = ym - xm @ coef
        return self

    def predict(self, X):
        return X @ self.coef_ + self.intercept_


class OLS(Linear):
    def fit(self, X, y):
        Xc, yc, xm, ym = _center(X, y)
        coef = np.linalg.lstsq(Xc, yc, rcond=None)[0]
        return self._finish(coef, xm, ym)


class Ridge(Linear):
    def fit(self, X, y):
        Xc, yc, xm, ym = _center(X, y)
        m = RidgeCV(alphas=np.logspace(-3, 3, 25), fit_intercept=False).fit(Xc, yc)
        return self._finish(m.coef_, xm, ym)


class KL(Linear):
    def __init__(self, clip=False):
        self.clip = clip

    def fit(self, X, y):
        Xc, yc, xm, ym = _center(X, y)
        n, p = Xc.shape
        U, d, Vt = np.linalg.svd(Xc, full_matrices=False)
        lam = d ** 2
        keep = d > 1e-10 * d.max()
        alpha = (Vt @ np.linalg.lstsq(Xc, yc, rcond=None)[0])
        resid = yc - Xc @ np.linalg.lstsq(Xc, yc, rcond=None)[0]
        dof = max(n - int(keep.sum()) - 1, 1)
        s2 = float(resid @ resid) / dof
        with np.errstate(divide="ignore", invalid="ignore"):
            kj = s2 / (2 * alpha[keep] ** 2 + s2 / lam[keep])
        k = float(np.nanmin(kj)) if kj.size else 0.0
        factor = (lam - k) / (lam + k)
        if self.clip:
            factor = np.clip(factor, 0.0, 1.0)
        self.k_ = k
        coef = Vt.T @ (factor * alpha)
        return self._finish(coef, xm, ym)


class LassoModel(Linear):
    def fit(self, X, y):
        Xc, yc, xm, ym = _center(X, y)
        m = LassoCV(cv=5, max_iter=20000).fit(Xc, yc)
        return self._finish(m.coef_, xm, ym)


def lasso_select(X, y):
    Xc, yc, _, _ = _center(X, y)
    m = LassoCV(cv=5, max_iter=20000).fit(Xc, yc)
    return np.abs(m.coef_) > 1e-10, np.arange(len(y))


def trimmed_lasso_select(X, y, h_fraction=0.75, max_iter=30):
    n, p = X.shape
    h = int(np.floor(h_fraction * n))
    retained = np.arange(n)
    prev = None
    coef = np.zeros(p)
    for _ in range(max_iter):
        Xc, yc, xm, ym = _center(X[retained], y[retained])
        m = LassoCV(cv=min(5, len(retained)), max_iter=20000).fit(Xc, yc)
        coef = m.coef_
        b0 = ym - xm @ coef
        res = (y - (X @ coef + b0)) ** 2
        new = np.sort(np.argsort(res)[:h])
        if prev is not None and np.array_equal(new, prev):
            retained = new
            break
        prev = retained = new
    return np.abs(coef) > 1e-10, retained


class Hybrid(Linear):
    """Two stages: select variables, then fit a second-stage estimator on the selected variables.
    robust=True uses the trimmed selector and fits stage two on the retained (non-trimmed) observations only."""
    def __init__(self, robust, second):
        self.robust, self.second = robust, second

    def fit(self, X, y):
        mask, rows = trimmed_lasso_select(X, y) if self.robust else lasso_select(X, y)
        if not mask.any():
            mask = np.ones(X.shape[1], dtype=bool)
        if not self.robust:
            rows = np.arange(len(y))
        stage = {"ridge": Ridge(), "kl": KL(clip=True)}[self.second]
        stage.fit(X[np.ix_(rows, np.where(mask)[0])], y[rows])
        coef = np.zeros(X.shape[1])
        coef[mask] = stage.coef_
        self.mask_ = mask
        return self._finish(coef, X[rows].mean(0), y[rows].mean())


def make_methods():
    return {
        "OLS": OLS,
        "Ridge": Ridge,
        "KL (as published)": lambda: KL(clip=False),
        "KL (factor clipped to [0,1])": lambda: KL(clip=True),
        "LASSO": LassoModel,
        "LASSO select -> Ridge": lambda: Hybrid(False, "ridge"),
        "LASSO select -> KL": lambda: Hybrid(False, "kl"),
        "Trimmed-LASSO select -> Ridge": lambda: Hybrid(True, "ridge"),
        "Trimmed-LASSO select -> KL": lambda: Hybrid(True, "kl"),
    }
