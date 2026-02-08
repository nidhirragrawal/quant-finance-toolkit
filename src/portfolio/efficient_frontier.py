import numpy as np
from .markowitz import portfolio_return, portfolio_volatility, sharpe_ratio


def generate_random_weights(n_assets):
    weights = np.random.random(n_assets)
    return weights / np.sum(weights)


def simulate_portfolios(mean_returns, cov_matrix, n_portfolios=5000, risk_free_rate=0.0):
    """
    Simulates random portfolios and returns arrays of:
    - returns
    - volatilities
    - sharpes
    - weights list
    """
    results = np.zeros((3, n_portfolios))
    weights_record = []

    for i in range(n_portfolios):
        weights = generate_random_weights(len(mean_returns))
        weights_record.append(weights)

        port_ret = portfolio_return(weights, mean_returns)
        port_vol = portfolio_volatility(weights, cov_matrix)
        port_sharpe = sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate)

        results[0, i] = port_ret
        results[1, i] = port_vol
        results[2, i] = port_sharpe

    return results, weights_record


def max_sharpe_portfolio(results, weights_record):
    sharpe_idx = np.argmax(results[2])
    return {
        "return": results[0, sharpe_idx],
        "volatility": results[1, sharpe_idx],
        "sharpe": results[2, sharpe_idx],
        "weights": weights_record[sharpe_idx]
    }


def min_volatility_portfolio(results, weights_record):
    vol_idx = np.argmin(results[1])
    return {
        "return": results[0, vol_idx],
        "volatility": results[1, vol_idx],
        "sharpe": results[2, vol_idx],
        "weights": weights_record[vol_idx]
    }

