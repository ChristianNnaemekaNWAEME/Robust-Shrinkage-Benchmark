# Benchmark summary

Mean over replications (standard error in parentheses). Test data are clean. Lower RMSE and coefficient error are better; higher F1 is better.


## contamination=leverage, coefficients=dense, rho=0.9, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.632 (0.022) | 3.792 (0.092) | n/a |
| Ridge | 1.625 (0.042) | 2.284 (0.067) | n/a |
| KL (as published) | 1.620 (0.021) | 3.719 (0.091) | n/a |
| KL (factor clipped to [0,1]) | 1.620 (0.021) | 3.719 (0.091) | n/a |
| LASSO | 1.821 (0.061) | 2.333 (0.042) | n/a |
| LASSO select -> Ridge | 1.678 (0.041) | 2.508 (0.068) | n/a |
| LASSO select -> KL | 1.703 (0.037) | 2.904 (0.117) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.226 (0.014) | 1.765 (0.053) | n/a |
| Trimmed-LASSO select -> KL | 1.230 (0.013) | 1.818 (0.049) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=leverage, coefficients=dense, rho=0.9, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.892 (0.040) | 3.451 (0.079) | n/a |
| Ridge | 1.743 (0.052) | 2.228 (0.032) | n/a |
| KL (as published) | 1.873 (0.040) | 3.377 (0.080) | n/a |
| KL (factor clipped to [0,1]) | 1.873 (0.040) | 3.377 (0.080) | n/a |
| LASSO | 1.985 (0.063) | 2.247 (0.032) | n/a |
| LASSO select -> Ridge | 1.742 (0.046) | 2.309 (0.041) | n/a |
| LASSO select -> KL | 1.803 (0.039) | 2.785 (0.110) | n/a |
| Trimmed-LASSO select -> Ridge | 1.206 (0.019) | 1.762 (0.048) | n/a |
| **Trimmed-LASSO select -> KL** | 1.203 (0.016) | 1.806 (0.047) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=leverage, coefficients=sparse, rho=0.9, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.297 (0.047) | 6.124 (0.144) | 0.286 (0.000) |
| Ridge | 2.942 (0.085) | 5.435 (0.086) | 0.286 (0.000) |
| KL (as published) | 2.286 (0.046) | 6.059 (0.142) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 2.286 (0.046) | 6.059 (0.142) | 0.286 (0.000) |
| LASSO | 3.028 (0.102) | 5.452 (0.097) | 0.303 (0.026) |
| LASSO select -> Ridge | 2.809 (0.074) | 5.427 (0.091) | 0.312 (0.023) |
| LASSO select -> KL | 2.560 (0.069) | 5.559 (0.103) | 0.312 (0.023) |
| Trimmed-LASSO select -> Ridge | 2.079 (0.109) | 4.169 (0.225) | 0.418 (0.022) |
| **Trimmed-LASSO select -> KL** | 1.921 (0.091) | 4.024 (0.221) | 0.418 (0.022) |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=leverage, coefficients=sparse, rho=0.9, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.806 (0.062) | 5.600 (0.123) | 0.286 (0.000) |
| Ridge | 3.442 (0.106) | 5.137 (0.084) | 0.286 (0.000) |
| KL (as published) | 2.795 (0.061) | 5.538 (0.121) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 2.795 (0.061) | 5.538 (0.121) | 0.286 (0.000) |
| LASSO | 3.611 (0.134) | 5.240 (0.096) | 0.248 (0.027) |
| LASSO select -> Ridge | 3.337 (0.109) | 5.224 (0.095) | 0.257 (0.026) |
| LASSO select -> KL | 3.067 (0.094) | 5.311 (0.102) | 0.257 (0.026) |
| Trimmed-LASSO select -> Ridge | 2.576 (0.125) | 4.665 (0.138) | 0.397 (0.020) |
| **Trimmed-LASSO select -> KL** | 2.444 (0.119) | 4.617 (0.147) | 0.397 (0.020) |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=response, coefficients=dense, rho=0.5, eps=0.0  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.084 (0.006) | 0.519 (0.015) | n/a |
| Ridge | 1.079 (0.006) | 0.501 (0.014) | n/a |
| KL (as published) | 1.082 (0.006) | 0.511 (0.015) | n/a |
| KL (factor clipped to [0,1]) | 1.082 (0.006) | 0.511 (0.015) | n/a |
| LASSO | 1.083 (0.006) | 0.520 (0.014) | n/a |
| **LASSO select -> Ridge** | 1.079 (0.006) | 0.501 (0.014) | n/a |
| LASSO select -> KL | 1.082 (0.006) | 0.511 (0.015) | n/a |
| Trimmed-LASSO select -> Ridge | 1.151 (0.010) | 0.712 (0.023) | n/a |
| Trimmed-LASSO select -> KL | 1.155 (0.010) | 0.724 (0.024) | n/a |

