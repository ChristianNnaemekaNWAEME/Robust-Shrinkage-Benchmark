import numpy as np
from robust_shrinkage_benchmark.data import generate
from robust_shrinkage_benchmark.estimators import OLS, KL, Ridge, trimmed_lasso_select, lasso_select


def test_reproducible():
    a, b = generate(seed=3), generate(seed=3)
    assert np.array_equal(a.X, b.X) and np.array_equal(a.y, b.y)


def test_contamination_count_and_clean_test():
    ds = generate(n=200, eps=0.1, seed=1)
    assert ds.outlier_mask.sum() == 20
    clean = generate(n=200, eps=0.0, seed=1)
    assert np.allclose(ds.X_test, clean.X_test) and np.allclose(ds.y_test, clean.y_test)  # test set never changes
    keep = ~ds.outlier_mask
    assert np.allclose(ds.X[keep], clean.X[keep]) and np.allclose(ds.y[keep], clean.y[keep])  # same clean sample


def test_kl_factor_negative_without_clip():
    # With a very large k the published factor (lam-k)/(lam+k) is negative; clipping keeps it in [0,1].
    rng = np.random.default_rng(0)
    X = rng.standard_normal((60, 5)); X[:, 4] = X[:, 3] + 1e-3 * rng.standard_normal(60)
    y = X @ np.ones(5) + 0.1 * rng.standard_normal(60)
    raw, clipped = KL(clip=False).fit(X, y), KL(clip=True).fit(X, y)
    assert np.isfinite(raw.coef_).all() and np.isfinite(clipped.coef_).all()
    assert np.linalg.norm(clipped.coef_) <= np.linalg.norm(OLS().fit(X, y).coef_) + 1e-8


def test_ols_recovers_clean_signal():
    ds = generate(n=500, p=5, rho=0.3, eps=0.0, structure="sparse", n_active=3, seed=2)
    assert np.linalg.norm(OLS().fit(ds.X, ds.y).coef_ - ds.beta) < 0.3


def test_trimming_flags_outliers():
    ds = generate(n=200, p=10, rho=0.5, eps=0.1, structure="sparse", n_active=3, seed=4)
    _, retained = trimmed_lasso_select(ds.X, ds.y)
    kept_outliers = ds.outlier_mask[retained].sum()
    assert kept_outliers <= 4  # most of the 20 outliers are trimmed away


def test_robust_selection_beats_lasso_selection_under_contamination():
    f1s_r, f1s_l = [], []
    for s in range(5):
        ds = generate(n=200, p=30, rho=0.9, eps=0.2, structure="sparse", n_active=5, seed=10 + s)
        true = ds.beta != 0
        for sel, store in ((trimmed_lasso_select(ds.X, ds.y)[0], f1s_r), (lasso_select(ds.X, ds.y)[0], f1s_l)):
            tp = (sel & true).sum(); store.append(0 if tp == 0 else 2 * tp / (sel.sum() + true.sum()))
    print(np.mean(f1s_r), np.mean(f1s_l))
    assert np.mean(f1s_r) >= np.mean(f1s_l) - 0.05
