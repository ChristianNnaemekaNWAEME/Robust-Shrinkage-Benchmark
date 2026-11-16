"""Summarize results/raw_results.csv into results/summary.md (mean and standard error over replications)."""
import numpy as np, pandas as pd

df = pd.read_csv("results/raw_results.csv")
order = list(dict.fromkeys(df["method"]))
out = ["# Benchmark summary\n",
       "Mean over replications (standard error in parentheses). Test data are clean. Lower RMSE and coefficient error are better; higher F1 is better.\n"]


def fmt(g, col):
    m, se = g[col].mean(), g[col].std(ddof=1) / np.sqrt(len(g))
    return f"{m:.3f} ({se:.3f})"


for (kind, structure, rho, eps), cell in df.groupby(["kind", "structure", "rho", "eps"]):
    out.append(f"\n## contamination={kind}, coefficients={structure}, rho={rho}, eps={eps}  (n={int(cell.n.iloc[0])}, p={int(cell.p.iloc[0])}, reps={cell.rep.nunique()})\n")
    out.append("| method | test RMSE | coefficient error | selection F1 |\n|---|---|---|---|")
    best = cell.groupby("method")["test_rmse"].mean().idxmin()
    for m in order:
        g = cell[cell.method == m]
        f1 = fmt(g, "f1") if structure == "sparse" else "n/a"
        name = f"**{m}**" if m == best else m
        out.append(f"| {name} | {fmt(g, 'test_rmse')} | {fmt(g, 'coef_error')} | {f1} |")
    out.append(f"\nLowest mean test RMSE: {best}.")
open("results/summary.md", "w").write("\n".join(out) + "\n")

# win counts
cells = df.groupby(["kind", "structure", "rho", "eps"])
wins = pd.Series(0, index=order)
for _, c in cells:
    wins[c.groupby("method")["test_rmse"].mean().idxmin()] += 1
print("Cells in which each method has the lowest mean test RMSE (of %d cells):" % len(cells))
print(wins[wins > 0].to_string())