Lowest mean test RMSE: LASSO select -> Ridge.

## contamination=response, coefficients=dense, rho=0.5, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.745 (0.025) | 1.799 (0.047) | n/a |
| Ridge | 1.515 (0.021) | 1.352 (0.036) | n/a |
| KL (as published) | 1.669 (0.024) | 1.646 (0.045) | n/a |
| KL (factor clipped to [0,1]) | 1.669 (0.024) | 1.646 (0.045) | n/a |
| LASSO | 1.693 (0.025) | 1.675 (0.036) | n/a |
| LASSO select -> Ridge | 1.589 (0.025) | 1.497 (0.042) | n/a |
| LASSO select -> KL | 1.718 (0.021) | 1.732 (0.035) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.196 (0.010) | 0.807 (0.025) | n/a |
| Trimmed-LASSO select -> KL | 1.199 (0.010) | 0.817 (0.025) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=dense, rho=0.5, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.227 (0.038) | 2.481 (0.070) | n/a |
| Ridge | 1.810 (0.025) | 1.671 (0.030) | n/a |
| KL (as published) | 2.092 (0.038) | 2.226 (0.069) | n/a |
| KL (factor clipped to [0,1]) | 2.092 (0.038) | 2.226 (0.069) | n/a |
| LASSO | 1.966 (0.030) | 1.940 (0.039) | n/a |
| LASSO select -> Ridge | 1.924 (0.029) | 1.881 (0.050) | n/a |
| LASSO select -> KL | 2.096 (0.035) | 2.154 (0.059) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.157 (0.009) | 0.688 (0.021) | n/a |
| Trimmed-LASSO select -> KL | 1.158 (0.009) | 0.697 (0.022) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=dense, rho=0.9, eps=0.0  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.088 (0.005) | 1.303 (0.041) | n/a |
| **Ridge** | 1.069 (0.005) | 1.117 (0.028) | n/a |
| KL (as published) | 1.081 (0.005) | 1.231 (0.038) | n/a |
| KL (factor clipped to [0,1]) | 1.081 (0.005) | 1.231 (0.038) | n/a |
| LASSO | 1.095 (0.006) | 1.385 (0.035) | n/a |
| LASSO select -> Ridge | 1.079 (0.006) | 1.230 (0.034) | n/a |
| LASSO select -> KL | 1.092 (0.006) | 1.345 (0.036) | n/a |
| Trimmed-LASSO select -> Ridge | 1.144 (0.007) | 1.636 (0.039) | n/a |
| Trimmed-LASSO select -> KL | 1.154 (0.008) | 1.719 (0.040) | n/a |

Lowest mean test RMSE: Ridge.

