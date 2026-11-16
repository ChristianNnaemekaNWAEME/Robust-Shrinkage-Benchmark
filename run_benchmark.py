"""Run the benchmark and write results/raw_results.csv.

    python run_benchmark.py            # full grid (several minutes)
    python run_benchmark.py --quick    # tiny grid, for a smoke test
Then:  python summarize.py
"""
import argparse, itertools, time
import numpy as np, pandas as pd
from robust_shrinkage_benchmark.data import generate
from robust_shrinkage_benchmark.estimators import make_methods
from robust_shrinkage_benchmark.metrics import test_rmse, coef_error, selection_f1


def seed_for(n, p, rho, structure, eps, kind, rep):
    key = [n, p, int(rho * 1000), 0 if structure == "sparse" else 1, int(eps * 1000), 0 if kind == "response" else 1, rep]
    return int(np.random.SeedSequence(key).generate_state(1)[0])


def run(grid, reps, out):
    rows, methods, t0 = [], make_methods(), time.time()
    for cell in grid:
        n, p, rho, structure, eps, kind = cell
        for r in range(reps):
            ds = generate(n=n, p=p, rho=rho, structure=structure, eps=eps, kind=kind,
                          seed=seed_for(*cell, r))
            for name, make in methods.items():
                m = make().fit(ds.X, ds.y)
                rows.append(dict(n=n, p=p, rho=rho, structure=structure, eps=eps, kind=kind, rep=r, method=name,
                                 test_rmse=test_rmse(m, ds), coef_error=coef_error(m, ds),
                                 f1=selection_f1(m, ds) if structure == "sparse" else np.nan))
        print(f"done {cell}  ({time.time() - t0:.0f}s)", flush=True)
    pd.DataFrame(rows).to_csv(out, index=False)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()
    if a.quick:
        grid, reps, out = [(100, 20, 0.9, "sparse", 0.1, "response")], 3, "results/quick.csv"
    else:
        grid = [(200, 30, rho, st, eps, "response")
                for rho, st, eps in itertools.product([0.5, 0.9, 0.99], ["sparse", "dense"], [0.0, 0.1, 0.2])]
        grid += [(200, 30, 0.9, st, eps, "leverage") for st in ["sparse", "dense"] for eps in [0.1, 0.2]]
        reps, out = 30, "results/raw_results.csv"
    run(grid, reps, out)
