import numpy as np


def portfolio_return(weights, mean_returns):
    """
    Computes expected portfolio return.

    weights: np.array of shape (n_assets,)
    mean_returns: np.array of shape (n_assets,)
    """
    return np.dot(weights, mean_returns)


def portfolio_volatility(weights, cov_matrix):
    """
    Computes portfolio volatility (standard deviation).

    weights: np.array of shape (n_assets,)
    cov_matrix: np.array of shape (n_assets, n_assets)
    """
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


def sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.0):
    """
    Computes Sharpe ratio of portfolio.
    """
    port_ret = portfolio_return(weights, mean_returns)
    port_vol = portfolio_volatility(weights, cov_matrix)

    if port_vol == 0:
        return 0

    return (port_ret - risk_free_rate) / port_vol