## contamination=response, coefficients=dense, rho=0.9, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.793 (0.032) | 4.543 (0.136) | n/a |
| Ridge | 1.351 (0.020) | 2.008 (0.075) | n/a |
| KL (as published) | 1.680 (0.031) | 3.922 (0.135) | n/a |
| KL (factor clipped to [0,1]) | 1.680 (0.031) | 3.922 (0.135) | n/a |
| LASSO | 1.411 (0.024) | 2.383 (0.103) | n/a |
| LASSO select -> Ridge | 1.404 (0.022) | 2.317 (0.088) | n/a |
| LASSO select -> KL | 1.506 (0.036) | 2.809 (0.169) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.152 (0.009) | 1.559 (0.032) | n/a |
| Trimmed-LASSO select -> KL | 1.161 (0.009) | 1.652 (0.033) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=dense, rho=0.9, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.156 (0.042) | 5.714 (0.180) | n/a |
| Ridge | 1.435 (0.022) | 1.993 (0.052) | n/a |
| KL (as published) | 1.966 (0.042) | 4.756 (0.192) | n/a |
| KL (factor clipped to [0,1]) | 1.966 (0.042) | 4.756 (0.192) | n/a |
| LASSO | 1.500 (0.023) | 2.336 (0.042) | n/a |
| LASSO select -> Ridge | 1.528 (0.025) | 2.442 (0.084) | n/a |
| LASSO select -> KL | 1.655 (0.037) | 2.920 (0.151) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.121 (0.006) | 1.419 (0.042) | n/a |
| Trimmed-LASSO select -> KL | 1.138 (0.007) | 1.567 (0.044) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=dense, rho=0.99, eps=0.0  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.097 (0.006) | 4.110 (0.123) | n/a |
| **Ridge** | 1.040 (0.005) | 1.879 (0.051) | n/a |
| KL (as published) | 1.079 (0.005) | 3.460 (0.118) | n/a |
| KL (factor clipped to [0,1]) | 1.079 (0.005) | 3.460 (0.118) | n/a |
| LASSO | 1.051 (0.005) | 2.293 (0.071) | n/a |
| LASSO select -> Ridge | 1.048 (0.005) | 2.157 (0.067) | n/a |
| LASSO select -> KL | 1.062 (0.006) | 2.615 (0.119) | n/a |
| Trimmed-LASSO select -> Ridge | 1.081 (0.007) | 2.584 (0.116) | n/a |
| Trimmed-LASSO select -> KL | 1.088 (0.007) | 2.825 (0.152) | n/a |

Lowest mean test RMSE: Ridge.

## contamination=response, coefficients=dense, rho=0.99, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.721 (0.030) | 13.358 (0.437) | n/a |
| Ridge | 1.150 (0.015) | 2.273 (0.112) | n/a |
| KL (as published) | 1.595 (0.030) | 11.027 (0.466) | n/a |
| KL (factor clipped to [0,1]) | 1.595 (0.030) | 11.027 (0.466) | n/a |
| LASSO | 1.178 (0.019) | 2.868 (0.172) | n/a |
| LASSO select -> Ridge | 1.188 (0.023) | 3.060 (0.277) | n/a |
| LASSO select -> KL | 1.242 (0.034) | 3.861 (0.498) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.075 (0.007) | 2.378 (0.089) | n/a |
| Trimmed-LASSO select -> KL | 1.081 (0.008) | 2.602 (0.113) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=dense, rho=0.99, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.178 (0.036) | 18.764 (0.409) | n/a |
| Ridge | 1.262 (0.030) | 2.515 (0.192) | n/a |
| KL (as published) | 1.994 (0.038) | 15.639 (0.478) | n/a |
| KL (factor clipped to [0,1]) | 1.994 (0.038) | 15.639 (0.478) | n/a |
| LASSO | 1.261 (0.026) | 2.715 (0.184) | n/a |
| LASSO select -> Ridge | 1.279 (0.033) | 2.823 (0.245) | n/a |
| LASSO select -> KL | 1.355 (0.050) | 3.941 (0.653) | n/a |
| **Trimmed-LASSO select -> Ridge** | 1.057 (0.008) | 2.302 (0.101) | n/a |
| Trimmed-LASSO select -> KL | 1.069 (0.009) | 2.639 (0.144) | n/a |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=sparse, rho=0.5, eps=0.0  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.088 (0.005) | 0.518 (0.012) | 0.286 (0.000) |
| Ridge | 1.087 (0.005) | 0.515 (0.012) | 0.286 (0.000) |
| KL (as published) | 1.088 (0.005) | 0.517 (0.012) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.088 (0.005) | 0.517 (0.012) | 0.286 (0.000) |
| **LASSO** | 1.045 (0.005) | 0.301 (0.017) | 0.610 (0.020) |
| LASSO select -> Ridge | 1.056 (0.005) | 0.351 (0.017) | 0.610 (0.020) |
| LASSO select -> KL | 1.056 (0.005) | 0.349 (0.018) | 0.610 (0.020) |
| Trimmed-LASSO select -> Ridge | 1.112 (0.008) | 0.537 (0.024) | 0.480 (0.022) |
| Trimmed-LASSO select -> KL | 1.111 (0.008) | 0.534 (0.024) | 0.480 (0.022) |

