# robust-shrinkage-benchmark

A small, fully reproducible simulation study of one question:

> When predictors are strongly correlated **and** a share of the observations are outliers, which estimators
> keep their accuracy: ridge-type shrinkage, the Kibria-Lukman (KL) estimator, the LASSO, or a *robust-first* hybrid
> that trims suspect observations before selecting variables?

Methods for correlated predictors (ridge, KL) and methods that resist outliers (trimming) are usually studied separately,
although industrial sensor and process data often have both problems. This repository puts them side by side under
identical, documented conditions, so that anyone can rerun every number below.

## What is compared (`robust_shrinkage_benchmark/estimators.py`)

| Method | Description |
|---|---|
| OLS | ordinary least squares |
| Ridge | ridge, penalty chosen by cross-validation |
| KL (as published) | Kibria-Lukman estimator in canonical form, shrinkage factor (lambda_j - k)/(lambda_j + k), k estimated as min_j sigma^2/(2 alpha_j^2 + sigma^2/lambda_j) |
| KL (factor clipped to [0,1]) | same, with the factor limited to [0,1] because it is negative whenever k exceeds lambda_j |
| LASSO | cross-validated LASSO |
| LASSO select -> Ridge / KL | select variables with LASSO, then fit Ridge or KL on the selected variables |
| Trimmed-LASSO select -> Ridge / KL | repeatedly fit LASSO, drop the 25% of observations with the largest residuals, refit until the retained set is stable; then fit Ridge or KL on the selected variables **using the retained observations only** |

The trimmed selector is a simple from-scratch scheme in the spirit of sparse least trimmed squares. It is **not** the
FAST-LTS algorithm of the R package `robustHD`.

## Data (`robust_shrinkage_benchmark/data.py`)

* n = 200 observations, p = 30 predictors, AR(1) correlation rho^|i-j| with rho in {0.5, 0.9, 0.99}.
* "sparse" coefficients (5 nonzero, magnitude 2 or 3) or "dense" coefficients (all 30 nonzero, magnitude 0.3 or 0.5). Noise sd = 1.
* Contamination share eps in {0, 0.1, 0.2}. "response" outliers shift y by +/- 10 sd; "leverage" outliers also move the row of X far from the bulk.
* **Test data are always clean** (1,000 new observations), so test RMSE measures how well the true relationship was recovered.
* 30 replications per cell; 22 cells; 9 methods; 5,940 fitted results in `results/raw_results.csv`. Seeds are derived from the cell and replication index.

## Reproduce

```bash
pip install -r requirements.txt
pytest -q                      # 6 tests, a few seconds
python run_benchmark.py        # full grid, about 10 minutes on two CPU cores
python summarize.py            # writes results/summary.md
```

`python run_benchmark.py --quick` runs a three-replication smoke test in seconds.

## What the results show (see `results/summary.md` for every cell)

1. **With contamination, the robust-first hybrids were best in all 16 contaminated cells** (response and leverage outliers, eps = 0.1 and 0.2, both coefficient structures, all rho tested). Their mean test RMSE was 7% to 36% lower than the best non-robust method in the same cell (median 21% lower).
   Example: sparse coefficients, rho = 0.9, 20% response outliers: Trimmed-LASSO -> Ridge 1.10, LASSO 1.59, Ridge 1.76, OLS 2.18.
2. **Without contamination, the robust hybrids lose a little**: their best RMSE was 4% to 7% higher than the best non-robust method in all six uncontaminated cells (for example 1.11 against 1.05 for the LASSO at rho = 0.5, sparse). Trimming throws away good data when there are no outliers.
3. **Under leverage outliers the advantage narrows** (sparse, rho = 0.9, eps = 0.2: 2.44 against 2.80 for OLS), because the trimming rule looks only at residuals.
4. **KL as published behaved like OLS in this design** (n = 200, p = 30): its estimated k was small (about 0.05 at rho = 0.99, against smallest eigenvalues above 0.5 in the cells checked), so there was almost no shrinkage, the factor was never negative, and clipping it changed nothing here. The KL stage showed no advantage over Ridge after the robust step. This benchmark does not test KL where it is expected to help most (very small n relative to p, extreme collinearity).
5. **Variable selection is not uniformly better.** The robust selector's F1 against the true support was about 0.4 to 0.5 in every cell. The plain LASSO's F1 was higher in most response-outlier cells (for example 0.57 against 0.44 at rho = 0.5, eps = 0.1), and lower only where collinearity is extreme and contamination present (rho = 0.99: 0.40 against 0.48 at eps = 0.1, and 0.31 against 0.52 at eps = 0.2) and under leverage outliers (0.25 against 0.40 at eps = 0.2). The robust gain in prediction comes mainly from fitting on the retained observations, not from sharper selection.

## Limitations

* Simulation only. No real data are used here.
* One sample size and dimension (n = 200, p = 30); no p > n case.
* Two contamination models, both with a fixed fraction and fixed size. Other patterns (heavy-tailed noise, clustered outliers, drifting sensors) are not tested.
* The trimmed selector is a simple approximation, not sparse LTS itself; it keeps more variables than the true support.
* 30 replications per cell; standard errors are given in `results/summary.md`.

## License

MIT. Author: Christian Nnaemeka Nwaeme.
