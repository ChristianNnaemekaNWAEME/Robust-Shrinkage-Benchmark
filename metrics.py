import numpy as np


def test_rmse(model, ds):
    return float(np.sqrt(np.mean((model.predict(ds.X_test) - ds.y_test) ** 2)))


def coef_error(model, ds):
    return float(np.linalg.norm(model.coef_ - ds.beta))


def selection_f1(model, ds, tol=1e-8):
    """F1 of the set of variables with nonzero estimated coefficient vs. the true support (sparse only)."""
    est = np.abs(model.coef_) > tol
    true = np.abs(ds.beta) > 0
    tp = int((est & true).sum())
    if tp == 0:
        return 0.0
    prec, rec = tp / est.sum(), tp / true.sum()
    return 2 * prec * rec / (prec + rec)