Lowest mean test RMSE: LASSO.

## contamination=response, coefficients=sparse, rho=0.5, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.740 (0.028) | 1.819 (0.058) | 0.286 (0.000) |
| Ridge | 1.680 (0.026) | 1.695 (0.056) | 0.286 (0.000) |
| KL (as published) | 1.720 (0.027) | 1.777 (0.058) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.720 (0.027) | 1.777 (0.058) | 0.286 (0.000) |
| LASSO | 1.369 (0.023) | 1.063 (0.050) | 0.568 (0.016) |
| LASSO select -> Ridge | 1.526 (0.029) | 1.327 (0.058) | 0.568 (0.016) |
| LASSO select -> KL | 1.533 (0.029) | 1.333 (0.060) | 0.568 (0.016) |
| Trimmed-LASSO select -> Ridge | 1.133 (0.009) | 0.603 (0.024) | 0.441 (0.017) |
| **Trimmed-LASSO select -> KL** | 1.132 (0.009) | 0.599 (0.025) | 0.441 (0.017) |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=response, coefficients=sparse, rho=0.5, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.187 (0.038) | 2.368 (0.058) | 0.286 (0.000) |
| Ridge | 2.115 (0.033) | 2.202 (0.052) | 0.286 (0.000) |
| KL (as published) | 2.143 (0.036) | 2.279 (0.054) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 2.143 (0.036) | 2.279 (0.054) | 0.286 (0.000) |
| LASSO | 1.736 (0.041) | 1.514 (0.070) | 0.571 (0.019) |
| LASSO select -> Ridge | 1.898 (0.042) | 1.779 (0.067) | 0.571 (0.019) |
| LASSO select -> KL | 1.899 (0.045) | 1.756 (0.069) | 0.571 (0.019) |
| Trimmed-LASSO select -> Ridge | 1.104 (0.008) | 0.498 (0.023) | 0.526 (0.020) |
| **Trimmed-LASSO select -> KL** | 1.103 (0.008) | 0.493 (0.023) | 0.526 (0.020) |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=response, coefficients=sparse, rho=0.9, eps=0.0  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.094 (0.007) | 1.267 (0.043) | 0.286 (0.000) |
| Ridge | 1.090 (0.007) | 1.240 (0.042) | 0.286 (0.000) |
| KL (as published) | 1.093 (0.007) | 1.254 (0.043) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.093 (0.007) | 1.254 (0.043) | 0.286 (0.000) |
| **LASSO** | 1.047 (0.006) | 0.702 (0.044) | 0.538 (0.019) |
| LASSO select -> Ridge | 1.065 (0.007) | 0.883 (0.059) | 0.538 (0.019) |
| LASSO select -> KL | 1.065 (0.008) | 0.868 (0.061) | 0.538 (0.019) |
| Trimmed-LASSO select -> Ridge | 1.111 (0.008) | 1.144 (0.065) | 0.448 (0.016) |
| Trimmed-LASSO select -> KL | 1.110 (0.008) | 1.130 (0.065) | 0.448 (0.016) |

Lowest mean test RMSE: LASSO.

## contamination=response, coefficients=sparse, rho=0.9, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.728 (0.024) | 4.259 (0.128) | 0.286 (0.000) |
| Ridge | 1.533 (0.024) | 3.192 (0.105) | 0.286 (0.000) |
| KL (as published) | 1.661 (0.022) | 3.892 (0.123) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.661 (0.022) | 3.892 (0.123) | 0.286 (0.000) |
| LASSO | 1.395 (0.031) | 2.323 (0.174) | 0.572 (0.023) |
| LASSO select -> Ridge | 1.472 (0.035) | 2.676 (0.174) | 0.572 (0.023) |
| LASSO select -> KL | 1.491 (0.038) | 2.744 (0.205) | 0.572 (0.023) |
| Trimmed-LASSO select -> Ridge | 1.116 (0.010) | 1.170 (0.078) | 0.490 (0.020) |
| **Trimmed-LASSO select -> KL** | 1.113 (0.010) | 1.148 (0.079) | 0.490 (0.020) |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=response, coefficients=sparse, rho=0.9, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.175 (0.041) | 5.875 (0.175) | 0.286 (0.000) |
| Ridge | 1.764 (0.026) | 3.777 (0.110) | 0.286 (0.000) |
| KL (as published) | 2.044 (0.038) | 5.212 (0.169) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 2.044 (0.038) | 5.212 (0.169) | 0.286 (0.000) |
| LASSO | 1.588 (0.034) | 2.871 (0.179) | 0.563 (0.021) |
| LASSO select -> Ridge | 1.701 (0.034) | 3.333 (0.166) | 0.563 (0.021) |
| LASSO select -> KL | 1.746 (0.047) | 3.465 (0.200) | 0.563 (0.021) |
| Trimmed-LASSO select -> Ridge | 1.099 (0.008) | 1.107 (0.068) | 0.507 (0.014) |
| **Trimmed-LASSO select -> KL** | 1.096 (0.008) | 1.074 (0.069) | 0.507 (0.014) |

Lowest mean test RMSE: Trimmed-LASSO select -> KL.

## contamination=response, coefficients=sparse, rho=0.99, eps=0.0  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.083 (0.006) | 4.045 (0.107) | 0.286 (0.000) |
| Ridge | 1.058 (0.005) | 3.094 (0.060) | 0.286 (0.000) |
| KL (as published) | 1.074 (0.005) | 3.687 (0.105) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.074 (0.005) | 3.687 (0.105) | 0.286 (0.000) |
| **LASSO** | 1.036 (0.005) | 2.118 (0.101) | 0.563 (0.017) |
| LASSO select -> Ridge | 1.047 (0.006) | 2.510 (0.119) | 0.563 (0.017) |
| LASSO select -> KL | 1.048 (0.006) | 2.465 (0.158) | 0.563 (0.017) |
| Trimmed-LASSO select -> Ridge | 1.083 (0.009) | 3.265 (0.177) | 0.494 (0.018) |
| Trimmed-LASSO select -> KL | 1.085 (0.010) | 3.305 (0.198) | 0.494 (0.018) |

Lowest mean test RMSE: LASSO.

## contamination=response, coefficients=sparse, rho=0.99, eps=0.1  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 1.700 (0.022) | 12.962 (0.310) | 0.286 (0.000) |
| Ridge | 1.290 (0.015) | 5.003 (0.113) | 0.286 (0.000) |
| KL (as published) | 1.593 (0.023) | 10.877 (0.341) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.593 (0.023) | 10.877 (0.341) | 0.286 (0.000) |
| LASSO | 1.304 (0.021) | 5.395 (0.251) | 0.396 (0.024) |
| LASSO select -> Ridge | 1.309 (0.016) | 5.262 (0.176) | 0.396 (0.024) |
| LASSO select -> KL | 1.369 (0.026) | 6.153 (0.384) | 0.396 (0.024) |
| **Trimmed-LASSO select -> Ridge** | 1.112 (0.008) | 3.624 (0.155) | 0.477 (0.017) |
| Trimmed-LASSO select -> KL | 1.112 (0.009) | 3.600 (0.186) | 0.477 (0.017) |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.

## contamination=response, coefficients=sparse, rho=0.99, eps=0.2  (n=200, p=30, reps=30)

| method | test RMSE | coefficient error | selection F1 |
|---|---|---|---|
| OLS | 2.174 (0.039) | 17.863 (0.470) | 0.286 (0.000) |
| Ridge | 1.424 (0.026) | 5.235 (0.118) | 0.286 (0.000) |
| KL (as published) | 1.987 (0.037) | 14.697 (0.511) | 0.286 (0.000) |
| KL (factor clipped to [0,1]) | 1.987 (0.037) | 14.697 (0.511) | 0.286 (0.000) |
| LASSO | 1.451 (0.029) | 5.933 (0.192) | 0.313 (0.027) |
| LASSO select -> Ridge | 1.469 (0.030) | 5.898 (0.194) | 0.313 (0.027) |
| LASSO select -> KL | 1.530 (0.039) | 6.536 (0.359) | 0.313 (0.027) |
| **Trimmed-LASSO select -> Ridge** | 1.075 (0.007) | 3.060 (0.150) | 0.521 (0.018) |
| Trimmed-LASSO select -> KL | 1.077 (0.009) | 3.091 (0.189) | 0.521 (0.018) |

Lowest mean test RMSE: Trimmed-LASSO select -> Ridge.
